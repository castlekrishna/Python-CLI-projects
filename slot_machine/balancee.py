import file_handling,utils


    
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
            utils.line()
            print("Enter in numbers..")
            utils.line()
        else:
            while True:
                if bet > 0:
                    return bet
                else:
                    utils.line()
                    print("Invalid bet amount...")
                    utils.line()
                    break
def zero_balance():
    user_data = file_handling.read_data()
    balance = user_data["balance"]
    if balance == 0:
        return True
    else:
        return False    
def low_balance(bet_amount):
    user_data = file_handling.read_data()
    balance = user_data["balance"]
    if balance-bet_amount < 0:
        return True
    else:
        return False
def print_Zero_balance():
    utils.line()
    print("Low balance... ")
    print(f"Current Balance: {show_balance()}")
    utils.line()