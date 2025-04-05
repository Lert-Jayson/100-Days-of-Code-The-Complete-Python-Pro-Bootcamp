import random 

words = ["TOMATO", "PUPPY", "DEATH", "SURVEY", "POWER", "ANIME"]

life_5 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
life_4 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
life_3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
life_2 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
life_1 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
life_0 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

title = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    __/ |                       
                   |___/
'''

print(title)

random_word = random.choice(words)
life = 6
guessed_letters = []  # Track guessed letters

def checkword():
    word_blanks = ""
    for letter in random_word:
        if letter in guessed_letters:
            word_blanks += letter
        else:
            word_blanks += "_"
    return word_blanks

def checklife(life):
    if life == 5 or life == 6:
        print(life_5)
    elif life == 4:
        print(life_4)
    elif life == 3:
        print(life_3)
    elif life == 2:
        print(life_2)
    elif life == 1:
        print(life_1)
    elif life == 0:
        print(life_0)

# Game loop
while life > 0:
    print(f"Word to Guess: {checkword()}")
    guess_letter = input("Guess a letter: ").upper()

    if guess_letter not in guessed_letters:
        guessed_letters.append(guess_letter)
        if guess_letter not in random_word:
            life -= 1
            print(f" Incorrect guess! You lose 1 life.")
    else:
        print(f"You already guessed '{guess_letter}'.")

    checklife(life)  # Show hangman
    print(f"*********** {life}/6 ***************")
    
    if "_" not in checkword():
        print("\n YOU WIN! The word was:", random_word)
        break
else:
    print("\n GAME OVER! The word was:", random_word)
