import random
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

def assign_number():
    num = random.randint(1,3)
    return num

# def confirm_responce(responce):
#     if responce == "n":
#         responce=input("Are you sure?(y or n): ").lower().strip()
#         if responce == "y" or responce == "n":
#             return responce
#         else:
#             print("Enter correct input: ")

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