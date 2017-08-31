# Create a program that uses a dictionary to store phonebook entries. Must have user interaction.
# Include ability to:
# 1. Search
# 2. Add Entry
# 3. Change Entry
# 4. Delete Entry
# 5. Exit Program

# Loops
# Dictionaries (within a dictionary)
# Functional Program

phone_book = {
        'Barreyro': {'name':'Pablo Barreyro', 'number':'2025382341'},
        'Magnuson':{'name':'Tom Magnuson', 'number':'2023630404'},
        'Yeaney': {'name':'Johny Yeaney', 'number':'2024154909'}
}
# Set up menu function...
def print_menu():
    print('1. Search')
    print('2. Add Entry')
    print('3. Change Entry')
    print('4. Delete Entry')
    print('5. Exit Program')

# Set up fancy phone converter...
def fancy_phone(number):
    print(f"({number[0:3]}) {number[3:6]}-{number[6:]}")

# Set up action function...
def menu_action():
    print_menu()
    while True:
       action = input("What would you like to do? ")
       if action in '1. Search':
            search = input("What is the last name of the person you're looking for: ")
            print(str(phone_book[search]['name']))
            print(fancy_phone(phone_book[search]['number']))

       elif action in '2. Add Entry':
            add_name = input("Who would you like to add? ")
            add_num = input("What is his/her/their number? ")
            # Split and index full name...
            split_name = add_name.split(' ', 1)
            # ... use last name to access key
            phone_book[str(split_name[1])] = {'name': str(add_name.title()), 'number': str(add_num)}
            print("Okay, here's what I've got: ")
            print(phone_book[str(split_name[1])]['name'])
            print(fancy_phone(phone_book[str(split_name[1])]['number']))

       elif action in '3. Change Entry':
           change_type = input("Would you like to change a name or a number? ")
           if change_type.lower() in 'name':
               change_name = input("Whose name would you like to change? ")
               new_name = input ("What would you like to change his/her/their name to? ")
               split_name = change_name.split(' ', 1)
               phone_book[split_name[1]]['name'] = new_name
               print("Okay, great. I've changed {}'s name to {}.".format(split_name[0], new_name))

           if change_type.lower() in 'number':
               change_name = input("Whose number would you like to change? ")
               new_num = input("What would you like to change his/her/their number to? ")
               split_name = change_name.split(' ', 1)
               phone_book[split_name[1]]['number'] = new_num
               print("Okay, great. I've changed {}'s number to".format(split_name[0]))
               print(fancy_phone((phone_book[str(split_name[1])])))

       elif action in '4. Delete Entry':
            del_name = input("Whose entry would you like to delete? ")
            split_name = del_name.split(' ', 1)
            del phone_book[str(split_name[1])]
            print("Okay, that should do it. I've removed {} from the directory.".format(del_name))

       else:
         print("So long!")

menu_action()