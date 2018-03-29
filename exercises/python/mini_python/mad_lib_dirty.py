## Madlib project
# print ("Welcome to Pablo's Madlib exercise!")
# #The following will prompt the user to enter words for the madlib.
# girl = input("Type a common girls' name: ")
# animal = input("Type a real or imaginary animal: ")
# verb = input("Type a verb (eat, work, dance): ")
# verb2 = input("Type another verb (sleep, run, sing): ")
# obj =  input("Type an object (vase, desk,pen): ")
# adjective = input("Type an adjective (floppy, dirty, loud): ")
# past_verb = input("Type a past-tense verb (ran, died, laughed): ")
# # The following will introduce the madlib and then print it out for the user.
#
# print ("Thanks! Here's your madlib:")
# print (
# "Once upon a time there was a poor little girl named {} who lived in the forest with a(n) {}."
# "She was forced to {} all day whole the {} sat around {}ing."
# "But then one day the little girl found a magic {}.When {} picked up the {}, she found that anything she imagined came true."
# "Soon, {} was making the {} {} while she chose to sit around and {}."
# "After a while, the girl realized this was not a very {} thing to do and released the {} from her spell."
# "They became best friends and {} every day, living happily ever after."
# .format(girl, animal, verb, animal, verb2, obj, girl, obj, girl, animal, verb, verb2, adjective, animal, past_verb))
#
# # Creating using an f-string
# print("Once upon a time there was a poor little girl named {girl} who lived in the forest with a(n) {animal}."
# "She was forced to {verb} all day whole the {animal} sat around {verb2}ing.")
#
# verb_list = []
# verb_list.append(input("Type a verb (eat, work, run)"))
# verb_list.append(input("Type a verb (eat, work, run)"))
# verb_list.append(input("Type a verb (eat, work, run)"))
#
# obj_list = []
# obj_list.append(input("Type a object (vase, desk,pen)"))
# obj_list.append(input("Type a object (vase, desk,pen)"))
# obj_list.append(input("Type a object (vase, desk,pen)"))
#
# print (verb_list)
# print (obj_list)

# # Utilizing split function
# verb = input("Enter three verbs, separated by commas: ").split(',')
#
# obj = input("Enter three objects, separated by commas: ").split(',')
#
#
# print (verb)
# print (obj)

# # As a function
# from random import shuffle
# # Call the function
# def split_words(string):
#         word_list = string.split(', ')
#         shuffle(word_list)
#         return word_list
# # Don't split it twice!
# verb = input("Enter three verbs, separated by commas: ")
# obj = input("Enter three objects, separated by commas: ")
#
# verb_list = split_words(verb)
# obj_list = split_words(obj)
#
# print(verb_list)
# print (obj_list)

# # Integrating repeat function
# from random import shuffle
# # Call the function
# def split_words(string):
#         word_list = string.split(', ')
#         shuffle(word_list)
#         return word_list
# #Establish a condition for continued play...
# playing = True
#
# # ...create a special content. But don't forget that "x" is a terrible var
# while playing:
# # Add a condition for stopping the loop
#         query = input ("Type '1' to enter new words, '2' to read story, or '3' to exit: ")
#         if query == '1':
#             verb = input("Enter three verbs, separated by commas: ")
#             obj = input("Enter three objects, separated by commas: ")
#             verb_list = split_words(verb)
#             obj_list = split_words(obj)
#         elif query == '2':
#                 print (f"When she picked up the {obj_list[0]}, she found that anything she imagined came true.")
#                 # "Soon, {} was making the {} {} while she chose to sit around and {}."
#         elif query == '3':
#                 print ("Thanks for playing!")
#                 playing = False
#         else:
#             print ("I don't understand that. Try again")

# # Don't split it twice!
# verb = input("Enter three verbs, separated by commas: ")
# obj = input("Enter three objects, separated by commas: ")
#
# verb_list = split_words(verb)
# obj_list = split_words(obj)
#
# print(verb_list)
# print (obj_list)

# # Second Lab: Fancy Phone number
# phone_number = input("Please enter your ten-digit phone number: ")
# # Split the string into several str([]) components, adding the necessary punctuation
# print (f"({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:]}")

## Distance conversion function assignment.
def unit_convert(float_num)
    distance = float(input("Enter a distance: ")
    input_unit = input("What unit are you starting with (mi, km, m, or ft)? ")
    output_unit = input("What would you like to convert to (mi, km, m, or ft)? ")
# Create conditions for input and output for all scenarios

playing = True
while playing:
    if (input_unit == 'mi' and output_unit == 'km'): #miles to kilometers
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in kilometers is: {output_unit}")

    elif (input_unit == 'mi' and output_unit == 'm'): #miles to meters
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in meters is: {output_unit}")

    elif (input_unit == 'mi' and output_unit == 'ft'): #miles to feet
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in feet is: {output_unit}")

    elif (input_unit == 'km' and output_unit == 'mi'): #kilometers to miles
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in miles is: {output_unit}")

    elif (input_unit == 'km' and output_unit == 'm'): #kilometers to meters
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in meters is: {output_unit}")

    elif (input_unit == 'km' and output_unit == 'ft'): #kilometers to feet
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in feet is: {output_unit}")

    elif (input_unit == 'm' and output_unit == 'km'): #meters to kilometers
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in kilometers is: {output_unit}")

    elif (input_unit == 'm' and output_unit == 'mi'): #meters to miles
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in miles is: {output_unit}")

    elif (input_unit == 'm' and output_unit == 'ft'): #meters to feet
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in feet is: {output_unit}")

    elif (input_unit == 'ft' and output_unit == 'km'): #feet to kilometers
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in kilometers is: {output_unit}")

    elif (input_unit == 'ft' and output_unit == 'mi'): #feet to miles
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in miles is: {output_unit}")

    elif (input_unit == 'ft' and output_unit == 'm'): #feet to meters
        conv_fac = 1.609 #conversion factor
        output_unit = distance * conv_fac
        print ("The distance in meters is: {output_unit}")
else:
    print ("Something went wrong. Shall we try again?")
