from Repository.movieRepository import MovieRepository
from Domain.Movie import Movie

def movie_test():
    movies = MovieRepository()

    # Verificam daca s-a creat dictionarul
    assert movies.getMovies() == {}
    
    # Verificam daca merge adaugarea
    movies.add(Movie(1, "Batman", "Batman Rises", "Action"))
    movies.add(Movie(2, "Alladin", "Alladin Flies", "Adventure"))
    assert movies.getNrOfMovies() == 2
    
    # Testam daca se ridica exceptie in cazul in care exista deja un client cu acelasi ID
    try:
        movies.add(Movie(1, "Batman", "Batman Rises", "Action"))
        assert False
    except KeyError:
        assert True
        
    # Daca s-a ridicat o exceptie nu trebuie adaugat in repository
    assert movies.getNrOfMovies() == 2

    # Verificam daca merge cautarea
    assert movies.find(1) == Movie(1, "Batman", "Batman Rises", "Action")

    # Verificam daca merge actualizarea
    movies.update(Movie(1, "Dracula", "Dracula Bites", "Horror"))
    assert movies.find(1) == Movie(1, "Dracula", "Dracula Bites", "Horror")
    
    # Daca s-a actualizat, numarul de clienti ramane neschimbat
    assert movies.getNrOfMovies() == 2
    
    # Verificam daca merge stergerea
    movies.remove(2)
    assert movies.getNrOfMovies() == 1
    

movie_test()