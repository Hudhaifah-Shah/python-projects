import random
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_cards(cards, no_of_cards):
    for _ in range(no_of_cards):
        card = random.choice(deck)
        cards.append(card)
    score = calc_score(cards)
    while 11 in cards and score > 21:
        i = cards.index(11)
        cards[i] = 1
        score = calc_score(cards)
    return score
def calc_score(cards):
    score = sum(cards)
    return score
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip()
while play == "y":
    clear()
    my_cards = []
    dealer = []
    my_score = deal_cards(my_cards, 2)
    dealers_score = 0
    while dealers_score < 17:
        dealers_score = deal_cards(dealer, 1)
    print(f"Your cards: {my_cards}, current score: {my_score}")
    print(f"Dealer's first card: {dealer[0]}")
    hit_or_pass = "y"
    while hit_or_pass == "y" and my_score < 21:
        hit_or_pass = input("Type 'y' to get a new card, type 'n' to pass: ").strip()
        if hit_or_pass == "y":
            my_score = deal_cards(my_cards, 1)
            print(f"Your cards: {my_cards}, current score: {my_score}")
            print(f"Dealer's first card: {dealer[0]}")
    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealers_score}")
    my_blackjack = my_cards[0] + my_cards[1]
    dealer_blackjack = dealer[0] + dealer[1]
    if my_blackjack == 21 and dealer_blackjack == 21:
        print("Push")
    elif my_blackjack == 21 and dealer_blackjack != 21:
        print("Blackjack! You win")
    elif my_blackjack != 21 and dealer_blackjack == 21:
        print("Blackjack! Dealer wins")
    elif my_score > 21:
        print("You went over. You lose")
    elif dealers_score > 21:
        print("Dealer went over. You win")
    elif my_score == dealers_score:
        print("Push")
    elif my_score > dealers_score:
        print("You win")
    else:
        print("You lose")
    play = input("Would you like to play again? Type 'y' or 'n': ").strip()

