import random
from replit import clear
from art import logo

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    choose_card=random.choice(cards)
    return choose_card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare (user_score,computer_score):
    if user_score>21 and computer_score>21:
        return " You Over You loose"
    
    if user_score == computer_score:
        return "Draw"
    elif user_score >21:
        return "You might over, You Loose"
    elif computer_score>21:
        return "You Win"    
    elif user_score ==0:
        return "You Win"
    elif computer_score ==0:
        return "You Lose"
    elif user_score>computer_score:
        return "You Win"
    else:
        return "You Loose"
     
def play():
    print(logo)
    user_cards=[]
    computer_cards=[]
    is_game=True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards {user_cards}, your current score {user_score} \n computer card {computer_cards[0]}")
        if user_cards == 0 or computer_score ==0 or user_score >21:
            is_game=False
        
        else:
            User_choice=input("Type 'Y' to get another card Or 'N' to pass :  ").lower()
            if User_choice=="y":
                user_cards.append(deal_card())
            else:
                is_game=False
    while computer_score!=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"Your cards {user_cards}, your final score {user_score} \n computer card {computer_cards} computer score {computer_score}")
    print(compare(user_score,computer_score))
while input("Do you Want to play a game of Blackjack? Type 'Y' or 'N' : ").lower()=="y":
    clear()
    play()

        