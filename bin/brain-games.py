import sys
from pathlib import Path
# Разрешите расширить sys.path, добавив в него родительскую директорию.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.games.gcm import gameLCM
from src.games.progression import gameProgres
from src.engine import greetUser, playBrainGame

name = greetUser()

playBrainGame(gameLCM, name=name)

playBrainGame(gameProgres, name=name)
