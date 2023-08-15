import random

def give_instructions():
    print('''\n Wordle is a single player game. 
          A player has to guess a 5 letter word.
          You have six attempts.d
          Your progress guide "✔xx✔+"
          "✔" = letter at that position was guessed correctly
          "✗" = Letter is in the word but in another position
          "_" = Letter is not in the word. 
    ''')

def check_word(hidden_word, guess):
    if hidden_word == guess:
        print("You've WON 🎉 🎊 🥳\nYou guessed the word correctly!\n") 
        return True
    else:
        result = ''
        for i, j in zip(guess, hidden_word):
            if i == j:
                result += f'✔'
            elif i in hidden_word:
                result += f'✗'
            else:
                result += f'_'
        print(result)
        return False
        
def game():
    words = ['about', 'alert', 'argue', 
             'beach', 'brain', 'carry', 'claim', 'cream',
             'brand', 'class', 'dance', 'dated', 'dealt',
             'debut', 'entry', 'risky', 'worth', 'stuff']
                     
    hidden_word = random.choice(words)
    attempt = 6

    give_instructions()
    
    while attempt > 0:
        guess = input("\nGuess the word: ").lower()
        if check_word(hidden_word, guess):
            break
        else:
            attempt -= 1
            print(f'You have {attempt} attempts left.')
    else:
        print(f'\nSorry, you lost!\nThe word was {hidden_word}')

game()
