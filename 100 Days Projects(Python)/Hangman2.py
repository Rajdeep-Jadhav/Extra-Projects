import random

words = {
    "apple": "a round fruit with red, green, or yellow skin and a white inside that you can eat",
    "chair": "a piece of furniture that you sit on, with a back and sometimes arms",
    "pencil": "a tool that you use for writing or drawing, made of wood and graphite or sometimes plastic and ink",
    "water": "a clear liquid that you drink and use to wash things",
    "phone": "a device that you use to talk to other people who are far away, often with a screen for texting and using apps",
    "table": "a piece of furniture with a flat top and usually four legs, that you use for eating or working",
    "shoe": "a piece of clothing that you wear on your foot to protect it and make it more comfortable when you walk or run",
    "music": "sounds that people make with instruments or their voices that can be pleasant to listen to",
    "cookie": "a sweet baked treat that you can eat, usually made with flour, sugar, and butter",
    "banana": "a long, curved fruit with yellow or green skin and soft, sweet inside",
    "jacket": "a piece of clothing that you wear over your shirt or sweater to keep warm",
    "camera": "a device that takes pictures or records video, often with a lens and screen",
    "basket": "a container made of woven material, often used for carrying or storing things",
    "butter": "a soft, creamy substance made from milk or cream, often used for cooking or spreading on bread",
    "flower": "a colorful plant with a sweet smell, often used for decoration or given as a gift",
    "mirror": "a smooth surface that reflects light, often used for looking at yourself",
    "pizza": "a round or rectangular dish made of dough, sauce, cheese, and toppings, often eaten as a meal",
    "robot": "a machine that can move and do tasks, often controlled by a computer",
    "garden": "a piece of land where people grow plants and flowers for decoration or food",
    "guitar": "a musical instrument with six strings that you play by strumming or picking them with your fingers or a pick",
    "jungle": "a dense forest in a hot, tropical region, often with many different plants and animals",
    "planet": "a large, round object that orbits around a star, like Earth or Jupiter",
    "rocket": "a device that travels through space or the air, often with the help of fuel and engines",
    "basketball": "a game played with a ball and two hoops, where players try to shoot the ball into the other team's hoop",
    "elephant": "a large animal with a long, curved trunk and tusks, often found in Africa and Asia",
    "keyboard": "a device that you use to type on a computer, often with letters and numbers",
    "penguin": "a flightless bird with black and white feathers, often found in Antarctica",
    "rainbow": "a colorful arc of light that appears in the sky after it rains",
    "teddy bear": "a stuffed toy that looks like a bear, often given as a gift or used for comfort",
    "telescope": "a device that helps you see things that are far away, often used for looking at stars",
    "train": "a vehicle with many cars that runs on tracks, often used for transportation",
    "violin": "a musical instrument with four strings that you play with a bow, often used in orchestras",
    "yogurt": "a creamy food made from milk and bacteria, often with fruit or other flavors added",
    "zebra": "an animal with black and white stripes, often found in Africa"

}

# Select a random word from dictionary
word = random.choice(list(words.keys()))
count = len(word)

print('\n''-------HANGMAN GAME-------''\n')

display = []
for letter in word:
    print("_", end=" ")
    display.append('_')

# Display meaning of word for user  to guess
print(':', words[word])
print('               '
      f': Length of word {count}')


def hangman():
    # Initialize number of guess user gets
    lives = 5
    print(f'               '
          f': You have {lives} chances to guess')

    while "_" in display:
        # Ask user to guess letters of word
        user_guess = input('\n''Guess letter of the word : ')

        # Check if user guess is in the word
        for position in range(count):
            letter_ = word[position]
            if letter_ == user_guess:
                display[position] = letter_
                print('\n'f"You have {lives} chances to guess")
        for guess in display:
            print(guess, end=" ")

        # If user guess incorrect reduce one live
        # If user is out of lives end game
        if user_guess not in list(word):
            lives -= 1
            print('\n'f"You have {lives} chances to guess")
            if lives == 0:
                print("You Lose")
                break

    else:
        # When user guess all letters in word correctly
        print('\n''\n'f"Yes the word was : {word}")


hangman()