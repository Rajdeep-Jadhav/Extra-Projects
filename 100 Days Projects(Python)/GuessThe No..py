import random

logo = """
 
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ 
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
        
"""
print(logo)

start = input("Chose difficulty \n"
              "Easy[E] or Hard[H] : ")

int_list = list(range(1, 101))
random_integer = random.choice(int_list)


def gaming():
    def game():
        End = False
        guess = int(input('Guess The Number : '))
        if guess == random_integer:
            print('Great! You got the number')
        elif guess > random_integer:
            print('Too High')
        elif guess < random_integer:
            print('Too low')

        if guess == random_integer:
            End = True

        while End is False:
            game()
    game()



if start == 'E' or start == 'e':
    print('YOU GET 10 CHANCES')
    for i in range(10):
        print(f'Guess Number : {i}')
        gaming()
elif start == 'H' or start == 'h':
    print('YOU GET 5 CHANCES')
    for i in range(5):
        print(f'Guess Number : {i}')
        gaming()
else:
    print('Enter Valid Input')
