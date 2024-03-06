# BlackJack

import random
from typing import Any

logo = """"


.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
      
      
"""


print(logo)

def deal_cards():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
comp_cards = []

is_game_over = False

for i in range(2):
    new1 = deal_cards()
    user_cards.append(new1)

for j in range(2):
    new2 = deal_cards()
    comp_cards.append(new2)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.appens(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return('DRAW ')
    elif comp_score == 0:
        return('LOST to a BLACKJACK ')
    elif user_score == 0 :
        return('WON by a BLACKJACK ('u') ')
    elif user_score > 21:
        return('OVER LIMIT LOST ')
    elif comp_score > 21:
        return('COMPUTER SCORE OVER LIMIT\n'
              'YOU WON ('u')')
    elif user_score > comp_score:
        return 'YOU WIN ('u')'
    else:
        return 'YOU LOST '

while not is_game_over:
    user_score: int | Any = calc_score(user_cards)
    comp_score = calc_score(comp_cards)

    print(f'\n \n'        
          f'USER STATS (0_0) : \n'
          f'                User card 1 : {user_cards[0]}\n'
          f'                User card 2 : {user_cards[1]}\n'
          f'                User Total Score : {user_score}\n'
          f'COMP STATS(>_<):\n'
          f'                Comp cards1 : {comp_cards[0]}'
          )

    if user_score == 0 or comp_score == 0 or user_score > 21:
        is_game_over = True
    else :
        user_input = input('\n -- Your Move -- \n'
                           'Enter Y to continue : \n'
                           'Enter N to pass     : ')
        if user_input == 'y':
             user_cards.append(deal_cards())
        else:
            is_game_over = True

user_final = sum(user_cards)
comp_final = sum(comp_cards)

while is_game_over == True:
    print(f'\n\n'
          f'your final sum : {user_final}\n'
          f"comp final sum : {comp_final}\n\n"
          f'compare(user_final, comp_final)\n')
    break