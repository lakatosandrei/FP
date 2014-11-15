from Domain.Validator import ValidatorException, commandValidator
from Repository.clientRepository import RepositoryException
import cmd
class Console(object):
    def __init__(self, controller):
        self.__controller = controller
    

    def __addClient(self):
        """
            Functia care se ocupa cu adaugarea unui client nou.
            Variabile:
                        idC - id-ul clientului
                        nameC - numele clientului
                        CNP - CNP-ul clientului
        """
        self.__idC = input("Dati id-ul clientului: ")
        self.__nameC = input("Dati numele clientului: ")
        self.__CNP = input("Dati CNP-ul clientului: ")
        try:
            self.__controller.addClient(self.__idC, self.__nameC, self.__CNP)
            print("Client " + self.__nameC + " adaugat.")
        except RepositoryException as errors:
            self.__showErrors(errors.getErrors())
        except ValidatorException as errors:
            self.__showErrors(errors.getErrors())

    def __updateClient(self):
        """
            Functia care se ocupa cu actualizarea unui client.
            Variabile:
                        idC - id-ul clientului
                        nameC - numele clientului
                        CNP - CNP-ul clientului
        """
        if self.__controller.showClients().keys():
            self.__idC = input("Dati id-ul clientului: ")
            self.__nameC = input("Dati numele clientului: ")
            self.__CNP = input("Dati CNP-ul clientului: ")
            try:
                self.__controller.updateClient(self.__idC, self.__nameC, self.__CNP)
                print("Client " + self.__nameC + " actualizat.")
            except RepositoryException as errors:
                self.__showErrors(errors.getErrors())
            except ValidatorException as errors:
                self.__showErrors(errors.getErrors())
        else:
            print("Nu exista clienti momentan.")

    def __deleteCLient(self):
        """
            Functia care sterge un client.
            Variabile:
                        idC - id-ul dupa care trebuie sters clientul
                        possibleID - o lista cu fiecare id posibil
                        validator - validator-ul id-ului dat de utilizator
        """
        self.__possibleID = self.__controller.showClients().keys()
        if self.__possibleID:
            while True:
                self.__showClients()
                self.__idC = input('Selecteaza id client sau x pentru a te intoarce: ')
                if self.__idC == 'x':
                    break
                if self.__idC in self.__possibleID:
                    self.__controller.removeClient(self.__idC)
                    print ("\nClientul cu id-ul " + self.__idC + " a fost sters.\n")
                    break
                else:
                    print("\nClientul cu id-ul " + self.__idC + " nu exista.\n")
        else:
            print("Nu exista clienti momentan.\n")
    
    def __showClients(self):
        """
            Functia care arata toti clientii.
        """
        clients = self.__controller.showClients()
        if clients:
            for aux in clients:
                print(clients[aux])
            print('')
        else:
            print("Nu exista clienti momentan.")
    
    def __showErrors(self, errors):
        """
            Functia care afiseaza erorile primite.
            Parametrii:
                        errors - erorile care trebuie afisate
        """
        print('')
        for aux in errors:
            print(aux)
        print('')
    

    def __addMovie(self):
        """
            Functia care se ocupa cu adaugarea unui film nou.
            Variabile:
                        idM - id-ul filmului
                        titleM - titlul filmului
                        descriptionM - descrierea filmului
                        genreM - tipul filmului
        """
        self.__idM = input("Dati id-ul filmului: ")
        self.__titleM = input("Dati titlul filmului: ")
        self.__descriptionM = input("Dati descrierea filmului: ")
        self.__genreM = input("Dati tipul filmului: ")
        try:
            self.__controller.addMovie(self.__idM, self.__titleM, self.__descriptionM, self.__genreM)
            print("Film " + self.__titleM + " adaugat.")
        except RepositoryException as errors:
            self.__showErrors(errors.getErrors())
        except ValidatorException as errors:
            self.__showErrors(errors.getErrors())
    

    def __showMovies(self):
        """
            Aceasta functie printeaza filmele.
        """
        movies = self.__controller.showMovies()
        if movies:
            for aux in movies:
                print(movies[aux])
                print('')
        else:
            print("Nu exista filme momentan.")
    

    def __updateMovie(self):
        """
            Functia care se ocupa cu actualizarea unui client.
            Variabile:
                        idM - id-ul filmului
                        titleM - titlul filmului
                        descriptionM - descrierea filmului
                        genreM - tipul filmului
        """
        if self.__controller.showClients().keys():
            self.__idM = input("Dati id-ul filmului: ")
            self.__titleM = input("Dati titlul filmului: ")
            self.__descriptionM = input("Dati descrierea filmului: ")
            self.__genreM = input("Dati tipul fimlului: ")
            try:
                self.__controller.updateMovie(self.__idM, self.__titleM, self.__descriptionM, self.__genreM)
                print("Film " + self.__nameC + " actualizat.")
            except RepositoryException as errors:
                self.__showErrors(errors.getErrors())
            except ValidatorException as errors:
                self.__showErrors(errors.getErrors())
        else:
            print("Nu exista filme momentan.")
    
    def __deleteMovie(self):
        """
            Functia care sterge un film.
            Variabile:
                        idM - id-ul filmului
                        titleM - titlul filmului
                        descriptionM - descrierea filmului
                        genreM - tipul filmului
        """
        self.__possibleID = self.__controller.showMovies().keys()
        if self.__possibleID:
            while True:
                self.__showMovies()
                self.__idM = input('Selecteaza id film sau x pentru a te intoarce: ')
                if self.__idM == 'x':
                    break
                if self.__idM in self.__possibleID:
                    self.__controller.removeMovie(self.__idM)
                    print ("\nFilmulcu id-ul " + self.__idM + " a fost sters.\n")
                    break
                else:
                    print("\nFilmul cu id-ul " + self.__idM + " nu exista.\n")
        else:
            print("Nu exista filme momentan.\n")    

    def showUI(self):
        validator = commandValidator([0, 1, 2, 3, 4, 5, 6, 7, 8])
        while True:
            message =   """
                    Meniu:
                        0. Iesire
                        1. Adauga client.
                        2. Actualizeaza client.
                        3. Sterge clienti.
                        4. Arata clienti.
                        5. Adauga film.
                        6. Actualizeaza film.
                        7. Sterge film.
                        8. Arata filme.
                    Dati comanda: 
                        """
            dictionary = {'0':exit, '1':self.__addClient, '2':self.__updateClient, '3':self.__deleteCLient,
                          '4':self.__showClients, '5':self.__addMovie, '6':self.__updateMovie, '7':self.__deleteMovie, '8':self.__showMovies}
            cmd = input(message)
            try:
                validator.validate(cmd)
                dictionary[cmd]()
            except ValidatorException as errors:
                self.__showErrors(errors.getErrors())
