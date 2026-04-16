import utils
def slot():
    while True:
        wheel1 = utils.assign_number()
        wheel2 = utils.assign_number()
        wheel3 = utils.assign_number()
        utils.line()
        print(f"{wheel1}    {wheel2}    {wheel3}")
        utils.line()
        if wheel1 == wheel2 == wheel3:
            print("You Won...")
            utils.line()
        else:
            print("you lost...")
            utils.line()

        print("Wanna Replay?? ")
        replay = utils.capture_responce()
        if replay == "y":
            continue
        else:
            return