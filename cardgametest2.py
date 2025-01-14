import random

values = {"Ace": 11, "King": 10, "Queen": 10, "Jack": 10}
player_hand_value = 0; dealer_hand_value = 0
player_hand = []; dealer_hand = []; fulldeck = []
    
for i in range(0,4):
    for i in range(1, 10):
        if i == 1:
            fulldeck.append(f"Ace") 
        else:
            fulldeck.append(f"{i}")
            fulldeck.append(f"Jack") 
            fulldeck.append(f"King") 
            fulldeck.append(f"Queen")  

random.shuffle(fulldeck); player_hand.append(random.choice(fulldeck)); player_hand.append(random.choice(fulldeck))

print(player_hand); dealer_hand.append(random.choice(fulldeck)); print(dealer_hand)

player_input = input("hit or stand?"); dealer_hand.append(random.choice(fulldeck)) 

if player_input.lower == "hit":
    player_hand.append(random.choice(fulldeck))

for i in player_hand:
    if i in values:
        player_hand_value += values[i]
    else:
        player_hand_value += int(i)

for i in dealer_hand:
    if i in values:
        dealer_hand_value += values[i]
    else:
        dealer_hand_value += int(i)

print(player_hand_value)

if player_hand_value > 21:
    print("You broke!")

if player_hand_value > dealer_hand_value:
    if player_hand_value == 21:
        print("You won by blackjack!")
    else:
        print("You won!")
elif player_hand_value == dealer_hand_value:
    print("Its a tie!")
else:
    print("You lost!")