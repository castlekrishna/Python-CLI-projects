import random
import balancee
def line():
    print("-"*50)
def welcome_message():
    line()
    print("Welcome to Slot machine game")
    print("Try your luck")
    line()

def capture_responce():
    while True:
        try:
            responce = input("y or n: ").lower().strip()
            if responce == "y" or responce == "n":
                line()
                return responce
            else:
                line()
                print("Enter correct input...")
                line()
        except:
            line()
            print("Enter correct input...!!")
            line()

def assign_number(start,end):
    num = random.randint(start,end)
    return num


def index_responce(start,end):
    while True:
        try:
            user_responce = int(input("Enter index: ").strip())
            if start <= user_responce <= end:
                line()
                return user_responce
            else:
                line()
                print("Enter correct input...")
                line()
        except:
            line()
            print("Enter correct input...!!")
            line()

def print_lost(bet_amount,multiplier):
    print(f"You Won... (+{bet_amount*multiplier} chips)")
    balancee.win(bet_amount*multiplier)
    print(f"Current balance: {balancee.show_balance()}")
    line()

def print_win(bet_amount,multiplier):
    print(f"You Won... (+{bet_amount*multiplier} chips)")
    balancee.win(bet_amount*multiplier)
    print(f"Current balance: {balancee.show_balance()}")
    line()