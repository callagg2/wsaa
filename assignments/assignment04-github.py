# a program that reads a file from a repository, replaces all the instances of the text "Andrew" with your name
# and commits those changes and pushes the file back to the repository.

# Author: gerry callaghan

from github import Github # to use this install package pip install PyGithub

# Authentication is defined via github.Auth
from github import Auth

import requests
from config import config as cfg

# importing my github key from a config file, which is not included in the repository, and which is ignored by git
apikey = cfg["githubkey"]

# basing the following code on the example
# https://pygithub.readthedocs.io/en/latest/examples/Repository.html#update-a-file-in-the-repository

# using a fine-grained token I set up on Github

#authorization token based on my apikey
g = Github(auth=Auth.Token(apikey))

# use the token to access the repository
repo = g.get_repo("callagg2/aprivateone")

# set the variable contents to the file I want to edit
fileInfo = repo.get_contents("gemini_created_json_with_instances_of_andrew.json")

# now I have the file, I can get the url to download it, and then get the contents of the file
urlOfFile = fileInfo.download_url

# set response to the contents of the file
response = requests.get(urlOfFile)
# set contentOfFile to the text of the file
contentOfFile = response.text
#print (contentOfFile) # to preview the contents of the file

# make the change to the file, replacing all instances of "Andrew" with "Gerry"
newContents = contentOfFile.replace("Andrew", "Gerry")
# print (newContents) # to preview the changes

# reupload the file with the changes, and commit those changes to the repository
#  where fileInfo.path is the path to the file,
# "updated by prog" is the commit message,  
# newContents is the new content of the file, and
# fileInfo.sha is the sha of the file, which is needed to make sure we are updating the correct version of the file
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
# print (gitHubResponse) # just to see the file has been updated.

