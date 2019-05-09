#!/usr/bin/python3
import cgi
import os
import importlib
import json
import time
import random
import datetime

print("Content-Type: text/html")
print("")

data = cgi.FieldStorage()

response = {"status": True, "payload": None, "errors": []}

method_name = data.getvalue("method")


def verify_data():

    try:
        num_items = int(data.getvalue("items"))
    except:
        response["errors"].append("The number of items provided is not an integer")
        return False

    if method_name is None or num_items is None:
        response["errors"].append("At least one method is not selected or a number of items value is not provided.")
        return False

    if response["status"] and num_items > 1000000 or num_items < 1:
        response["errors"].append("Number of items is not between 1 and 100000")
        return False

    try:
        method = importlib.import_module("methods." + method_name)
    except:
        response["errors"].append("That method does not exist")
        return False

    return True


response["status"] = verify_data()

if response["status"]:
    num_items = int(data.getvalue("items"))
    method = importlib.import_module("methods." + method_name)
    start_time = time.time()
    variation = 1000
    items = [random.randrange(variation) for x in range(num_items)]
    method.mode(items)
    time_needed = str(time.time() - start_time)[:8]
    response["payload"] = time_needed

    stored = open("times.json", "r").read()
    stored_json = json.loads(stored)

    try:
        test = stored_json[method_name]["times"]
    except:
        stored_json[method_name] = {
            "times": []
        }

    stored_json[method_name]["times"].append({
        "timestamp": str(datetime.datetime.utcnow()).split(".")[0],
        "data": {
            "num_items": num_items,
            "exec_time": time_needed
        }
    })

    write_back = open("times.json", "w")
    write_back.write(json.dumps(stored_json))

print(json.dumps(response))
