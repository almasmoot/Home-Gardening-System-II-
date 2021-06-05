import json
import random
def generate_new_data():
    with open("data.json", "r") as fileHandler:
        old_data = fileHandler.read()
    old_data_json = json.loads(old_data)
    data = {
        "home_screen": {
            "water_level": random.randrange(0, 100),
            "temp": random.randrange(0, 100),
            "humidity": random.randrange(0, 100),
            "water_pressure": random.randrange(0, 100),
        },
        "lighting_screen": {
            "start_time": old_data_json["lighting_screen"].get("start_time"),
            "end_time": old_data_json["lighting_screen"].get("end_time"),
        },
        "nutrient_screen": {
            "ppm": old_data_json["nutrient_screen"].get("ppm"),
        },
        "misting_screen": {
            "duration_min": old_data_json["misting_screen"].get("duration_min"),
            "duration_sec": old_data_json["misting_screen"].get("duration_sec"),
        },
    }

    # with open("data.json", "w") as fileHandler:
    #     fileHandler.write(json.dumps(data))
    #     "water_level": random.randrange(10, 100),
    #     "temp": random.randrange(49, 71),
    #     "humidity": random.randrange(0, 100),
    #     "water_pressure": random.randrange(0, 100)
    # }

    # open("test_data.json", "w").write(json.dumps(data))
