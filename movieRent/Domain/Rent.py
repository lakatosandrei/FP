from Domain.Client import Client
from Domain.Movie import Movie

class Rent(object):
    
    def __init__(self, idC, idM):
        self.__idC = idC
        self.__idM = idM

    def getIdClient(self):
        return self.__idC

    def getIdMovie(self):
        return self.__idM

    def setIdClient(self, idC):
        self.__idC = idC

    def setIdMovie(self, idM):
        self.__idM = idM
    
    def __eq__(self, ot):
        if ot == None:
            return False
        return self.__idC == ot.__idC and self.__idM == ot.__idM
    
    def __str__(self):
        return "Id Client: " + self.__idC + "\nId Film: " + self.__idM + "\n"

def test_Rent():
    client = Client('1', 'Vasile', '1950901125792')
    movie = Movie('1', 'Batman', 'Batman Rises', 'Action')
    rent = Rent(client.getId(), movie.getId())
    
    # Test getter-e
    assert rent.getIdClient() == '1'
    assert rent.getIdMovie() == '1'
    
    # Test setter-e
    rent.setIdClient('2')
    rent.setIdMovie('2')
    assert rent.getIdClient() == '2'
    assert rent.getIdMovie() == '2'
    
    # Test egal
    rent2 = Rent(client.getId(), movie.getId())
    assert rent != rent2
    rent2.setIdClient('2')
    rent2.setIdMovie('2')
    assert rent == rent2

test_Rent()