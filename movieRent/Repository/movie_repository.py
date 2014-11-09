class MovieRepository:
    def __init__(self):
        self.movies = {}
    
    def add(self, movie):
        if movie.getId() in self.movies:
            # Daca avem un movie cu acelasi ID ridicam exceptie
            raise KeyError("Movie with ID " + str(movie.getId()) + " already exists.")
        # Altfel adaugam movieul in dictionar
        self.movies[movie.getId()] = movie
    
    def update(self, movie):
        if not movie.getId() in self.movies:
            # Daca nu exista movie cu ID-ul dat de utilizator ridicam exceptie
            raise KeyError("Can't update movie with ID " + str(movie.getId()) + " because it doesn't exist.")
        # Altfel actualizam movie-ul
        self.movies[movie.getId()] = movie

    def remove(self, ID):
        if not ID in self.movies:
            # Daca nu exista ID-ul dat de utilizator ridicam exceptie
            raise KeyError("Can't remove movie with ID " + str(ID) + " because doesn't exist.")
        # Altfel, stergem movie-ul cu ID-ul dat de utilizator
        del self.movies[ID]

    def find(self, ID):
        if ID in self.movies:
            return self.movies[ID]
        else:
            return None

    def getMovies(self):
        return self.movies

    def getNrOfMovies(self):
        return len(self.movies)