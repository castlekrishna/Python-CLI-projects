import slot1,slot2,utils
def play():
    while True:
        print("""
            What do you wanna play?
                1. Slot1 (3*1)
                2. Slot2 (3*3)
                3. exit
            """)
        utils.line()
        try:
            responce = int(int(input("Enter index: ").strip()))
        except:
            print("Enter integer...")
            utils.line()
        if responce == 1:
            slot1.slot()
        if responce == 2:
            slot2.slot()
        if responce == 3:
            return