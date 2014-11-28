from Repository.clientRepository import RepositoryException
from Domain.Client import Client
from Domain.Movie import Movie
from Domain.Rent import Rent

class rentRepository(object):
    def __init__(self):
        self.__rents = {}
    
    def rentM(self, rent):
        """
            Adauga inchirerea in dictionar la id-ul format din adunarea id-ului clientului + cea
        a filmului.
        """
        self.__rents[rent.getIdClient() + ' ' + rent.getIdMovie()] = rent

    def find(self, idR):
        """
            Returneaza o inchiriere cu id-ul idR, daca exista.
        """
        #print(idR, list(self.__rents.keys()))
        if idR not in list(self.__rents.keys()):
            # Daca nu exista returnam None
            return None
        # Altfel returnam elementul
        return self.__rents[idR]
    
    def getRents(self):
        return self.__rents

    def getNrOfRents(self):
        return len(self.__rents.keys())

    def returnM(self, idR):
        if idR not in self.__rents:
            raise RepositoryException(["Nu exista inchiriere cu id-ul " + idR + "."])
        del self.__rents[idR]

def test_rentRepository():
    repo = rentRepository()
    
    client = Client('1', 'Andrei', '1950901125782')
    movie = Movie('1', 'Batman', 'Batman Rises', 'Action')
    rent = Rent(client.getId(), movie.getId())
    
    # Testam adaugarea
    repo.rentM(rent)
    assert repo.getNrOfRents() == 1
    
    # Testam cautarea
    assert repo.find('1 1') == rent
    
    # Testam returnarea
    repo.returnM('1 1')
    assert repo.getNrOfRents() == 0

test_rentRepository()