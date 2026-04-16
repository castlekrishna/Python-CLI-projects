import random
def line():
    print("-"*50)
def welcome_message():
    line()
    print("Welcome to Slot machine game")
    print("Try your luck")
    line()

def capture_responce():
    responce = input("y or n: ")
    return responce

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