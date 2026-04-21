import utils,setting,router,balancee

def main():
    utils.welcome_message()
    while True:
        print(balancee.show_user())
        print(f"Balance: {balancee.show_balance()}")
        
        main_index=("""
            1. Play
            2. Setting
            3. Exit
        """)
        print(main_index)
        user_responce = utils.index_responce(1,3,main_index)
        if user_responce == 1:
            router.play()
        elif user_responce == 2:
            setting.setting()
        elif user_responce == 3:
            print("Do you wanna exit??")
            responce = utils.capture_responce()
            if responce == "y":
                print("Byee... have a good day :)")
                return
            if responce == "n":
                print("Cancelled operation")
                continue
        else:
            print("Invalid input...")

if __name__=="__main__":
    main()