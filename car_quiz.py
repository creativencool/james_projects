# Guess the car.

def check_guess(guess, answer):
    global score
    if guess == answer:
        print('Correct answer')
        score = score + 1

score = 0
print("Guess the Car!")
guess1 = input("Which car is fastest ?")
check_guess(guess1, "Race car")
guess2=input("How fast does a car go?")
check_guess(guess2,"200mph")
