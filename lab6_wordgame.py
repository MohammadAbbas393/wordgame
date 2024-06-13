"""
CSCI 150 Lab 6

Name: Mohammad Abbas, PB
Section: A

Creativity:
1. Added an error checker where the guessed word is checked to make sure its a letter
2. Added the number of the charactars in the word and created an introduction for the game

"""
import random as r
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# ------------------------------------

def play_wordgame(filename, num_tries):
    """
    Play a game where the user tries to guess a randomly selected word from a specific file that should be in the same directory.
    
    Args:
        filename: A file that have the words needed to play the game
        num_tries: The number of tries a user gets to guess the word
    """
    start = input('Do you want to play a game? (yes/no) ')
    if start == 'yes':
        print('\nTry to guess the word!')
        
        word = r.choice(read_words(filename))
        set_to_string(word)
        tries = '*' * num_tries
        guessed_letters = set()
        incorrect_guesses = 0
        underscored_word = "_" * len(word)
        print('This word has', len(word), 'characters\n')
        
        while '_' in underscored_word and incorrect_guesses < num_tries:
            print('Guessed letters: ', set_to_string(guessed_letters))
            print('Incorrect guesses left: ', tries)
            print('Word:', underscored_word)
            
            guessed_letter = input('\n---------------\nGuess a letter: ')
            guessed_letter = guessed_letter.lower()

            while guessed_letter in guessed_letters:
                print("Letter already guessed!")
                guessed_letter = input('\nGuess a different letter: ')

            while len(guessed_letter) != 1:
                print('\nOnly 1 letter is allowed!')
                guessed_letter = input('\nGuess a letter: ')

            while guessed_letter not in ALPHABET:
                print('\nPlease enter a letter')
                guessed_letter = input('\nGuess a letter: ')
                
            if guessed_letter not in word:
                guessed_letters.add(guessed_letter)
                incorrect_guesses += 1
                tries = tries[:-1]
                print('Letter is not in the word.\n')
                    
            else:
                guessed_letters.add(guessed_letter)
                underscored_word = insert_letter(guessed_letter, underscored_word, word)
                print('Good job!\n')
                    
            if incorrect_guesses == num_tries:
                print('\nThe word was:', word, '\nBetter luck next time!')

            if '_' not in underscored_word:
                print('\nYou win! \nThe word was:', word, '\nYou guessed it with', incorrect_guesses,'incorrect guesses')
   
    else:
        print('Thank you! Have a good day.')

# ------------------------------------

def read_words(filename):
    """
    Read file into list of words assuming one word per line.
    Args:
        filename: Path to file
        
    Return:
        List of words
    """
    with open(filename, "r") as file:
        words = []
        
        for line in file:
            words.append(line.strip())    
        
        return words

# ------------------------------------

def set_to_string(word_set):
    """
    Takes a set and transform it into a string, while capitalizing all the letters and adding spaces in between
    
    Args:
        word_set: The selected set to be transformed
    
    Returns:
        A string with all the letters in the set capitalized and seperated by spaces
    """
    x = ''
    
    for item in word_set:
        x = x + str(item) + ' '
        
    final = x[:-1]
    
    return final.upper()

# ------------------------------------

def insert_letter(letter, underscored_word, word):
    """
    Fill in the corresponding letter of a word instead of '_'
    
    Args:
        letter: Guessed letter by user
        underscored_word: The word the user is filling in
        word: The word the user is trying to guess
        
    Returns:
        The underscored word with the guessed letter in its appropriate position
    """
    for i in range(len(word)):
        if word [i] in letter:
            underscored_word = underscored_word [:i] + word [i] + underscored_word [i + 1:]
    return underscored_word

# ------------------------------------

if __name__ == '__main__':
    play_wordgame('cs_words.txt', 7)