from Repository.client_repository import CLientRepository
from Domain.Client import Client

def client_test():
    clients = CLientRepository()

    # Verificam daca s-a creat dictionarul
    assert clients.getClients() == {}
    
    # Verificam daca merge adaugarea
    clients.add(Client(1, "Vasile", "1950901245678"))
    clients.add(Client(2, "Ion", "1950901456123"))
    assert clients.getNrOfClients() == 2
    
    # Testam daca se ridica exceptie in cazul in care exista deja un client cu acelasi ID
    try:
        clients.add(Client(1, "Vasile", "1950901245678"))
        assert False
    except KeyError:
        assert True
        
    # Daca s-a ridicat o exceptie nu trebuie adaugat in repository
    assert clients.getNrOfClients() == 2

    # Verificam daca merge cautarea
    assert clients.find(1) == Client(1, "Vasile", "1950901245678")

    # Verificam daca merge actualizarea
    clients.update(Client(1, "Gheorghe", "1950901245678"))
    assert clients.find(1) == Client(1, "Gheorghe", "1950901245678")
    
    # Daca s-a actualizat, numarul de clienti ramane neschimbat
    assert clients.getNrOfClients() == 2
    
    # Verificam daca merge stergerea
    clients.remove(2)
    assert clients.getNrOfClients() == 1
    

client_test()