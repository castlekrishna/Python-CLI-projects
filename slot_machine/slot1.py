import utils
def slot():
    wheel1 = utils.assign_number()
    wheel2 = utils.assign_number()
    wheel3 = utils.assign_number()

    print(f"{wheel1}    {wheel2}    {wheel3}")

    if wheel1 == wheel2 == wheel3:
        print("You Won...")
    else:
        print("you lost...")