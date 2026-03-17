from os import system, name as os_name
def clear():
    if os_name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')
def highest_bidder(bid_dict):
    winner = max(bid_dict, key=bid_dict.get)
    highest_bid = bid_dict[winner]
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

