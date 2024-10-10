import random

gameDescription = "What number is missing in the progression?"

def gameProgres():
    print(gameDescription)
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    length = random.randint(5, 10)

    progression = []

    for i in range(length):
        progression.append(start * (step ** i))

    correctAnswer = random.choice(progression)
    index = progression.index(correctAnswer)

    progression[index] = '...'

    question = progression

    return question, correctAnswer

