#0 to exitt
def exitt():
    while True:
        opt = int(input("Enter 0 to exitt: "))
        printline()
        if opt == 0:
            break
        else:
            print("Invalid Input...!!")
            printline()
#print line function
def printline():
    print("------------------------------------")
#sum funtion
def add(num1,num2):
    printline()
    print(f"Sum = {num1+num2}")
    printline()
    exitt()
#Subtraction function
def sub(num1,num2):
    printline()
    print(f"Subtraction = {num1-num2}")
    printline()
    exitt()
#multiplication function
def mul(num1,num2):
    printline()
    print(f"Multiplication: {num1*num2}")
    printline()
    exitt()
#divide function
def div(num1,num2):
    printline()
    if num2 == 0:
        print("Invalid denominator..!!")
    else:
        print(f"Division = {num1/num2}")
    printline()
    exitt()
#Reminder function
def rem(num1,num2):
    printline()
    print(f"Reminder = {num1%num2}")
    printline()
    exitt()
#main function
while True:
    printline()
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Reminder")
    print("0. exitt")
    printline()
    choice = int(input("Enter index: "))
    printline()
    if choice == 0:
        print("Thanks for using Basic calculator...")
        printline()
        break
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    if choice == 1:
        add(num1,num2)
    elif choice == 2:
        sub(num1,num2)
    elif choice == 3:
        mul(num1,num2)
    elif choice == 4:
        div(num1,num2)
    elif choice == 5:
        rem(num1,num2)
    else:
        print("Invalid Input...!!")
        printline()