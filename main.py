import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(value, suit) for value in values for suit in suits]

random.shuffle(deck)

def deal_card():
    return deck.pop()

def card_value(card):
    value, suit = card
    if value in ['J', 'Q', 'K']:
        return 10
    elif value == 'A':
        return 11
    else:
        return int(value)
    

def hand_value(hand):
    hand_total = 0
    number_of_aces = 0

    for card in hand:
        hand_total += card_value(card)
        if card[0] == 'A':
            number_of_aces += 1

    while hand_total > 21 and number_of_aces:
        hand_total -= 10
        number_of_aces -= 1

    return hand_total

def display_hand(player, hand):
    print(f"{player}'s hand: {' '.join([f'{value}{suit}' for value, suit in hand])}")

def player_turn(player_hand):
    while True:
        display_hand('Player', player_hand)
        print(f"Player's hand value: {hand_value(player_hand)}")
        if hand_value(player_hand) > 21:
            print("Player busts!")
            return False
        elif hand_value(player_hand) == 21:
            print("Player wins!")
            return True
        else:
            action = input("Do you want to hit or stand? ")
            if action == 'hit':
                player_hand.append(deal_card())
            else:
                return False
            
def dealer_turn(dealer_hand):
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    display_hand('Dealer', dealer_hand)
    print(f"Dealer's hand value: {hand_value(dealer_hand)}")
    if hand_value(dealer_hand) > 21:
        print("Dealer busts!")
        return True
    elif hand_value(dealer_hand) == 21:
        print("Dealer wins!")
        return False
    return False

def determine_winner(player_hand, dealer_hand):
    player_hand_value = hand_value(player_hand)
    dealer_hand_value = hand_value(dealer_hand)

    if player_hand_value > dealer_hand_value:
        print("Player wins!")
    elif player_hand_value < dealer_hand_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

def blackjack():
    global deck
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck) 
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    if player_turn(player_hand):
        dealer_turn(dealer_hand)

    # determine_winner(player_hand, dealer_hand)


blackjack()