class Client:
    def __init__(self, idC, nameC, CNP):
        self.__idC = idC
        self.__nameC = nameC
        self.__CNP = CNP
    
    def setId(self, idC):
        self.__idC = idC

    def setName(self, nameC):
        self.__nameC = nameC
        
    def setCNP(self, CNP):
        self.__CNP = CNP
        
    def getId(self):
        return self.__idC
    
    def getName(self):
        return self.__nameC
    
    def getCNP(self):
        return self.__CNP
    
    def __eq__(self, ot):
        return self.__idC == ot.__idC and self.__nameC == ot.__nameC and self.__CNP == ot.__CNP
    
    def __str__(self):
        self.__printID = "ID: " + str(self.__idC) + "\n"
        self.__printName = "Name: " + self.__nameC + "\n"
        self.__printCNP = "CNP: " + self.__CNP + "\n"
        return self.__printID + self.__printName + self.__printCNP