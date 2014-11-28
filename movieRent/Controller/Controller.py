from Domain.Client import Client
from Domain.Movie import Movie
from Repository.clientRepository import clientRepository
from Domain.Validator import clientValidator, movieValidator
from Repository.movieRepository import movieRepository
from Repository.rentRepository import rentRepository
from Domain.Rent import Rent

class clientController(object):

    def __init__(self, clientRepository, clientValidator):
        """
            Initializeaza repository-ul si validator-ul.
            Parametrii:
                        repository - repository-ul care trebuie folosit
                        validator - validatorul care trebuie folosit
        """
        self.__clientRepository = clientRepository
        self.__clientValidator = clientValidator
    
    def addClient(self, idC, nameC, CNP):
        """
            Creaza un client.
            Parametrii:
                        idC - id-ul clientului
                        nameC - numele clientului
                        CNP - CNP-ul clientului
        """
        # Cream un client
        client = Client(idC, nameC, CNP)
        # Validam clientul
        self.__clientValidator.validate(client)
        # Salvam clientul in repository
        self.__clientRepository.add(client)
    
    def updateClient(self, idC, nameC, CNP):
        """
            Actualizeaza un client.
            Parametrii:
                        idC - id-ul clientului
                        nameC - numele clientului
                        CNP - CNP-ul clientului
        """
        # Cream client-ul
        client = Client(idC, nameC, CNP)
        # Validam clientul
        self.__clientValidator.validate(client)
        # Actualizam clientul
        self.__clientRepository.update(client)

    def removeClient(self, ID):
        """
            Sterge un client.
            Parametrii:
                        ID - id-ul clientului care trebuie sters
        """
        del self.__clientRepository.getClients()[ID]

    def showClients(self):
        """
            Returneaza dictionarul de clienti.
        """
        return self.__clientRepository.getClients()
    
    def findClient(self, ID):
        """
            Returneaza clientul de la id-ul ID.
        """
        return self.__clientRepository.find(ID)

class movieController(object):

    def __init__(self, movieRepository, movieValidator):
        """
            Initializeaza repository-ul si validator-ul.
            Parametrii:
                        repository - repository-ul care trebuie folosit
                        validator - validatorul care trebuie folosit
        """
        self.__movieRepository = movieRepository
        self.__movieValidator = movieValidator

    def addMovie(self, idM, titleM, descriptionM, genreM):
        """
            Adauga un film.
            Parametrii:
                        idM - id-ul filmului
                        titleM - titlul filmului
                        descriptionM - descrierea filmului
                        genreM - tipul filmului
        """
        # Cream un film
        movie = Movie(idM, titleM, descriptionM, genreM)
        # Validam filmul
        self.__movieValidator.validate(movie)
        # Adaugam filmul
        self.__movieRepository.add(movie)
    
    def updateMovie(self, idM, titleM, descriptionM, genreM):
        """
            Actualizeaza un film.
            Parametrii:
                        idM - id-ul filmului
                        titleM - titlul filmului
                        descriptionM - descrierea filmului
                        genreM - tipul filmului
        """
        # Cream un film
        movie = Movie(idM, titleM, descriptionM, genreM)
        # Validam filmul
        self.__movieValidator.validate(movie)
        # Actualizam filmul
        self.__movieRepository.update(movie)

    def removeMovie(self, ID):
        """
            Sterge un film.
            Parametrii:
                        ID - id-ul filmului care trebuie sters
        """
        self.__movieRepository.remove(ID)
    
    def showMovies(self):
        """
            Returneaza dictionarul de filme.
        """
        return self.__movieRepository.getMovies()
    
    def findMovie(self, ID):
        """
            Returneaza filmul cautat.
        """
        return self.__movieRepository.find(ID)


class rentController(object):

    def __init__(self, repo):
        """
            Initializeaza repository-ul pentru inchirieri.
            Parametrii:
                        repo - repository-ul folosit
        """
        self.__rentRepository = repo

    
    def addRent(self, idC, idM):
        """
            Inchiriaza un film.
            Parametrii:
                        idC - id-ul clientului
                        idM - id-ul filmului
        """
        # Cream inchiriere
        rent = Rent(idC, idM)
        # Adaugam inchirierea
        self.__rentRepository.rentM(rent)

    
    def showRents(self):
        return self.__rentRepository.getRents()

    
    def removeRent(self, idR):
        """
            Returneaza un film.
            Parametrii:
                        idR - id-ul inchirierii
        """
        del self.__rentRepository.getRents()[idR]

def test_rentController():
    repo = rentRepository()
    contrl = rentController(repo)
    
    # Testam daca merge showRents
    assert contrl.showRents() == repo.getRents()
    
    # Testam daca merge inchirierea
    client = Client('1', 'Andrei', '1950901125792')
    movie = Movie('1', 'Batman', 'Batman Rises', 'Action')
    contrl.addRent(client.getId(), movie.getId())
    
    # Testam daca merge returnarea
    contrl.removeRent(client.getId() + ' ' + movie.getId())
    assert contrl.showRents() == repo.getRents()
    
test_rentController()

def test_clientController():
    repo = clientRepository()
    val = clientValidator()
    contrl = clientController(repo, val)
    
    # Testam daca merge showClients
    assert contrl.showClients() == repo.getClients()
    # Testam daca merge aduagarea
    client = Client('1', 'Andrei', '1950901125792')
    contrl.addClient('1', 'Andrei', '1950901125792')
    assert contrl.showClients()['1'] == client
    # Testam daca merge actualizarea
    client = Client('1', 'Vasile', '1950901125792')
    contrl.updateClient('1', 'Vasile', '1950901125792')
    assert contrl.showClients()['1'] == client
    # Testam daca merge stergerea
    contrl.removeClient('1')
    assert repo.getNrOfClients() == 0

test_clientController()

def test_movieController():
    repo = movieRepository()
    val = movieValidator()
    contrl = movieController(repo, val)
    
    # Testam daca merge showClients
    assert contrl.showMovies() == repo.getMovies()
    # Testam daca merge aduagarea
    movie = Movie('1', 'Batman', 'Batman Rises', 'Action')
    contrl.addMovie('1', 'Batman', 'Batman Rises', 'Action')
    assert contrl.showMovies()['1'] == movie
    # Testam daca merge actualizarea
    movie = Movie('1', 'Alladin', 'Alladin Flies', 'Adventure')
    contrl.updateMovie('1', 'Alladin', 'Alladin Flies', 'Adventure')
    assert contrl.showMovies()['1'] == movie
    # Testam daca merge stergerea
    contrl.removeMovie('1')
    assert repo.getNrOfMovies() == 0

test_movieController()