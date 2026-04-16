import utils
def slot():
    while True:

        a11 = utils.assign_number()
        a12 = utils.assign_number()
        a13 = utils.assign_number()
        a21 = utils.assign_number()
        a22 = utils.assign_number()
        a23 = utils.assign_number()
        a31 = utils.assign_number()
        a32 = utils.assign_number()
        a33 = utils.assign_number()
        utils.line()
        print(f"""
                {a11}   {a12}   {a13}
                {a21}   {a22}   {a23}
                {a31}   {a32}   {a33}
    """)
        utils.line()

        if a11 == a12 == a13 or a21 == a22 == a23 or a31 == a32 == a33 or a11 == a22 == a33 or a13 == a22 == a31:
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