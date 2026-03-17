from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')
def highest_bidder(bid_dict):
    highest_bid = float('-inf')
    winner = ""
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
bidding = {}
next_person = True
while next_person:
    name = input("What is your name? ").strip()
    bid = int(input("What is your bid? $"))
    bidding[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").strip().lower()
    clear()
    if should_continue == "no":
        next_person = False
highest_bidder(bidding)
