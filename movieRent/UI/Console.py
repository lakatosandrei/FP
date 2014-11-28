from Domain.Validator import ValidatorException, commandValidator
from Repository.clientRepository import RepositoryException
import cmd
class Console(object):
    
    def __init__(self, clientController, movieController, rentController):
        self.__clientController = clientController
        self.__movieController = movieController
        self.__rentController = rentController
    
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
            self.__clientController.addClient(self.__idC, self.__nameC, self.__CNP)
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
        if self.__clientController.showClients().keys():
            self.__idC = input("Dati id-ul clientului: ")
            self.__nameC = input("Dati numele clientului: ")
            self.__CNP = input("Dati CNP-ul clientului: ")
            try:
                self.__clientController.updateClient(self.__idC, self.__nameC, self.__CNP)
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
        self.__possibleID = self.__clientController.showClients().keys()
        if self.__possibleID:
            while True:
                self.__showClients()
                self.__idC = input('Selecteaza id client sau x pentru a te intoarce: ')
                if self.__idC == 'x':
                    break
                if self.__idC in self.__possibleID:
                    self.__clientController.removeClient(self.__idC)
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
        clients = self.__clientController.showClients()
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
            self.__movieController.addMovie(self.__idM, self.__titleM, self.__descriptionM, self.__genreM)
            print("Film " + self.__titleM + " adaugat.")
        except RepositoryException as errors:
            self.__showErrors(errors.getErrors())
        except ValidatorException as errors:
            self.__showErrors(errors.getErrors())
    

    def __showMovies(self):
        """
            Aceasta functie printeaza filmele.
        """
        movies = self.__movieController.showMovies()
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
        if self.__movieController.showClients().keys():
            self.__idM = input("Dati id-ul filmului: ")
            self.__titleM = input("Dati titlul filmului: ")
            self.__descriptionM = input("Dati descrierea filmului: ")
            self.__genreM = input("Dati tipul fimlului: ")
            try:
                self.__movieController.updateMovie(self.__idM, self.__titleM, self.__descriptionM, self.__genreM)
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
        self.__possibleID = self.__movieController.showMovies().keys()
        if self.__possibleID:
            while True:
                self.__showMovies()
                self.__idM = input('Selecteaza id film sau x pentru a te intoarce: ')
                if self.__idM == 'x':
                    break
                if self.__idM in self.__possibleID:
                    self.__movieController.removeMovie(self.__idM)
                    print ("\nFilmulcu id-ul " + self.__idM + " a fost sters.\n")
                    break
                else:
                    print("\nFilmul cu id-ul " + self.__idM + " nu exista.\n")
        else:
            print("Nu exista filme momentan.\n")    


    def __findMovie(self):
        """
            Functia care cauta un film dupa id.
            
        """
        self.__possibleID = self.__movieController.showMovies().keys()
        if self.__possibleID:
            while True:
                self.__idM = input('Da un id sau x pentru a iesi: ')
                if self.__idM == 'x':
                    break
                if self.__idM in self.__possibleID:
                    print(self.__movieController.findMovie(self.__idM))
                    break
                else:
                    print("\nFilmul cu id-ul " + self.__idM + " nu exista.\n")
        else:
            print("Nu exista filme momentan.\n")

    def __findClient(self):
        """
            Functia care cauta un film dupa id.
            
        """
        self.__possibleID = self.__clientController.showClients().keys()
        if self.__possibleID:
            while True:
                self.__idC = input('Da un id sau x pentru a iesi: ')
                if self.__idC == 'x':
                    break
                if self.__idC in self.__possibleID:
                    print(self.__clientController.findClient(self.__idC))
                    break
                else:
                    print("\nClientulcu id-ul " + self.__idM + " nu exista.\n")
        else:
            print("Nu exista clienti momentan.\n")        
    

    def __rentMovie(self):
        """
            Functia care inchiriaza un film.
        """
        self.__possibleIDClient = self.__clientController.showClients().keys()
        self.__possibleIDMovie = self.__movieController.showMovies().keys()
        ret = False
        if not self.__possibleIDClient:
            ret = True
            print("Nu exista clienti momentan.")
        if not self.__possibleIDMovie:
            ret = True
            print("Nu exista filme momentan.")
        if ret:
            return None
        while True:
            self.__showClients()
            while True:
                idC = input("Selectati un id pentru client: ")
                if idC in self.__possibleIDClient:
                    break
                else:
                    print("Clientul cu id-ul " + idC + " nu exista.")
            self.__showMovies()
            while True:
                idM = input("Selectati un id pentru film: ")
                if idM in self.__possibleIDMovie:
                    break
                else:
                    print("Filmul cu id-ul " + idM + " nu exista.")
            break
        print("Filmul cu id-ul " + idM + " a fost inchiriat clientului cu id-ul " + idC + ".")
        self.__rentController.addRent(idC, idM)
    

    def __removeRent(self):
        """
            Functia care returneaza un film.
        """
        self.__possibleID = self.__rentController.showRents().keys()
        self.__showRents()
        if self.__possibleID:
            while True:
                self.__idR = input('Da un id de inchiriere sau x pentru a iesi: ')
                if self.__idR == 'x':
                    break
                if self.__idR in self.__possibleID:
                    self.__rentController.removeRent(self.__idR)
                    break
                else:
                    print("\nInchirierea cu id-ul " + self.__idM + " nu exista.\n")
        else:
            print("Nu exista inchirieri momentan.")     
    
    def __showRents(self):
        """
            Aceasta functie printeaza filmele.
        """
        rents = self.__rentController.showRents()
        if rents:
            for aux in rents:
                print("Id inchiriere: " + aux)
                print("Client")
                print(self.__clientController.findClient(rents[aux].getIdClient()))
                print("Film")
                print(self.__movieController.findMovie(rents[aux].getIdMovie()))
                print('')
        else:
            print("Nu exista inchirieri momentan.")
    
    def showUI(self):
        validator = commandValidator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        while True:
            message =   """
            +-------------------------------------------------------------------------------+
            |      Clienti      |      Filme      |      Inchiriere      |      Sistem      |
            |-------------------------------------------------------------------------------|
            |1. Adauga          | 6. Adauga       | 11. Inchiriaza film  | 0. Iesire        |
            |2. Actualizeaza    | 7. Actualizeaza | 12. Sterge           |                  |
            |3. Sterge          | 8. Sterge       | 13. Arata            |                  |
            |4. Arata           | 9. Arata        |                      |                  |
            |5. Cauta           | 10. Cauta       |                      |                  |
            +-------------------------------------------------------------------------------+
            Dati comanda: 
                        """
            dictionary = {'0':exit, '1':self.__addClient,
                          '2':self.__updateClient, '3':self.__deleteCLient,
                          '4':self.__showClients, '5':self.__findClient,
                          '6':self.__addMovie, '7':self.__updateMovie,
                          '8':self.__deleteMovie, '9':self.__showMovies,
                          '10':self.__findMovie, '11':self.__rentMovie,
                          '12':self.__removeRent, '13':self.__showRents}
            cmd = input(message)
            try:
                validator.validate(cmd)
                dictionary[cmd]()
            except ValidatorException as errors:
                self.__showErrors(errors.getErrors())
