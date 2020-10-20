#! /usr/bin/env python3

import os
import requests

path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

files = os.listdir(path)

for file in files:
    if file.endswith(".txt"):
        with open(path+file, 'r') as f:
            f_name = os.path.splitext(file)[0]
            data = f.read()
            data = data.split("\n")

            f_dict = {"name":data[0],"weight":data[1].strip("lbs"),"description":data[2],"image_name":f_name+".jpeg"}
            response = requests.post(url, json=f_dict)
            response.raise_for_status()

