from art import logo
from replit import clear
import random
print(logo)
def add(n1, n2):
  total = n1+n2 
  return total
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
hand = []
hand_total = {"y": add}
computer_hand = []
def blackjack():
  draw = True
  comp = True
  should_continue = input("Do you want to play blackjack? \"y\" or \"n\". ").lower()
  clear()
  if should_continue == "y":
    computer_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    hand.append(random.choice(cards))
    hand.append(random.choice(cards))
    print(f"You got: {hand} which equals {hand_total[should_continue](hand[0],hand[1])}")
    total = int(hand_total[should_continue](hand[0],hand[1]))
    print(f"Computers first card is: {computer_hand[0]}\n")
    computer_total = int(hand_total[should_continue](computer_hand[0],computer_hand[1]))
    if total == 21:
      print("BLACKJACK!!!! OHHHH YEAAAAHHH YOU WON!")
      comp=False
      draw=False
    if computer_total == 21:
      print("OOHHHH SNAP! COMPUTER GOT A BLACKJACK! YOU LOST!!!!")
      comp=False
      draw=False
    while comp:
      if computer_total < 16:
        computer_hand.append(random.choice(cards))
        new_computer_card = computer_hand[-1]
        if new_computer_card == 11 and computer_total > 21:
          new_computer_card = 1
        computer_total = hand_total["y"](computer_total,new_computer_card)
      if computer_total > 16:
        comp = False
      while draw:
        keep_continuing = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()
        if keep_continuing == "y":
          hand.append(random.choice(cards))
          new_card = hand[-1]
          if new_card == 11 and total > 21:
            new_card = 1
          print(f"You got: {hand} which equals {hand_total[keep_continuing](total,new_card)}")
          total = hand_total[keep_continuing](total,new_card)
          if total > 21:
            print(f"Your total was {total}. The computers total was {computer_total}.")
            print("YOU LOST!!! TAKE THE L!")
            draw = False
        if keep_continuing == "n":
          if computer_total > 21:
            print(f"Your total was {total}. The computers total was {computer_total}.")
            print("YOU WON!")
            draw = False
          if total == computer_total:
            print(f"Your total was {total}. The computers total was {computer_total}.")
            print("DRAW!")
            draw = False
          if total < computer_total and computer_total < 22:
            print(f"Your total was {total}. The computers total was {computer_total}.")
            print("TAKE THE L, LoSeR!!!!")
            draw = False
          if total > computer_total:
            print(f"Your total was {total}. The computers total was {computer_total}.")
            print("CONGRATS ON WINNING!")
            draw = False
        
blackjack()



