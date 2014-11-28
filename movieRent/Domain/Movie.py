class Movie(object):
    def __init__(self, idM, titleM, descriptionM, genreM):
        self.__idM = idM
        self.__titleM = titleM
        self.__descriptionM = descriptionM
        self.__genreM = genreM

    def setId(self, idM):
        self.__idM = idM

    def setTitle(self, titleM):
        self.__titleM = titleM
    
    def setDescription(self, descriptionM):
        self.__descriptionM = descriptionM
    
    def setGenre(self, genreM):
        self.__genreM = genreM

    def getId(self):
        return self.__idM
    
    def getTitle(self):
        return self.__titleM
    
    def getDescription(self):
        return self.__descriptionM
    
    def getGenre(self):
        return self.__genreM
    
    def __eq__(self, ot):
        return self.__idM == ot.__idM
    
    def __str__(self):
        self.__printID = "ID: " + self.__idM + "\n"
        self.__printTitle = "Title: " + self.__titleM + "\n"
        self.__printDescription = "Description: " + self.__descriptionM + "\n"
        self.__printGenre = "Genre: " + self.__genreM + "\n"
        return self.__printID + self.__printTitle + self.__printDescription + self.__printGenre

def test_Movie():
    movie = Movie('1', 'Batman', 'Batman Rises', 'Action')
    
    # Test getID
    assert movie.getId() == '1'
    
    # Test getTitle
    assert movie.getTitle() == 'Batman'
    
    # Test getDescription
    assert movie.getDescription() == 'Batman Rises'
    
    # Test getGenre
    assert movie.getGenre() == 'Action'
    
    # Test setId
    movie.setId('2')
    assert movie.getId() == '2'
    
    # Test setTitle
    movie.setTitle('Spiderman')
    assert movie.getTitle() == 'Spiderman'
    
    # Test setDescription
    movie.setDescription('Spiderman Fights')
    assert movie.getDescription() == 'Spiderman Fights'
    
    # Test setGenre
    movie.setGenre('Adventure')
    assert movie.getGenre() == 'Adventure'
    
    # Test eq
    movie2 = Movie('2', 'Alladin', 'Alladin Flies', 'Adventure')
    assert movie == movie2
    
    # Test str
    string = movie.__str__()
    assert string == 'ID: 2\nTitle: Spiderman\nDescription: Spiderman Fights\nGenre: Adventure\n'

test_Movie()