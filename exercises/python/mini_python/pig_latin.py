
# input_word = input("Give me a word to translate: ")
# # Reformat and identify the first letter
# rform_word = input_word.lower()
# first = input_word[0]
# # You can split using the following:
# # first_letter = word[0]
# # left_over = word [1:]
# # Set condition for words that start with vowels...
# # Could do it this way:
# # vowels = 'aeiou'
# if first in 'aeiou':
#     print(rform_word.capitalize + 'yay')
# # Set condition for all other words...
# else:
#     print(rform_word[1:].capitalize + first + 'ay')

def pig_funct(word):
    # input_word = input('Give me a word to translate: ')
    rform_word = word.lower()
    first = word[0]
    if first.lower() in 'aeiou':
        print(word.capitalize() + 'yay')
    else:
        print(rform_word[1:].capitalize() + first.lower() + 'ay')

pig_funct()

# # List vowels
# def pig_latin(word):
#     vowels = 'aeiou'
#     consonant = -1
#
#     for letter in word:
#         if letter.lower() in vowels:
#             break
#         else:
#             consonant += 1
#
#     first_letter = word[0:consonant +1]
#     left_over = word[consonant + 1:]
#
#     if first_letter() in vowels:
#         return '{0}yay'.format(word)
#     else:
#         if first_letter[0].isupper():
#             return '{0}{1}ay'.format(left_over.capitalize(), first_letter.lower())
#         else:
#             return '{0}{1}ay'.format(left_over, first_letter)

print(pig_latin('Chambray'))
