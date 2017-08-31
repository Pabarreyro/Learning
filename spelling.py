# Create a program that asks for a _single_ English word and checks if it follows the rule **"I before E except after C".
# Write a function that searches for the index of any instances of `ie` in the string, then see if the preceding letter is `c`.

def ie_search(word):
    if 'ie' in word:
        if 'cie' in word:
            word_split = word.split('ie', 1)
            print("I think you'll find that it's spelled '{}ei{}.'".format(word_split[0].lower(), word_split[1]))
        else:
            print("Seems fine to me, champ.")

ie_word = str(input("What word would you like to spellcheck? "))
ie_search(ie_word)