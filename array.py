import numpy as np

print("Hello, welcome to the pub quiz")

moon_question = np.array(["left", "right", "both"])
print("Which foot did Neil Armstrong first put on the moon?")
print(moon_question[0])
print(moon_question[1])
print(moon_question[2])
moon_answer = input("What is your guess?  ")
if moon_answer == moon_question[0]:
    print("Congrats that is the correct answer!")
else:
    print("Unlucky that's incorrect, it was his left foot!")

print("Next question")

drink_question = np.array(["water", "beer", "wine"])
print("Which is the most common drink in Europe?")
print(drink_question[0])
print(drink_question[1])
print(drink_question[2])
drink_answer = input("What is your guess?  ")
if drink_answer == drink_question[1]:
    print("Congrats that is the correct answer!")
else:
    print("Uh oh that's not right! The answer was beer!")

print("Okay, final question")

planet_question = np.array(["jupiter", "mars", "uranus"])
print("Apart from Venus, which planet rotates from east to west?")
print(planet_question[0])
print(planet_question[1])
print(planet_question[2])
planet_answer = input("What is your guess?  ")
if planet_answer == planet_question[2]:
    print("Congrats that is the correct answer!")
else:
    print("So close! It is of course uranus!")

print("That's all for today, I hope you enjoyed the pub quiz!")
