from random import choices
main_cards=[11,1,2,3,4,5,6,7,8,9,10,10,10]
computer_cards=[]
user_cards=[]
temp=0
def winner():
    global user_cards
    global computer_cards
    global temp
    if sum(computer_cards)>=21:
        print('computer_wins')
        return ('computer_wins',1)
    elif sum(user_cards)>=21:
        return ('user_wins',1)
    elif sum(computer_cards)>sum(user_cards) and temp==1:
        print('computer_wins')
        return ('computer_wins', 1)
    elif sum(user_cards) > sum(computer_cards) and temp==1:
        print('user_wins')
        return ('user_wins', 1)
    else:
        return ('not_declared_yet',0)

def decision(choice):
    global temp
    if choice == 'y':
        temp = 1
        pick_cards(user_cards, 1)
        pick_cards(computer_cards, 1)
        game()
    elif choice == 'n':
        temp = 1
        pick_cards(computer_cards, 1)
        game()

def pick_cards(cards,ch):
    global main_cards
    for i in choices(main_cards,k=ch):
        if (11 in cards and i==11):
            cards.append(1)
        else:
            cards.append(i)
    return cards

def game():
    global temp
    if 0 in winner():
        print("computer cards are", computer_cards[0])
        print("your cards: ", user_cards, "your score is", sum(user_cards))
        choice=input("Do you want to draw another card...! Type 'y' for yes and 'n' for pass :")
        decision(choice)

computer_cards=pick_cards(computer_cards,2)
user_cards=pick_cards(user_cards,2)
if 0 in winner():
    game()

