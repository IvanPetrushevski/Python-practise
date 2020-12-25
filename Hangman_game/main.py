##########################-STEP 1-##########################
#
# word_list = ["aardvark", "baboon", "camel"]
#
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# import random
# izbran_zbor = random.choice(word_list)
# print(izbran_zbor)
#
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Vnesete bukva: ").lower()
#
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in izbran_zbor:
#   if letter == guess:
#     print("Correct")
#   else:
#     print("Wrong")

##########################-STEP 2-##########################

import random


broj_na_zivoti = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)

game_over = False
while game_over == False:
    guess = input("Pogoduvajte bukva: ").lower()


    pogodok = False
    for possition in range(len(chosen_word)):  #possition = 0, 1, 2, 3, ..... len(chosen_word)
        letter = chosen_word[possition]     # letter = b, a, b, o, o, n
        if letter == guess and display[possition] == "_":
            pogodok = True
            display[possition] = letter


    broj_pogodeni_bukvi = 0
    for letter in display:
        if letter != "_":
            broj_pogodeni_bukvi += 1

    if broj_pogodeni_bukvi == len(chosen_word):
        print("Bravo, gi pogodivte site bukvi.")
        game_over = True

    #Dali ima ushte ostanati zivoti?
    if pogodok == False:
        broj_na_zivoti -= 1

    if broj_na_zivoti == 0:
        print("Kraj, nemash vekje zivoti.")
        game_over = True

    print(f"Vi ostanuvaat {broj_na_zivoti} zivoti.\n\n")