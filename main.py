import random
WORDLIST = ['rock','fish','lime','this','that','live','flew','jump']
wordToGuess = 'rock'
guesses = 10

def checkWord(word):
    guessedletters = word
    wordletters = wordToGuess
    res = [0,0]
    for i in range(0,4):
        if (guessedletters[i] == wordletters[i]):
            res[0] += 1       
        elif(guessedletters[i] in wordletters):
            res[1] += 1
    return res

while (guesses > 0):
    guess = input(">>>")
    print(f"{guess}\t{checkWord(guess)}")
