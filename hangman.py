import hangman_printer
import random

# list_of_words_animals = ["elephant", "tiger", "monkey", "lion", "butterfly"]
list_of_words_animals = ["monkey", "lion"]
# list_of_words_fruits = ["apple", "banana", "grapefruit", "strawberry"]
list_of_words_fruits = ["apple", "banana"]


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
        print("Nieprawidlowe slowo, zostalo ci " + str(chances) + " proby")
        print(player_word)
    elif chances == 4:
        print(hangman_printer.status2)
        print("Nieprawidlowe slowo, zostalo ci " + str(chances) + " proby")
        print(player_word)
    elif chances == 3:
        print(hangman_printer.status3)
        print("Nieprawidlowe slowo, zostalo ci " + str(chances) + " proby")
        print(player_word)
    elif chances == 2:
        print(hangman_printer.status4)
        print("Nieprawidlowe slowo, zostalo ci " + str(chances) + " proby")
        print(player_word)
    elif chances == 1:
        print(hangman_printer.status5)
        print("Nieprawidlowe slowo, zostalo ci " + str(chances) + " proby")
        print(player_word)
    elif chances == 0:
        print(player_word)
        print(hangman_printer.status6)


def game(list_of_words):
    word = random.choice(list_of_words)
    player_word = "*" * len(word)
    chances = 6
    used_letters = []
    print("twoje slowo to: " + player_word + " zaczynasz z czysta karta")
    while chances > 0 and word != player_word:
        player_input = input("wybierz litere: ").lower()
        if player_input in word and player_input not in used_letters:
            player_word = good_answer(player_input, player_word, word)
            used_letters.append(player_input)
            print(player_word)
        elif player_input not in word and player_input not in used_letters:
            chances = wrong_answer(chances)
            print_hangman(chances, player_word)
            used_letters.append(player_input)
        else:
            print("Uzyles juz te litery, wybierz inna")
    win_lose(player_word, word)


def start_game():
    while True:
        print("1. Zwierzeta")
        print("2. Owoce")
        player_input = input("Wybierz jaki rodzaj slowa chcesz odgadnac ")
        if player_input == str(1):
            game(list_of_words_animals)
        elif player_input == str(2):
            game(list_of_words_fruits)
        while True:
            player_input = input("Chcesz zagrac jeszcze raz? y/n: ")
            if player_input.lower() == "y":
                start_game()
            elif player_input.lower() == "n":
                break
            else:
                print("Wybrales nieprawidlowa opcje")
        break


def main():
    while True:
        print(hangman_printer.start)
        print("1. Rozpocznij gre")
        print("2. Pokaz odkryte slowa")
        print("3. Wyjdz z gry")
        player_input = input("Wybierz opcje: ")
        if player_input == str(1):
            start_game()
        elif player_input == str(2):
            text_file = open("guessed_words.txt", "r")
            text_file = text_file.read()
            print(text_file)
            player_choice = input("Wcisnij przycisk zeby wyjsc")
        elif player_input == str(3):
            print("Goodbye")
            break
        else:
            print("Wybrales nieprawidlowa opcje")


def win_lose(player_word, word):
    if player_word == word:
        print("Gratulacje, wygrales. Twoje slowo zostalo zapisane")
        text_file = open("guessed_words.txt", "a")
        text_file.write(player_word + "\n")
        text_file.close()
    else:
        print("Przegrales")


main()
