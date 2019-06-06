import sys
import os
from GithubController import GithubController

name = sys.argv[1]
description = sys.argv[2]
path = sys.argv[3]

def createGitHub():
    git = GithubController(name,description)
    git.createRepo()
    if git.Error:
        print(git.Message)
        print(git.CloneUrl)
        print(git.CommitUrl)
        return False
    else:
        print(git.URL)
        print(git.CloneUrl)
        print(git.CommitUrl)
        return True

def createFolder():
    os.mkdir(path)

def createReadMe():
    filepath = path + "/README.md"
    readme = open(filepath,"w")
    readme.write(Text())


def Text():
    text = "Auto generated project structure by [ProjectAutomator](https://github.com/RafaelMuniz94/ProjectAutomator)"
    return text

createGitHub()
createFolder()
createReadMe()
