import random
def printline():
    print("-"*50)



def game():
    computer_number = random.randint(0,100) 
    count = 1
    while True:
        user_input = int(input("Enter a number (0 ≤ number ≤ 100): "))
        printline()
        if user_input == computer_number:
            print("Yaayyyy...You guessed the number right")
            print(f"Attempt taken: {count}")
            printline()
            break
        elif 100 < user_input or user_input < 0:
            print("Bro... atleast write number in 0 ≤ number ≤ 100 range")
            printline()
        elif user_input>computer_number:
            print("Lower")
            printline()
        else:
            print("Higher")
            printline()
        count += 1

printline()
print(" "*15,"Number Guessing Game", " "*20)
printline()
while True:
    choice = input(("Wanna play a game(y/n)?: "))
    printline()
    if choice.lower() == "y":
        game()
    elif choice.lower() == "n":
        print("Thanks for playing...")
        printline()
        break
    else:
        print("Invalid Choice")
        printline()