class Client(object):
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
        return self.__idC == ot.__idC
    
    def __str__(self):
        self.__printID = "ID: " + self.__idC + "\n"
        self.__printName = "Name: " + self.__nameC + "\n"
        self.__printCNP = "CNP: " + self.__CNP + "\n"
        return self.__printID + self.__printName + self.__printCNP
    
def test_Client():
    client = Client('1', 'Vasile', '1950901245672')
    
    # Test getID
    assert client.getId() == '1'
    
    # Test getName
    assert client.getName() == 'Vasile'
    
    # Test getCNP
    assert client.getCNP() == '1950901245672'
    
    # Test setId
    client.setId('2')
    assert client.getId() == '2'
    
    # Test setName
    client.setName('Andrei')
    assert client.getName() == 'Andrei'
    
    # Test setCNP
    client.setCNP('1850901234562')
    assert client.getCNP() == '1850901234562'
    
    # Test eq
    client2 = Client('2', 'Gheorghe', '1750902345623')
    assert client == client2
    
    # Test str
    string = client.__str__()
    assert string == 'ID: 2\nName: Andrei\nCNP: 1850901234562\n'

test_Client()