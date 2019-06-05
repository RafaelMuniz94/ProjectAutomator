import sys
import os
from GithubController import GithubController

name = sys.argv[1]
description = sys.argv[2]

git = GithubController(name,description)
print(git.createRepo())