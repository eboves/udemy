

bidders = {}
keep_playing = True
# This code add and look for the highest bidder.
def secret_action(name_bidder, bid_amount):
    bidders[name_bidder] = bid_amount
    holder = 0

    for key in bidders:
        if bidders[key] > holder:
            holder = bidders[key]
    print(f"The highest bidder is {name_bidder} with a bid of ${holder}")  

while keep_playing:
    name = input("Please Enter you Name: ").title()
    bid = int(input("Please Enter you Bid $"))
    secret_action(name, bid)
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if another_bidder == 'no':
        keep_playing = False
        secret_action(name, bid)

