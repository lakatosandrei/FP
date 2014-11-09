class Movie:
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
        return self.__idM == ot.__idM and self.__titleM == ot.__titleM and self.__descriptionM == ot.__descriptionM and self.__genreM == ot.__genreM
    