import hangman_printer
import random

list_of_words_animals = ["elephant", "tiger", "monkey", "lion",
                         "butterfly", "duck", "horse", "pig", "turtle", "cat", "dog"]
list_of_words_fruits = ["apple", "banana", "grapefruit", "strawberry", "orange", "watermelon",
                        "pineapple", "grapefruit"]


def wrong_answer(chances):
    chances = chances - 1
    return chances


def good_answer(player_input, player_word, word):
    count = 0
    for x in word:
        if x == player_input:
            new_player_word = player_word[:count] + x + player_word[count + 1:]
            player_word = new_player_word
        count += 1
    return player_word


def print_hangman(chances, player_word):
    if chances == 5:
        print(hangman_printer.status1)
        print("Incorrect letter, " + str(chances) + " chances left")
        print(player_word)
    elif chances == 4:
        print(hangman_printer.status2)
        print("Incorrect letter, " + str(chances) + " chances left")
        print(player_word)
    elif chances == 3:
        print(hangman_printer.status3)
        print("Incorrect letter, " + str(chances) + " chances left")
        print(player_word)
    elif chances == 2:
        print(hangman_printer.status4)
        print("Incorrect letter, " + str(chances) + " chances left")
        print(player_word)
    elif chances == 1:
        print(hangman_printer.status5)
        print("Incorrect letter, " + str(chances) + " chance left")
        print(player_word)
    elif chances == 0:
        print(player_word)
        print(hangman_printer.status6)


def game(list_of_words):
    word = random.choice(list_of_words)
    player_word = "*" * len(word)
    chances = 6
    used_letters = []
    print("Your word: " + player_word + " ,you start with 6 chances")
    while chances > 0 and word != player_word:
        player_input = input("Select letter: ").lower()
        if player_input in word and player_input not in used_letters:
            player_word = good_answer(player_input, player_word, word)
            used_letters.append(player_input)
            print(player_word)
        elif player_input not in word and player_input not in used_letters:
            chances = wrong_answer(chances)
            print_hangman(chances, player_word)
            used_letters.append(player_input)
        else:
            print("You have already used these letters, choose another one")
    win_lose(player_word, word)


def start_game():
    while True:
        print("1. Animals")
        print("2. Fruits")
        player_input = input("Choose what kind of word you want to guess: ")
        if player_input == str(1):
            game(list_of_words_animals)
        elif player_input == str(2):
            game(list_of_words_fruits)
        while True:
            player_input = input("Would you like to play again? y/n: ")
            if player_input.lower() == "y":
                start_game()
            elif player_input.lower() == "n":
                break
            else:
                print("You have chosen the wrong option")
        break


def main():
    while True:
        print(hangman_printer.start)
        print("1. Start game")
        print("2. Show guessed words")
        print("3. Quit")
        player_input = input("Choose option: ")
        if player_input == str(1):
            start_game()
        elif player_input == str(2):
            text_file = open("guessed_words.txt", "r")
            text_file = text_file.read()
            print(text_file)
            input("Press enter to exit")
        elif player_input == str(3):
            print("Goodbye")
            break
        else:
            print("You have chosen the wrong option")


def win_lose(player_word, word):
    if player_word == word:
        print("Congratulations, the correct word is " + player_word + ". Discovered word has been saved.")
        text_file = open("guessed_words.txt", "a")
        text_file.write(player_word + "\n")
        text_file.close()
    else:
        print("You lose")


main()
