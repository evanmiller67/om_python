#/usr/bin/env python3
"""
title: json_manipulation.py
author: exm5840
date(created): 2019-09-19 17:45:49 EDT
date (updated): 2019-09-19 17:45:49 EDT
"""
import json

with open('medical.json', 'r') as medical_rooms:
    data = json.load(medical_rooms)
    print(json.dumps(data, indent=4))
for room_name in data:
    print(room_name)
for room_name in data:
    print(f"{room_name} is in room {data[room_name]['room-number']}")
for room_name in data:
    data[room_name]['price'] = data[room_name]['price'] * 0.5
with open('medical.json', 'w') as medical_rooms:
  json.dump(data, medical_rooms, indent=4)
