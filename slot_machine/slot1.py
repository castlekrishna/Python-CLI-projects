import utils,balancee
import time

def slot():
    bet_amount = balancee.bet_amount()
    while True:
        if balancee.low_balance(bet_amount) == False and balancee.zero_balance()==False:
                
            wheel1 = utils.assign_number(1,3)
            wheel2 = utils.assign_number(1,3)
            wheel3 = utils.assign_number(1,3)

            multiplier = utils.assign_number(2,12)
            
            utils.line()
            print(f"{wheel1}    {wheel2}    {wheel3}        {multiplier}x")
            utils.line()
            if wheel1 == wheel2 == wheel3:
                utils.print_win(bet_amount=bet_amount,multiplier=multiplier)
            else:
                utils.print_lost(bet_amount=bet_amount)
            time.sleep(.3)
            print("Wanna Replay?? ")
            replay = utils.capture_responce()
            if replay == "y":
                continue
            else:
                return
        else:
            balancee.print_Zero_balance()
            break
        