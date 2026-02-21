# downloading repository from github using the API and authentication
#author: gerry callaghan


import requests
import json
from config import config as cfg

filename = "github_private_repo.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
# url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'
url = 'https://api.github.com/repos/callagg2/aprivateone'


# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["github_key"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
