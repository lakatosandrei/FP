from Domain.Client import Client
from Domain.Movie import Movie
class inMemoryController:
    def __init__(self, clientRepository, clientValidator, movieRepository, movieValidator):
        """
            Initializeaza repository-ul si validator-ul.
            Parametrii:
                        repository - repository-ul care trebuie folosit
                        validator - validatorul care trebuie folosit
        """
        self.__clientRepository = clientRepository
        self.__clientValidator = clientValidator
        self.__movieRepository = movieRepository
        self.__movieValidator = movieValidator
    
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
        self.__clientRepository.remove(ID)

    def showClients(self):
        """
            Returneaza dictionarul de clienti.
        """
        return self.__clientRepository.getClients()
    
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
        self.__movieRepository.validate(movie)
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