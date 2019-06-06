
from github import Github

userName = ""
password = ""

class GithubController:

    def get_User_Login(self):
        if self.user is None:
            self.user = Github(userName,password).get_user()
           
        return self.user

    def createRepo(self):
        user = self.get_User_Login()

        try:
            self.__repo = user.get_repo(self.name)
            self.__error = True
            self.__message = 'Repositório já existe!'
            self.__url = self.__repo.clone_url
        except:
            self.__repo = user.create_repo(self.name,self.description)
            self.__url=  self.__repo.clone_url


    @property
    def Error(self):
        return self.__error

    @property
    def Message(self):
        return self.__message

    @property
    def URL(self):
        return self.__url
    @property
    def CommitUrl(self):
        return self.__repo.commits_url

    def CloneUrl(self):
        return self.__repo.clone_url


    def  __init__(self,name,description):
        self.name = name
        self.description = description
        self.user = None
        self.__url = None
        self.__error= False
        self.__message= None
        self.__repo = None
        

