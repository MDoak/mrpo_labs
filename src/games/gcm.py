import random

gameDescription = "Find the smallest common multiple of given numbers."

def findGCD(a, b):
    while b:
        [a, b] = [b, a % b]
    return a
def findLCM(a, b):
    return abs(a * b) / findGCD(a, b)
def gameLCM():
    print(gameDescription)
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    n3 = random.randint(1, 100)

    correctAnswer = findLCM(findLCM(n1, n2), n3)

    question = [n1, n2, n3]

    return question, correctAnswer

