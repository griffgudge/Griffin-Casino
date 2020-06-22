import random
import time
from cards import *
from games_games import *
from card_engine import CardEngine

with open("balance.txt", "r") as balance:
    money = int(balance.read())

print("""
  ______     ___           _______. __  .__   __.   ______
 /      |   /   \         /       ||  | |  \ |  |  /  __  ™
|  ,----'  /  ^  \       |   (----`|  | |   \|  | |  |  |  |
|  |      /  /_\  \       \   \    |  | |  . `  | |  |  |  |
|  `----./  _____  \  .----)   |   |  | |  |\   | |  `--'  |
 \______/__/     \__\ |_______/    |__| |__| \__|  \______/

""")
selection = input("Hello, Welcome to GriffCasino! Your starting balance is {} GriffCoins™! \nPlease Select the Game you would like to play! \n1)Coin Flip \n2)Roulette \n3)Black Jack \nPlease enter your choice via it's corresponding number! \n".format(money))

checker = True

while checker:
    try:
        if int(selection) > 0 and int(selection) < 4:
            checker = False
        else:
            selection = input("Please use number within the range! \n")
    except:
        selection = input("Invalid input! Please try again! \n")

if selection == "1":
    print("Coin Flip selected! Please input the amount you would like to bet!")
    amount = input("\n")
    checker = True
    while checker:
        try:
            if int(amount) > 0 and int(amount) <= money:
                print("You bet " + amount)
                checker = False
            else:
                amount = input("Invalid amount bet! Your current balance is {} GriffCoins™. Please try again! \n".format(money))
        except:
            amount = input("Invalid input! Please try again! \n")
    print("Please choose whether you think the coin will land on heads or tails \n")
    checker = True
    while checker:
        selection = (input("Heads or Tails? \n")).title()
        if selection == "Heads" or selection == "Tails":
            print("You selected {}!".format(selection))
            checker = False
        else:
            print("You selected neither heads nor tails! Please try again!")
    print("Flipping coin...")
    time.sleep(1)
    side = coin()
    print("{}!".format(side))
    if side == selection:
        money += int(amount)
        with open("balance.txt", "w") as balance:
            balance.write(str(money))
        print("You win! Your new balance is: {} GriffCoins™".format(money))
    else:
        money += -int(amount)
        with open("balance.txt", "w") as balance:
            balance.write(str(money))
        print("You lost! Your new balance is: {} GriffCoins™".format(money))

if selection == "2":
    print("You selected Roulette! Please input the amount you would like to bet!")
    amount = input("")
    checker = True
    while checker:
        try:
            if int(amount) > 0 and int(amount) <= money:
                print("You bet " + amount)
                checker = False
            else:
                amount = input("Invalid amount bet! Your current balance is {} GriffCoins™. Please try again! \n".format(money))
        except:
            amount = input("Invalid input! Please try again! \n")
    bet = (input("\nPlease select if you would like to bet where the wheel will land on!\nNUMBER / COLOUR / PARITY \n")).title()
    checker = True
    while checker:
        if bet == "Number" or  bet == "Colour" or bet == "Parity":
            print("You chose to bet on {}!".format(bet))
            checker = False
        else:
            bet = (input("Please try again! \n")).title()
    if bet == "Number":
        index = 0
        print("Please select a number within the range 0 up to and including 36!")
        bet = input()
        checker = True
        while checker:
            try:
                if int(bet) >= 0 and int(bet) <= 36:
                    print("The number you selected is {}!".format(bet))
                    checker = False
                else:
                    number = input("The number you selected does not fall within the specified range!")
            except:
                number = input("Invalid input!")
    if bet == "Colour":
        index = 2
        print("Please select a colour you would like to bet on! (Red or Black)")
        bet = (input()).title()
        checker = True
        while checker:
            if bet == "Black" or bet == "Red":
                print("The colour you selected is {}!".format(bet))
                checker = False
            else:
                bet = (input("Invalid input please try again!\n")).title()
    if bet == "Parity":
        index = 1
        print("Please input whether you think the number will be even or odd!")
        bet = (input()).title()
        checker = True
        while checker:
            if bet == "Odd" or bet == "Even":
                print("The parity you selected is {}!".format(bet))
                checker = False
            else:
                bet = (input("Invalid input! Please try again!\n")).title()
    print("Rolling the wheel...")
    landed = roulette()
    time.sleep(2)
    if bet == landed[index]:
        if index > 0:
            amount_won = int(amount)
            money += amount_won
        else:
            amount_won = 35 * amount
            money += amount_won
        with open("balance.txt", "w") as balance:
            balance.write(str(money))
        print("You won {}! The ball landed on {}! Which is {} and {}!".format(amount_won, landed[0], landed[1], landed[2]))

    else:
        amount_won = int(amount)
        money += -amount_won
        with open("balance.txt", "w") as balance:
            balance.write(str(money))
        print("You lost {}! The ball landed on {}! Which is {} and {}!".format(amount_won, landed[0], landed[1], landed[2]))

if selection == "3":
    print("Black Jack selected! selected! Please input the amount you would like to bet!")
    amount = input("\n")
    checker = True
    while checker:
        try:
            if int(amount) > 0 and int(amount) <= money:
                print("You bet " + amount)
                checker = False
            else:
                amount = input("Invalid amount bet! Your current balance is {} GriffCoins™. Please try again! \n".format(money))
        except:
            amount = input("Invalid input! Please try again! \n")
    print("Drawing dealer cards...")
    time.sleep(1)
    deck = CardEngine(False)
    dealer_hand = [deck.card_picker() for i in range(2)]
    print(special_cards.get(1))
    print(deck.graphic(dealer_hand[1]))
    print("Drawing player cards...")
    time.sleep(1)
    player_hand = [deck.card_picker() for i in range(2)]
    print(deck.graphic(player_hand[0]))
    print(deck.graphic(player_hand[1]))
    print("You drew a {} of {} and a {} of {}!".format(deck.card_reader(player_hand[0])[1], deck.card_reader(player_hand[0])[2], deck.card_reader(player_hand[1])[1], deck.card_reader(player_hand[1])[2]))
    print("Dealer drew a {} of {} atleast...".format(deck.card_reader(dealer_hand[1])[1], (deck.card_reader(dealer_hand[1])[2])))
    print("\n")
    player_value = hand_value_calc(player_hand)
    print("Player hand is worth {}!".format(player_value))
    dealer_value = hand_value_calc(dealer_hand)
    print("\n")
    if player_hand == 21 and dealer_hand == player_hand:
        print("Split!")
    elif player_hand == 21:
        print("Player wins!")
        win(amount)
    elif dealer_hand == 21:
        print("Dealer wins!")
        lose(amount)
    else:
        checker = True
        while checker:
            print("What would you like to do next?\nSTAND / HIT")
            move = input("\n").lower()
            if move != "stand" and move != "hit":
                print("\nInvalid input! Please try again! \n")
            else:
                checker = False
        if move == "stand":
            print("Dealer's current hand:")
            for i in dealer_hand:
                print(deck.graphic(i))
            print("Dealer has a {} of {} and a {} of {}...\n".format(deck.card_reader(dealer_hand[0])[1], (deck.card_reader(dealer_hand[0])[2]), deck.card_reader(dealer_hand[1])[1], (deck.card_reader(dealer_hand[1])[2])))
            time.sleep(1)
            if dealer_value < player_value:
                print("Drawing more cards for the dealer...")
                while dealer_value < player_value:
                    index = len(dealer_hand)
                    dealer_hand.append(deck.card_picker())
                    print(deck.graphic(dealer_hand[index]))
                    dealer_value = hand_value_calc(dealer_hand)
                    print("Dealer's hand is now worth {}...".format(dealer_value))
                if dealer_value > 21:
                    print("Dealer has gone bust! Player wins!")
                    win(amount)
                elif dealer_value > player_value:
                    print("Dealer wins with a hand worth {} versus your hand which was only worth {}...".format(dealer_value, player_value))
                    lose(amount)
            elif dealer_value > player_value:
                print("Dealer wins with a hand worth {} versus your hand which was only worth {}...".format(dealer_value, player_value))
                lose(amount)
        if move == "hit":
            hit = True
            while hit:
                print("\nDrawing a card...")
                index = len(player_hand)
                player_hand.append(deck.card_picker())
                print(deck.graphic(player_hand[index]))
                player_value = hand_value_calc(player_hand)
                if player_value > 21:
                    print("You have gone bust! You lose!")
                    lose(amount)
                    hit = False
                else:
                    print("Your hand is now worth {}!\n".format(player_value))
                    checker = True
                    while checker:
                        move = (input("Hit again?\nYES / NO\n")).lower()
                        if move != "yes" and move != "no":
                            print("Invalid input please try again!")
                        else:
                            checker = False
                            if move == "yes":
                                print("Hitting again...\n")
                            else:
                                hit = False
            if move == "no":
                print("\nRevealing Dealer's hand...")
                for i in dealer_hand:
                    print(deck.graphic(i))
                print("Dealer has a {} of {} and a {} of {}...\n".format(deck.card_reader(dealer_hand[0])[1], (deck.card_reader(dealer_hand[0])[2]), deck.card_reader(dealer_hand[1])[1], (deck.card_reader(dealer_hand[1])[2])))
                print("Dealer's hand is worth {}!".format(dealer_value))
                if dealer_value > player_value:
                    print("Dealer wins!")
                    lose(amount)
                if dealer_value == player_value:
                    print("Split...")
                else:
                    if dealer_value < player_value:
                        print("Drawing more cards for the dealer...")
                        while dealer_value < player_value:
                            index = len(dealer_hand)
                            dealer_hand.append(deck.card_picker())
                            print(deck.graphic(dealer_hand[index]))
                            dealer_value = hand_value_calc(dealer_hand)
                            print("Dealer's hand is now worth {}...".format(dealer_value))
                        if dealer_value > 21:
                            print("Dealer has gone bust! Player wins!")
                            win(amount)
                        elif dealer_value > player_value:
                            print("Dealer wins with a hand worth {} versus your hand which was only worth {}...".format(dealer_value, player_value))
                            lose(amount)
                    elif dealer_value > player_value:
                        print("Dealer wins with a hand worth {} versus your hand which was only worth {}...".format(dealer_value, player_value))
                        lose(amount)
