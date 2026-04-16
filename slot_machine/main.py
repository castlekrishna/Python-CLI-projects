import utils
import slot1
import setting
import router
def main():
    utils.welcome_message()
    while True:
        print("""
            1. Play
            2. Setting
            3. Exit
        """)
        user_responce = utils.index_responce(1,3)
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

if __name__=="__main__":
    main()