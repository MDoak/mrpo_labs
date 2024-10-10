def greetUser():
    print(f"Welcome to the Brain Games! \nMay I have your name?")
    name = input()
    print(f"Hello, {name}")
    return name

def playBrainGame(gameRound, name):

    for i in range(3):
        question, correctAnswer = gameRound()

        print(f"Question: {question} \n"
              f"Your answer: ")

        userAnswer = int(input())

        if userAnswer != correctAnswer:
            print(f"'{userAnswer}' is wrong answer ;(. Correct answer was '{correctAnswer}' \n"
                  f"Let's try again, {name}!")
        else:
            print(f"Correct! \nCongratulations, {name}!")
