import random
def line():
    print("-"*50)

# game
def game(starting_number,ending_number,attempt):
    computer_number = random.randint(starting_number,ending_number)
    while True:
        user_input = int(input(f"Enter a number ({starting_number} ≤ number ≤ {ending_number}): "))
        line()
        if user_input == computer_number:
            print("Yaayyy...You guessed the number right")
            print(f"Attempt taken: {attempt}")
            line()
            break
        elif ending_number < user_input or user_input < starting_number:
            print(f"Bro... atleast write number in {starting_number} ≤ number ≤ {ending_number} range")
            line()
        elif user_input>computer_number:
            print("Lower")
            line()
        elif user_input < computer_number:
            print("Higher")
            line()
        else:
            print("Invalid input...")
            line()
        attempt += 1

#game options
def gameoptions():
    print("Choose difficulty\n1. Easy\n2. Medium\n3. Hard\n4. Custom\n0. Exit")
    line()
    while True:
        try:
            choice = int(input("Enter index: "))
            line()
        except:
            print("Enter correct choice...")
            line()
        else:
            if choice == 1:
                return 0,50
            elif choice == 2:
                return(0,100)
            elif choice == 3:
                return(0,500)
            elif choice == 4:
                try:
                    starting_number = int(input("Enter starting number: "))
                except:
                    print("Invalid input...!!")
                    line()
                else:
                    try:
                        ending_number = int(input("Enter ending number: "))
                    except:
                        print("Invalid input...!!")
                        line()
                    else:
                        if starting_number > ending_number:
                            print("Ending point is less than starting point.. please enter a valid input..!!")
                        else:
                            return starting_number,ending_number
            elif choice == 0:
                return
#main
line()
print(" "*15,"Number Guessing Game", " "*20)
line()
while True:
    print("1. Play\n2. Stats\n0. Exit")
    line()
    try:
        choice = int(input(("Enter Index: ")))
        line()
    except:
        line()
        print("Invalid input...!!")
        line()
    else:
        if choice == 1:
            parameter = gameoptions()
            if gameoptions is None:
                print("Exiting...!!")
            else:
                game(*parameter,1)
        elif choice == 0:
            print("Thanks for playing...")
            line()
            break
        else:
            print("Invalid Choice")
            line()