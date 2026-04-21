import utils,balancee
import time
def num():
    return 1,3
def slot():
    bet_amount = balancee.bet_amount()

    while True:
        if balancee.low_balance(bet_amount) == False and balancee.zero_balance()==False:
            start = 1
            end = 7
            a11 = utils.assign_number(start=start,end=end)
            a12 = utils.assign_number(start=start,end=end)
            a13 = utils.assign_number(start=start,end=end)
            a21 = utils.assign_number(start=start,end=end)
            a22 = utils.assign_number(start=start,end=end)
            a23 = utils.assign_number(start=start,end=end)
            a31 = utils.assign_number(start=start,end=end)
            a32 = utils.assign_number(start=start,end=end)
            a33 = utils.assign_number(start=start,end=end)
            multiplier = utils.assign_number(2,12)
            utils.line()
            print(f"""
                    {a11}   {a12}   {a13}
                    {a21}   {a22}   {a23}       {multiplier}x
                    {a31}   {a32}   {a33}
        """)
            utils.line()

            if a11 == a12 == a13 or a21 == a22 == a23 or a31 == a32 == a33 or a11 == a22 == a33 or a13 == a22 == a31:
                utils.print_win(bet_amount=bet_amount,multiplier=multiplier)
            else:
                utils.print_lost(bet_amount=bet_amount,multiplier=multiplier)
            # time.sleep(00.3)
            print("Wanna Replay?? ")
            replay = utils.capture_responce()
            if replay == "y":
                continue
            else:
                return
        else:
            balancee.print_Zero_balance()
            break