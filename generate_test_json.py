import json
import random
def generate_new_data():
    data = {
        "water_level": random.randrange(0, 100),
        "temp": random.randrange(0, 100),
        "humidity": random.randrange(0, 100),
        "water_pressure": random.randrange(0, 100)
    }

    open("touch_screen/test_data.json", "w").write(json.dumps(data))
