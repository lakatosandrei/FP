class RepositoryException(Exception):
    def __init__(self, errors):
        self.__errors = errors
    def getErrors(self):
        return self.__errors

class clientRepository(object):
    def __init__(self):
        self.__clients = {}
    
    def add(self, client):
        if client.getId() in self.__clients:
            # Daca avem un client cu acelasi ID ridicam exceptie
            raise RepositoryException(["Client with ID " + str(client.getId()) + " already exists."])
        # Altfel adaugam clientul in dictionar
        self.__clients[client.getId()] = client
    
    def update(self, client):
        if not client.getId() in self.__clients:
            # Daca nu exista client cu ID-ul dat de utilizator ridicam exceptie
            raise RepositoryException(["Can't update client with ID " + str(client.getId()) + " because it doesn't exist."])
        # Altfel actualizam clientul
        self.__clients[client.getId()] = client

    def remove(self, ID):
            del self.__clients[ID]

    def find(self, ID):
        if ID in self.__clients:
            return self.__clients[ID]
        else:
            return None

    def getClients(self):
        return self.__clients

    def getNrOfClients(self):
        return len(self.__clients)