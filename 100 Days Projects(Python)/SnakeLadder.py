import random

import pygame

# pygame.init()
# X = 700
# Y = 700
#
# screen = pygame.display.set_mode((X, Y))
# pygame.display.set_caption('image')
# imp = pygame.image.load(r'C:\Users\Shree\Documents\Python\SNL.png').convert()
#
# screen.blit(imp, (0, 0))
# pygame.display.flip()
# status = True
#
# while status:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             status = False
#
# pygame.quit()


def Rules():
    print(" --- Welcome To Snakes And Ladder ---  "'\n''\n'
          "Rules :"'\n'
          "     1. Max players allowed are 4"'\n'
          "     2. All players start from block 0"'\n'
          "     3. If you land on ladder you'll advance higher "'\n'
          "     4. If you land on snake you'll be swallowed down  "'\n'
          "     5. If you roll a six you get 'BONUS' roll!" '\n'
          "     6. If you roll a six on bonus you won't get roll again" '\n'
          "     7. First to reach 100 'WINS'!! "'\n''\n')


Rules()


def start():
    snakes = [28, 37, 47, 75, 96]
    ladders = [14, 12, 22, 41, 54]
    print("You'll find "'\n'
          f"    >> Ladders on following blocks : {ladders}"'\n'
          f"    >>  Snakes on following blocks : {snakes}"'\n')

    player_count = int(input("Enter Number of Users : "))

    def player_names():
        if player_count > 4:
            print("Max Players Limit : 4")
            start()

    player_names()

    player = []
    for i in range(player_count):
        name = input(f"Enter User Name : ")
        player.append(name)

    score = []
    for i in player:
        initial_score = 0
        score.append(initial_score)

    def player_scores():
        for i in range(player_count):
            print(F'[{player[i]} : {score[i]}]', end="  ")
        print("\n")

    print('\n'"----- Initial Scores ------")
    player_scores()

    print('\n'"----- START GAME ------")

    def GameOn():
        round = 0
        while 100 not in score:
            for move in range(player_count):
                n = 0
                n = move
                user_input = input(f"{player[n]} Press Enter to roll dice :")
                if user_input == "":
                    roll = random.randint(1, 6)
                    print(f"{player[n]} you rolled : {roll}""\n")
                    score[n] = score[n] + roll

                    if roll == 6:
                        print(f"YAY!! {player[n]} rolled a 6 Roll Again !!")
                        user_input2 = (input(f"{player[n]} Press Enter to roll dice :"))
                        if user_input2 == "":
                            roll2 = random.randint(1, 6)
                            print(f"{player[n]} you rolled : {roll2}"'\n')
                            score[n] = score[n] + roll2

                if score[n] in ladders:
                    print('\n'f"{player[n]} you found a LADDER! ")
                    if score[n] == 12:
                        print(f"{player[n]} You climb up to 50")
                        score[n] = 50
                    elif score[n] == 14:
                        print(f"{player[n]} You climb up to 55")
                        score[n] = 55
                    elif score[n] == 22:
                        print(f"{player[n]} You climb up to 58")
                        score[n] = 58
                    elif score[n] == 41:
                        print(f"{player[n]} You climb up to 79")
                        score[n] = 79
                    elif score[n] == 54:
                        print(f"{player[n]} You climb up to 88")
                        score[n] = 88

                if score[n] in snakes:
                    print('\n'f"OOPS A snake found you !!")
                    if score[n] == 28:
                        print(f"{player[n]} You drop down to 10")
                        score[n] = 10
                    elif score[n] == 37:
                        print(f"{player[n]} You drop down to 3")
                        score[n] = 3
                    elif score[n] == 47:
                        print(f"{player[n]} You drop down to 16")
                        score[n] = 16
                    elif score[n] == 75:
                        print(f"{player[n]} You drop down to 32")
                        score[n] = 32
                    elif score[n] == 96:
                        print(f"{player[n]} You drop down to 42")
                        score[n] = 42

            round += 1
            print(f"Score is ", end="")
            player_scores()
            print(f'------ROUND{round}------''\n')
        else:
            print("Good Game!")

    GameOn()


start()