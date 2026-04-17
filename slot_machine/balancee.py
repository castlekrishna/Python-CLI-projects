import file_handling


    
def show_balance():
    user_data = file_handling.read_data()
    balance = f"{user_data["balance"]} chips"
    return balance
def show_user():
    user_data = file_handling.read_data()
    username = user_data["username"]
    return username

def win(amount):
    user_data = file_handling.read_data()
    user_data["balance"] += amount
    file_handling.write_data(user_data)

def lost(amount):
    user_data = file_handling.read_data()
    user_data["balance"] -= amount
    file_handling.write_data(user_data)

def bet_amount():
    while True:
        try:
            bet = float(input("Enter Chip amount to bet: "))
        except:
            print("Enter in numbers..")
        else:
            return bet
        
def zero_balance():
    user_data = file_handling.read_data()
    balance = user_data["balance"]
    if balance <= 0:
        return 1
    else:
        return 0