zbor = "peperutkae"
display = []
lives = 6

for letter in zbor:
    display += "_"
print(display)

end_game = False
while not end_game:
    guess = input("Pogodi bukva: ")
#Updating display
    did_guess_matched_letter = False
    did_you_double_guess = False
    for position in range(len(zbor)):
        letter = zbor[position]
        if guess == letter:
            if display[position] != "_":
                did_you_double_guess = True
            else:
                did_guess_matched_letter = True
            display[position] = letter
    if did_you_double_guess == True:
        print("Ja pogodivte istata bukva dva pati.")

    if did_guess_matched_letter == False:
        lives -= 1
        print(f"Izgubivte zivot. Vi ostanuvaat {lives} zivoti. ")

#Dali site bukvi se pogodeni
    empty_found = False
    for simbol in display:
        if simbol == "_":
            empty_found = True
    if empty_found == False:
        print("Game over. You won.")
        end_game = True
    print(display)

#Check if we have lives left
    if lives == 0:
        print("Game over. You lose.")
        end_game = True
