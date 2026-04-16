import utils
import slot1
def main():
    utils.welcome_message()
    while True:
        user_responce = input("Wanna play a game??? (y or n): ").lower().strip()
        if user_responce == "y":
            slot1.slot()
        elif user_responce == "n":
            print("Do you wanna exit??")
            responce = utils.capture_responce()
            if responce == "y":
                print("Byee... have a good day :)")
                return
            if responce == "n":
                print("Cancelled operation")
                continue

if __name__=="__main__":
    main()