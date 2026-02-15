# a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json".

# Author: gerry callaghan

import requests
import json

#common paths to CSO
url_begin = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
url_end = "/JSON-stat/2.0/en"

# ID of this dataset
dataset_id = "FIQ02" 

# complete url
url= url_begin + dataset_id + url_end

# Make the GET request to retrieve the dataset
response = requests.get(url)

# set our variable equal to the JSON data from the response
exchequer_data = response.json()

#print(exchequer_data)

# save the data in exchequer_data to a file called "cso.json" with indentation for readability
with open("cso.json", "w") as json_file:
    json.dump(exchequer_data, json_file, indent=4)

