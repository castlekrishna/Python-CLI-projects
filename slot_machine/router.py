import slot1,slot2,utils
def play():
    while True:
        index = ("""
            What do you wanna play?
                1. Slot1 (3*1)
                2. Slot2 (3*3)
                3. exit
            """)
        print(index)
        utils.line()
        
        responce = utils.index_responce(1,3,index)
        
        if responce == 1:
            slot1.slot()
        elif responce == 2:
            slot2.slot()
        elif responce == 3:
            return
        else:
            print("Invalid input...")
            utils.line()