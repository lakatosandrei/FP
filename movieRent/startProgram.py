from Repository.clientRepository import clientRepository
from Domain.Validator import clientValidator, movieValidator
from Controller.Controller import inMemoryController
from UI.Console import Console
from Repository.movieRepository import movieRepository

clientRepo = clientRepository()
clientValidator = clientValidator()
movieRepo = movieRepository()
movieValidator = movieValidator()
controller = inMemoryController(clientRepo, clientValidator, movieRepo, movieValidator)
ui = Console(controller)

ui.showUI()