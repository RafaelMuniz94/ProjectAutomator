
from github import Github

userName = ""
password = ""

class GithubController:

    def get_User_Login(self):
        user = Github(userName,password).get_user()
        return user

    def createRepo(self):
        user = self.get_User_Login()
        repo = user.create_repo(self.name,self.description)
        return repo.clone_url

    def commitRepo(self):
        userName

    def  __init__(self,name,description):
        self.name = name
        self.description = description
        

