from src.games.gcm import gameLCM
from src.games.progression import gameProgres
from src.engine import greetUser, playBrainGame

name = greetUser()

playBrainGame(gameLCM, name=name)

playBrainGame(gameProgres, name=name)
