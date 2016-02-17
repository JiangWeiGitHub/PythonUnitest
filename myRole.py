class myRole(object):
    
    def __init__(self):
        self.name = "john"
        self.age = 18

    def getName(self):
        return self.name
    
    def setName(self, name):
        if type(name) == str:
            self.name = name
        else:
            raise TypeError(r"'%s' is not right name format!" % name)
        
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        if type(age) == int:
            self.age = age
        else:
            raise TypeError(r"'%s' is not right age format!" % age)

