class Database():

    __users = {}


    def __contains__(self, user):

        return user in self.__users


    def addKey(self, user, value):

        self.__users[user]["keys"].append(value)


    def createUser(self, user):

        self.__users[user] = {"keys": [], "output": "", "input": ""}


    def destroy(self):

        self.__users.clear()


    def getInput(self, user):

        input = self.__users[user]["input"]
        self.__users[user]["input"] = ""
        return input 


    def getKeys(self, user):

        return self.__users[user]["keys"]


    def getOutput(self, user):

        output = self.__users[user]["output"]
        self.__users[user]["output"] = ""
        return output


    def setInput(self, user, value):

        self.__users[user]["input"] = value


    def setOutput(self, user, value):

        self.__users[user]["output"] = value


    @property
    def users(self):
        
        return list(self.__users.keys())
    