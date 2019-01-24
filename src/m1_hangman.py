"""
Hangman.

Authors: Jacob Tebbe and Brandon Wohlfarth.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random


def main():
    play_game(5)


def pick_a_word(length):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        word_choices = string.split()
    while True:
        word = word_choices[random.randrange(0, len(word_choices))]
        if len(word) >= length:
            break
    return word


def print_dashes(word):
    dashes = ''
    for k in range(len(word)):
        dashes += '_ '
    print(dashes)
    return dashes


def check_guess(guess, word, printy_boi):
    new_word = ''
    for k in range(0, len(word) * 2, 2):
        if guess == word[k // 2]:
            new_word += guess
            new_word += ' '
        else:
            new_word += printy_boi[k]
            new_word += ' '
    printy_boi = new_word
    print(printy_boi)
    return printy_boi


def check_win(printy_boi):
    for k in range(0, len(printy_boi), 2):
        if printy_boi[k] == '_':
            return False
    return True


def decrease_guesses(guess, current, previous, number_of_guesses):
    if previous == current:
        number_of_guesses -= 1
        print(guess, 'is wrong')
    return number_of_guesses


def play_game(number_guesses):
    while True:
        word = intro()
        printy_boi = print_dashes(word)
        while True:
            print(number_guesses)
            previous = printy_boi
            print()
            guess = input({'Make a guess'})
            printy_boi = check_guess(guess, word, printy_boi)
            number_guesses = decrease_guesses(guess, printy_boi, previous, number_guesses)
            if number_guesses == 0:
                lose(word)
                break
            if check_win(printy_boi) == True:
                win(word)
                break
        if input({'Do you want to play again? (yes/no)'}) == 'no':
            break


def intro():
    word_length = int(input({'What length of word do you want?'}))
    return pick_a_word(word_length)


def lose(word):
    print()
    print(word)
    print('You Lose!!')
    print()


def win(word):
    print()
    print(word)
    print('You Win')
    print()


main()
