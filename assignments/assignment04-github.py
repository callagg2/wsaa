# a program that reads a file from a repository, replaces all the instances of the text "Andrew" with your name
# and commits those changes and pushes the file back to the repository.

# Author: gerry callaghan

import requests
import json
from config import config as cfg

filename = "instances_of_andrew"

url = "https://api.github.com/repos/callagg2/aprivateone/contents/gemini_created_json_with_instances_of_andrew.json"
#url = "https://api.github.com/repos/callagg2/wsaa"
api_key = cfg["github_key"]
response = requests.get(url, auth = ('token', api_key))

print(response.status_code)
#print(response.json())

#gemini_created_json_with_instances_of_andrew.json

#'repo = 
#fileInfo = repo.get_contents("test.txt")

with open(filename, "w") as fp:
        data = response.json()
        json.dump(data, fp, indent=4)
