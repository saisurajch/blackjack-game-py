import random

#created a function for generating random cards
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)

#created a function that takes list of cards as input and returns the sum as score
def calculate_score(cards):
    """Takes list of cards as inputs and returns the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#created a compare function which compares the scores of user and computer
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose...! Opponent has a blackjack"
    elif user_score == 0:
        return "You Win with a blackjack"
    elif user_score > 21:
        return "You went over...! You Lose"
    elif computer_score > 21:
        return "Opponent went over...! You Win"
    elif user_score > computer_score:
        return "You win...!"
    else:
        return "You Lose"
playgame = True
def game():
    #declaring an empty list for both user and computer to hold cards
    user_cards = []
    computer_cards = []
    is_game_over = False
    #appending 2 default cards for both user and computer as a start
    for i in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append((deal_card()))

    #calling the calculate_score function by passing user_cards and computer_cards as list inputs
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    #creating a while loop for user choices
    while is_game_over == False:
        #displaying the cards and score at start
        print(f"Your cards : {user_cards}, present score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        #making conditions for deciding win or lose
        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            user_choice = input("Do you want to draw another card...! Type 'y' for yes and 'n' for pass :")
            if(user_choice == 'y'):
                user_cards.append(deal_card())
                user_score = sum(user_cards)
            else:
                is_game_over = True

    #creating a while loop for computer choices
    while computer_score != 0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    #last part
    print(f"Your Final hand:: Cards: {user_cards} Final Score: {user_score}")
    print(f"Computer's Final hand:: Cards: {computer_cards} Final Score: {computer_score}")
    print(compare(user_score, computer_score))
    play_game = input("Do you want to play the game again? Type 'y' for yes and other char for exit :")
    if play_game == 'y':
        game()
    else:
        print("Game End")
game()
