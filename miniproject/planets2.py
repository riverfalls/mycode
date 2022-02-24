#!/usr/bin/env python3

def main():

    print("\nAmaze us with what you know about the planets in our solar system.")

    print("You'll have two attempts to answer each question. Let's get started!\n")

    x = 0                                   #start counter for question 1

    while True:
        x = x + 1                           #increase counter by +1
        print("Which planet has 14 moons?")
        answer_1 = input("Your answer: ")   #waits for user input

        if answer_1.lower() == "neptune":   #convert answer_1 to lower case string
            print("That's right! Great job!")
            break;
        elif x == 2:                        #ends after two unsuccessful attempts
            print("No, not " + answer_1 + ". Neptune has 14 moons")
            break;
        else:
            print("No, not " + answer_1 + ". Let's try again.\n")

    y = 0                                   #start counter for question 2

    while True:
        y = y + 1
        print("\nWhich planet has 10,759 Earth days in a year (i.e., one orbit around the Sun)?")
        answer_2 = input("Your answer: ")

        if answer_2.lower() == "saturn":
            print("Wow! You really know our planets.")
            break;

        elif y == 2:
            print("No, not " + answer_2 + ". Saturn rotates around the Sun in 10,759 days.")
            break;

        else:
            print("No, not " + answer_2 + ". Let's try again.") 

    z = 0                                   #start counter for question 3

    while True:
        z = z + 1
        print("\nWhich planet has 5,832 hours in one day?")
        answer_3 = input("Your answer: ")

        if answer_3.lower() == "venus":
            print("Now you're scaring me! Very few people know that about Venus.")
            break;

        elif z == 2:
            print("No, not " + answer_3 + ". Venus has 5,832 hours in one day.")
            break;

        else:
            print("No, not " + answer_3 + ". Let's try again.")

    print("\nThank you for sharing what you know about planets!\n")

main()
