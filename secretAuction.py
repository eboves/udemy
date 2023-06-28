import art_secret_auction

from art_secret_auction import logo
#print(art_secret_auction.logo)
print(logo)
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

##### A DIFFERENT WAY TO DO IT ########
# def find_highest_bidder(bids):
#     highest_bid = 0
#     winner = ""
#     for bidder in bids:
#         bid_amount = bids[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder

#     print(f"The highest bidder is {winner} with a bid of ${highest_bid}")  

# bids = {}

# bidding_finished = False
# while not bidding_finished:
#     name = input("Please Enter you Name: ").title()
#     bid = int(input("Please Enter you Bid $"))

#     bids[name] = bid
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("Screen clean")

















