# entry is an element with a service name (website, social, etc...) a userID and a password
class entry:

    def __init__(self, service, userId, password):
        self.service = service
        self.userId = userId
        self.password = password

    def showPsw(self):
        print('WEBSITE: ', str(self.service), ' - USER: ', str(self.userId), ' - PASSWORD: ', str(self.password), '\n')

    def getPsw(self):
        return self.password

    def getSvc(self):
        return self.service

    def getUsr(self):
        return self.userId

    def editPsw(self):
        print("Please, type actual password:\n")
        actual = input()
        if actual == self.password:
            print('Please, type new password:\n')
            new = input()
            self.password = new
        else:
            print("Error! Failed to change password:\n")

    def editUsr(self):
        new = input('Please, type new username:\n')
        self.userId = new
