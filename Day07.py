import random
stages = [
    r'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''',

    r'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''',

    r'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''',

    r'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''',

    r'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''',

    r'''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''',

    r'''
 +---+
 |   |
     |
     |
     |
     |
=========
'''
]
word_list = ["holmes", "spiderman" , "hulk" , "jerry"]
random_word = random.choice(word_list) 

lives = 6

display = []
word_length = len(random_word)
for _ in range(word_length) :
    display += "_"
print(display)  

game_end = False
while not game_end :
    guess = input("Guess a letter\n")
    lowercase_guess = guess.lower()

    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            game_end = True
            print("You Lose!")
    print(display)

    if "_" not in display:
        game_end = True
        print("You Win!")

    print(stages[lives])    





  