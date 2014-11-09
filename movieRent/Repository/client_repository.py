class CLientRepository:
    def __init__(self):
        self.clients = {}
    
    def add(self, client):
        if client.getId() in self.clients:
            # Daca avem un client cu acelasi ID ridicam exceptie
            raise KeyError("Client with ID " + str(client.getId()) + " already exists.")
        # Altfel adaugam clientul in dictionar
        self.clients[client.getId()] = client
    
    def update(self, client):
        if not client.getId() in self.clients:
            # Daca nu exista client cu ID-ul dat de utilizator ridicam exceptie
            raise KeyError("Can't update client with ID " + str(client.getId()) + " because it doesn't exist.")
        # Altfel actualizam clientul
        self.clients[client.getId()] = client

    def remove(self, ID):
        if not ID in self.clients:
            # Daca nu exista ID-ul dat de utilizator ridicam exceptie
            raise KeyError("Can't remove client with ID " + str(ID) + " because doesn't exist.")
        # Altfel, stergem clientul cu ID-ul dat de utilizator
        del self.clients[ID]

    def find(self, ID):
        if ID in self.clients:
            return self.clients[ID]
        else:
            return None

    def getClients(self):
        return self.clients

    def getNrOfClients(self):
        return len(self.clients)