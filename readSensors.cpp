#include "readSensors.h"
#include "Helper.h"
#include "PinAssignments.h"
#include "DHT11.h"
#include "ads1115.h"
#include "errorManager.h"
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
#include <Python.h>
#include <time.h>
#include "json.hpp"

struct timespec current_time_rs;

void *readSensors(void *ptr)
{
	string file_name = "sentData";
	json sentData;
	ifstream fileIn(file_name+".json");
	fileIn >> sentData;
	ofstream fileOut(file_name+".json");
    int nutrientFillAmount;    // The number of miliseconds it takes to have the parastalitc
   							    // pump on in order to reach the preferred TDS 
    float preferredTDS = 0;     // The TDS we want the reservoir to be (4mL of nutrient/gallon)
    float TDSMeasurement = 0;   // Measurement taken by the TDS sensor 
    int previoustime = 0;
    float waterLevel = 0;

    clock_gettime(CLOCK_REALTIME, &current_time_rs);
    int time = current_time_rs.tv_sec;
    printf("\nStarting readSensor Thread\nCurrent Time is %d\n\n", time);
    while (1)
    {
        int i = 0;
        bool valid = false;
        valid = sDHT1.read();
        printf( "DHT1: Humidity = %.2f %% Temperature = %.2f C (%.2f F) valid: %d\n",
            sDHT1.humidity,
            sDHT1.tempC,
            sDHT1.tempF,
            valid);
		sentData["Temperature"] = sDHT1.tempF;
        valid = sDHT2.read();
        printf( "DHT2: Humidity = %.2f %% Temperature = %.2f C (%.2f F) valid: %d\n",
            sDHT2.humidity,
            sDHT2.tempC,
            sDHT2.tempF,
            valid);
        valid = sDHT3.read();
        printf( "DHT3: Humidity = %.2f %% Temperature = %.2f C (%.2f F) valid: %d\n",
            sDHT3.humidity,
            sDHT3.tempC,
            sDHT3.tempF,
            valid);		
        // Find the TDS of the water before any nutrient is put in
        TDSMeasurement = readTDS();
		sentData["Concentration"] = TDSMeasurement;
        printf("TDS is %.3fv\n", TDSMeasurement);

        waterLevel = measureWaterLevel();
		sentData["WaterLevel"]=waterLevel;
        printf("Water level is %.2fin\n", waterLevel);
        if (waterLevel < LOWWATERLIMIT) // Is the water level less than an inch?
        {
            reservoirWasDrained = true;
        }
        if (reservoirWasDrained == true && waterLevel > FULLWATER)  // This means that the reservoir was 
        {                           					            // drained and then filled again
            calibratePreferredTDS();
            reservoirWasDrained = false;
        }
        // Ventilation system
        if(sDHT1.tempF >= HOTTEMPTHRESHF)
        {
            highTempFlag = true;
        }
        else if(sDHT1.tempF <= COLDTEMPTHRESHF) //Make sure the temperature is real
        {

            //Send an email saying requesting to add water to reservoir
            clock_gettime(CLOCK_REALTIME, &current_time_rs);
            currTimeCold = current_time_rs.tv_sec;
            lowTempFlag = true;    //We always want this to trigger regardless of delay.
#ifndef DEBUGNOEMAILDELAY
            if(currTimeCold - previousTimeCold >= EMAILLAG)  // Will always report the first time
            {
#endif // !DEBUGNOEMAILDELAY
                Warning("Room is too cold; Please turn the temperature of the room up by at least %4.1f degrees fahrenheit.", (COLDTEMPTHRESHF - sDHT3.tempF));
#ifndef DEBUGNOEMAILDELAY
                previousTimeCold = currTimeCold;   // Set the current time to be the previous time
            }
#endif // !DEBUGNOEMAILDELAY
        }
        else
        {
            lowTempFlag = false;
            highTempFlag = false;
            previousTimeCold = 0;  // Allow the email to be sent immediately if another occurance happens
        }
        // Now that the flags are updated, have the ventChamber function update the vent fan
        ventChamber(); 
   
        // Replace nutrient (only if there is water in the reservoir and
	    // the preferredTDS variable has been calibrated)
	    if(reservoirWasDrained == false)
        {
            TDSMeasurement = readTDS();
            printf("TDS is %f\n", TDSMeasurement);
            if (TDSMeasurement > (preferredTDS + EXCESSNUTRIENT)) // The reservoir has too much nutrient if the solution is 
            {                                                     // more than *100* ppt greater than the preferredTDS
            //Send an email saying requesting to add water to reservoir
            clock_gettime(CLOCK_REALTIME, &current_time_rs);
            currTDSTime = current_time_rs.tv_sec;
            tooMuchNutrientFlag = true;   //We always want this to trigger regardless of delay.
#ifndef DEBUGNOEMAILDELAY
            if (currTDSTime - previousTDSTime >= EMAILLAG)  // Will always report the first time
            {
#endif // !DEBUGNOEMAILDELAY
                Critical("The reservoir has too much nutrient; Please fill reservoir with 1 cup of water to dillute nutrient.");
#ifndef DEBUGNOEMAILDELAY
                previousTDSTime = currTDSTime;  // Set the current time to be the previous time
            }
#endif // !DEBUGNOEMAILDELAY
        }
        else
        {
            tooMuchNutrientFlag = false;
            previousTDSTime = 0; // Allow the email to be sent immediately if another occurance happens
        }
        while ((TDSMeasurement + LOWNUTRIENTLIM) < preferredTDS) // The TDS of the solution can be less than
        {
               														// the preferred TDS by *30* ppt
            // Find out how much time the pump must be on in order to fully replace the nutrients
            nutrientFillAmount = (preferredTDS - TDSMeasurement)*TDSTOML;
            // Inject nutrient and mix solution
            injectNutrient(mlts(nutrientFillAmount));
            delay(1000);    //This is how long until the water settles down after being mixed by high pressure
            TDSMeasurement = readTDS();  // Verify that the nutrient was sufficient and the while loop can be exited
        }
    }
		
      // Water level
		waterLevel = measureWaterLevel();
        if (waterLevel < LOWWATER) // 5 inches
        {
#ifdef DEBUGWLS
			printf("Current Water Level is: %f\n", waterLevel);
#endif // DEBUGWLS
            //Send an email saying requesting to refill reservoir
            clock_gettime(CLOCK_REALTIME, &current_time_rs);
            currTimeWL = current_time_rs.tv_sec;
#ifndef DEBUGNOEMAILDELAY
			if(currTimeWL - previousTimeWL >= EMAILLAG)  // Will always report the first time
            {
#endif // !DEBUGNOEMAILDELAY
               Critical("Reservoir water level is below %1.2f inches; Please fill reservoir with %1.2f more inches of water.", 
                        LOWWATER, 
                        (waterLevel > 0)?(FULLWATER - waterLevel):FULLWATER);
#ifndef DEBUGNOEMAILDELAY
               previousTimeWL = currTimeWL; // Set the current time to be the previous time
            }
#endif // !DEBUGNOEMAILDELAY

            digitalWrite(WATERLEVELLEDPIN, HIGH);
         }
      else
      {
         digitalWrite(WATERLEVELLEDPIN, LOW);
         previousTimeWL = 0;  // Allow the email to be sent if another occurance happens
      }
      // Since the injectNutrient function fills the reservoir a little to mix up the nutrient,
      // check the water level AFTER replacing the nutrient
	   
      //TODO look for high humidity and vent chamber.
      //TODO implement system clock to time events.
      printf("\n");
	  fileout << sentData;
      delay(5000);
   }
}