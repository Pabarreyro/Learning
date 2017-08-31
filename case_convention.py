# Write a program that prompts the user for a word.
# Print out either  `snake_case` or `CamelCase` depending case convention it is!.
# Use substring membership with the `in` operator

def case_convention(word):
    score = '_'
    chk_word = word[1:]
    if chk_word != chk_word.lower():
        print("It appears as though you are using the CamelCase convention.")
    elif score in chk_word:
        print("It appears as though you are using the snake_case convention.")
    else:
        print("I'm not sure what convention you are using. Please try again.")

in_word = str(input("What is the name you are using? "))
case_convention(in_word)
