import random

values = {"Ace": 11, "King": 10, "Queen": 10, "Jack": 10}
player_hand_value = 0; dealer_hand_value = 0
player_hand = []; dealer_hand = []; fulldeck = []
    
for i in range(0,4):
    for i in range(1, 10):
        if i == 1:
            fulldeck.append(f"Ace")
            fulldeck.append(f"Jack") 
            fulldeck.append(f"King") 
            fulldeck.append(f"Queen")   
        else:
            fulldeck.append(f"{i}")

for _ in range(2): 
    card = random.choice(fulldeck)
    player_hand.append(card)
    fulldeck.remove(card)

print(player_hand)
card = random.choice(fulldeck)
dealer_hand.append(card)
fulldeck.remove(card)
print(dealer_hand)

while True:
    player_input = input("Hit or stand? ").strip().lower()
    if player_input == "hit":
        card = random.choice(fulldeck)
        player_hand.append(card)
        fulldeck.remove(card)
        print(f"You drew: {card}")
        break
    elif player_input == "stand":
        print("You chose to stand.")
        break 
    else:
        print("Invalid input! Please type 'hit' or 'stand'.")

for i in dealer_hand:
    if i in values:
        dealer_hand_value += values[i]
    else:
        dealer_hand_value += int(i)

while dealer_hand_value < 17:
    drawn_card = random.choice(fulldeck)  
    dealer_hand.append(drawn_card) 
    fulldeck.remove(drawn_card)

    if drawn_card in values:
        dealer_hand_value += values[drawn_card]
    else:
        dealer_hand_value += int(drawn_card)

for i in player_hand:
    if i in values:
        player_hand_value += values[i]
    else:
        player_hand_value += int(i)
    if "Ace" in player_hand and player_hand_value > 21:
        player_hand_value -= 10


print(dealer_hand)
print(player_hand_value)
print(dealer_hand_value)

if player_hand_value > 21:
    print("You broke!")
elif player_hand_value > dealer_hand_value or dealer_hand_value >= 22 and player_hand_value <= 21:
    if player_hand_value == 21 and dealer_hand_value != 21:
        print("You won by blackjack!")
    else:
        print("You won!")
elif player_hand_value == dealer_hand_value:
    print("Its a tie!")
else:
    print("You lost!")
