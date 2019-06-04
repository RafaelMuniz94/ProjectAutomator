import sys
import os
from github import Github

userName = ""
password = ""

#class GithubController:

def get_User_Login():
    user = Github(userName,password).get_user()
    return user

def createRepo(projectName,description):
    user = get_User_Login()
    repo = user.create_repo(projectName,description)
    return repo.clone_url

'''def __init__(name,description):
    return createRepo(name,description)'''

print(createRepo(sys.argv[1],sys.argv[2]))