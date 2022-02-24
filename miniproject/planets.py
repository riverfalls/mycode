#!/usr/bin/env python3

def main():
    #start of counter
    x = 0

    print("Let's learn about the planets in our solar system.\n")

    while True:
        x = x + 1   #increase counter by +1
        print("Which planet has 14 moons?")
        answer = input("Your answer: ")

        if answer.lower() == "neptune":
            print("Correct! Great job!")
            break
        elif x == 2:
            print("No, not " + answer + ". Neptune has 14 moons")
            break
        else:
            print("No, not " + answer + ". Let's try again!\n")

main()
