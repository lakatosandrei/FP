from Domain.Client import Client
from Domain.Movie import Movie

class ValidatorException(Exception):
    def __init__(self, errors):
        self.__errors = errors
    
    def getErrors(self):
        return self.__errors

class clientValidator(object):
    
    def validate(self, client):
        """
            Arunca exceptia ValidateException in cazul in care trebuie.
            Parametrii:
                        client - client-ul care trebuie validat
            Variabile:
                        errors - o lista cu erori
        """
        errors = []
        if (client.getId() == ''):
            errors.append("Id nu poate fi null.")
        elif (not client.getId().isdigit()):
            errors.append("Id trebuie sa fie numar.")
        if (client.getName() == ''):
            errors.append("Name nu poate fi null.")
        if (client.getCNP() == ''):
            errors.append("CNP nu poate fi null.")
        elif (not client.getCNP().isdigit()):
            errors.append("CNP trebuie sa fie numar.")
        if len(client.getCNP()) != 13:
            errors.append("CNP trebuie sa aiba 14 cifre")
        elif client.getCNP()[0] != '1' and client.getCNP()[0] != '2':
            errors.append("CNP trebuie sa aiba prima cifra 1 sau 2(fata sau baiat)")
        if len(errors):
            raise ValidatorException(errors)


def test_clientValidator():
    validator = clientValidator()
    
    client = Client('', '', '')
    
    try:
        validator.validate(client)
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 4
    
    client = Client('1', '', '')
    try:
        validator.validate(client)
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 3
    
    client = Client('1', 'Vasile', '1950901123523')
    try:
        validator.validate(client)
        assert True
    except ValidatorException as errors:
        assert False
    
    client = Client('ceva', 'Vasile', '195023442234')
    try:
        validator.validate(client)
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 2
    
    client = Client('1', 'Vasile', '195023442234a')
    try:
        validator.validate(client)
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 1


class movieValidator(object):
    
    def validate(self, movie):
        """
            Arunca exceptia ValidatorException in cazul in care trebuie.
            Parametrii:
                        movie - movie-ul care trebuie validat
            Variabile:
                        errors - o lista cu erorile intalnite
        """
        errors = []
        
        if (movie.getId() == ''):
            errors.append("Id nu poate fi null.")
        elif (not movie.getId().isdigit()):
            errors.append("Id trebuie sa fie numar.")
        if (movie.getTitle() == ''):
            errors.append("Title nu poate fi null.")
        if (movie.getDescription() == ''):
            errors.append("Description nu poate fi null.")
        if (movie.getGenre() == ''):
            errors.append("Genre nu poate fi null.")
        if (len(errors) > 0):
            raise ValidatorException(errors)

def test_movieValidator():
    validator = movieValidator()
    
    movie = Movie('', '', '', '')
    try:
        validator.validate(movie)
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 4
    
    movie = Movie('1', 'Hanna', '', '')
    try:
        validator.validate(movie)
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 2
    
    movie = Movie('ab', 'Batman', 'Batman Rises', 'Action')
    try:
        validator.validate(movie)
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 1
    
    movie = Movie('1', 'Batman', 'Batman Rises', '')
    try:
        validator.validate(movie)
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 1
    
    movie = Movie('1', 'Batman', 'Batman Rises', 'Action')
    try:
        validator.validate(movie)
        assert True
    except ValidatorException:
        assert False

class commandValidator(object):
    
    def __init__(self, possibleCommands):
        self.__possibleCommands = possibleCommands
        
    def __returnPossible(self):
        """
            Aceasta functie printeaza comenzile posibile
            Variabile:
                        errorString - stringul care trebuie returnat
        """
        errorString = ''
        errorString += '\n'
        for aux in self.__possibleCommands:
            errorString += str(aux) + ','
        errorString = errorString[:-1]
        errorString += '\n'
        return errorString

    def validate(self, command):
        """
            Aceasta functie arunca ValidatorException in cazul in care trebuie.
            Parametrii:
                        command - un string care trebuie validat
            Variabile:
                        errors - o lista cu erorile intalnite
        """
        errors = []
        if not command.isdigit():
            errors.append("Comanda trebuie sa fie neaparat o cifra.")
        if command.isdigit() and int(command) not in self.__possibleCommands:
            errors.append("Comanda trebuie sa fie printre comenzile posibile: " + self.__returnPossible())
        if len(errors) > 0:
            raise ValidatorException(errors)

class rentValidator(object):
    def __init__(self):
        pass

def test_commandValidator():
    validator = commandValidator([0, 1, 2, 3, 4])
    
    try:
        validator.validate('ab')
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 1
    
    try:
        validator.validate('12')
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 1
    
    try:
        validator.validate('5')
        assert False
    except ValidatorException as errors:
        assert len(errors.getErrors()) == 1
    
    try:
        validator.validate('1')
        assert True
    except ValidatorException:
        assert False
    


test_commandValidator()
test_clientValidator()
test_movieValidator()
    