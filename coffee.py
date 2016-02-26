from __future__ import division
import math


POT_SIZE = 12           # Number of cups in the pot
CUPS_PER_DRINKER = 2    # ~number of pot-cups that go into 1 mug
SCOOPS_PER_CUP = 0.5    # Assuming use of 2 TBS scoop, per pot-cup
SCOOPS_PER_POT = POT_SIZE * SCOOPS_PER_CUP


print('--------------------------------------------------------------------------------------')
print("                                IT'S COFFEE TIME                                      ")
print('--------------------------------------------------------------------------------------')

response = raw_input(">>>> Hello! I'm coffee-bot, would you like to make some coffee? (y/n) ")

if response in ('Yes', 'Y', 'yes', 'y', 'please'):
    print(">>>> Very well, lets make it happen")
    print(">>>>")

    # PT = pot_type
    PT = raw_input(">>>> Are you using a drip coffee maker (D/d) or a French Press (F/f)? ")

    if PT in ('D', 'd', 'drip'):
        print("Brewing shall commence at once!")
        print

    # 12 CUP DRIP COFFEE CALCULATIONS

        drinkers = raw_input(">>>> How many people would like coffee? ")
        try:
            drinkers = int(drinkers)
        except ValueError:
            print("PLEASE ENTER NUMERIC VALUES ONLY. I'M NOT ADVANCED ENOUGH FOR WORDS HERE.")
            exit(1)

        cups = 2 * drinkers
        scoops = cups / 2
        pots = (cups / POT_SIZE)
        full_pots = math.floor(pots)
        partial_pots = pots - full_pots
        # print("pots: {}".format(pots))
        # print("full pots: {}".format(full_pots))
        # print("partial pots: {}".format(partial_pots))

        if drinkers >= 7:
            print(">>>>>> This is going to be a multi-pot affair...")
            print(">>> You will need {} full pots and {} partial pots".format(full_pots, math.ceil(partial_pots)))
            print(">>> Use 6 scoops of grounds for each full pot ({} scoops total)".format(6 * full_pots))

            if partial_pots > 0:
                print(">>> The partial pot will need {} cups of water".format((12 * partial_pots)))
                print(">>> You will need to use {} scoops of grounds for the partial pot".format(((12 * partial_pots)/2)))
            else:
                pass

        elif drinkers == 6:
            print
            print(">>>> Go ahead and brew a whole pot")
            print(">>>> For a full pot, use 6 scoops")

        elif drinkers < 6:
            print
            print(">>>> I'll need to do some math...")
            print("...")
            print("......")
            print("............")
            print(">>>> For {} people I recommend a pot brewing size of {} cups".format(drinkers, cups))
            print(">>>> For a {} cup pot, I recommend using {} scoops of grounds".format(cups, scoops))
        else:
            raise RuntimeError("Uh oh - negative drinkers?!")

        print
        print("** Remember, use cold water for better brewing **")
        print

    # FRENCH PRESS COFFEE CALCULATIONS
    else:
        print("I AM NOT YET CONFIGURED FOR SUCH CALCULATIONS.")

elif response in ('No', 'no', 'n'):
    print(response)
    print(">>> Perhaps you'd like some tea then?")

else:
    raise RuntimeError("INVALID RESPONSE, I'M A COMPUTER NOT A LINGUIST")


# CT 2/25/2016
