# Number utility (prime, palindrome, Armstrong )
#printline
def printline():
    print("----------------------------------------")
#prime number
def prime(num):
    flag = True
    if num <= 1:
        print(f"{num} is not prime number")
        printline()
        return
    elif num == 2:
        print(f"{num} is prime number")
        printline()
        return
    else:
        for i in range(2,num):
            if num % i ==0:
                flag = False
                break
    if flag:
        print(f"{num} is prime...!!")
        printline()
    else:
        print(f"{num} is not prime...!!")
        printline()
#palindrome 
def palindrome(num):
    original = num
    reverse = 0
    result = 0
    while num != 0:
        reverse = num % 10
        result = result*10+reverse
        num = num // 10
    if result == original:
        print(f"{original} is palindrome")
        printline()
    else:
        print(f"{original} is not palindrome")
        printline()
#Armstrong
def armstrong(num):
    reminder = 0
    result = 0
    original = num
    original2 = num
    length =0
    while num !=0:
        num = num // 10
        length+=1
    while original != 0:
        reminder = original % 10
        result += reminder**length
        original = original // 10
    if result ==  original2:
        print(f"{original2} is armstrong")
        printline()
    else:
        print(f"{original2} is not armstrong")
        printline()
#main
while True:
    printline()
    print("1. Check Prime\n2. Check palindrome\n3. Check Armstrong\n0. Exit")
    printline()
    choice = int(input("Enter Index: "))
    printline()
    if 3<choice or choice < 0:
        print("Invalid Index...!!")
        printline()
        continue
    if choice == 0:
        print("Thanks for using Number utility....")
        printline()
        break
    num = int(input("Enter number to check: "))
    printline()
    if choice == 1:
        prime(num)
    elif choice == 2:
        palindrome(num)
    else:
        armstrong(num)