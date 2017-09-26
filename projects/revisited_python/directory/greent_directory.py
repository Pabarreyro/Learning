# gt_name = input("Give me a name: ")
# if str(gt_name.lower()) in 'sharon':
#     print('{} is a Consul (ESFJ)'.format(gt_name.capitalize()))
# if str(gt_name.lower()) in 'aaron, jennifer, jen':
#     print('{} is a Commander (ENTJ)'.format(gt_name.capitalize()))
# if str(gt_name.lower()) in 'rob, robert':
#     print('{} is an Entertainer (ESFP)'.format(gt_name.capitalize()))
# if str(gt_name.lower()) in 'alex, alexis':
#     print('{} is a Logician (INTP)'.format(gt_name.capitalize()))
# if str(gt_name.lower()) in 'john':
#     print('{} is an Architect (INTJ)'.format(gt_name.capitalize()))
# if str(gt_name.lower()) in 'jessy, jesse, michelle, chelle':
#     print('{} is a Protagonist (ENFJ)'.format(gt_name.capitalize()))
# if str(gt_name.lower()) in 'pablo':
#     print('{} is a Debater (ENTP)'.format(gt_name.capitalize()))
# if str(gt_name.lower()) in 'chris':
#     print('{} is a Campainger (ENFP)'.format(gt_name.capitalize()))


gt_registry = {'Sharon': {'name': 'Sharon Hatch', 'type': 'Consul (ESFJ)', 'title': 'Officer of Play Dates'},
               'Aaron': {'name': 'Aaron Smith', 'type': 'Commander (ENTJ)', 'title': 'Officer of Special Projects'},
               'Jen': {'name': 'Jen Burgess', 'type': 'Commander (ENTJ)', 'title': 'Officer of Hospitality'},
               'Jesse': {'name': 'Jesse Friedt', 'type': 'Protagonist (ENFJ)', 'title': 'Officer of Fun'},
               'Rob': {'name': 'Rob Nathan', 'type': 'Entertainer (ESFP)', 'title': 'Officer of Home & Garden'},
               'Michelle': {'name': 'Michelle Antalos', 'type': 'Protagonist (ENFJ)', 'title': 'Joint Chief of Staff'},
               'Alexis': {'name': 'Alexis Acosta', 'type': 'Logician (INTP)', 'title': 'Officer of Intrigue'},
               'Elise': {'name': 'Elise Jannuzzi', 'type': 'Mediator (INFP)', 'title': 'Officer of Bread'},
               'John': {'name': 'John Spence', 'type': 'Architect (INTJ)', 'title': 'Officer of Utility'},
               'Bob': {'name': 'Bob Webber', 'type': 'Entrepreneur (ESTP)', 'title': 'Title pending'},
               'Ivana': {'name': 'Ivana Deletis', 'type': 'Protagonist (ENFJ)', 'title': 'Officer of Movement'},
               'Chris K': {'name': 'Chris Kaminski', 'type': 'Campaigner (ENFP)', 'title': 'Officer of Recreation'},
               'Pablo': {'name': 'Pablo Barreyro', 'type': 'Debater (ENTP)', 'title': 'Officer of Inquiry'},
               'Fernel': {'name': 'Fernel Valdez', 'type': 'Debater (ENTP)', 'title': 'Title pending'},
               'Jane': {'name': 'Jane Moisan', 'type': 'Campaigner (ENFP)', 'title': 'Title pending'},
               'Garret': {'name': 'Garret Wright', 'type': 'Protagonist (ENFJ)', 'title': 'Title pending'},
               'Chris T': {'name': 'Chris Taylor', 'type': 'Adventurer (ISFP)', 'title': 'Title pending'},
               'Danielle': {'name': 'Danielle Taylor', 'type': 'Defender (ISFJ)', 'title': 'Title pending'},
               'Alex': {'name': 'Alex Cambier', 'type': 'Adventurer (ISFP)', 'title': 'Officer of Defense'},
               'Benjamin': {'name': 'Benjamin Emerson', 'type': 'Advocate (INFJ)', 'title': 'Officer of Patience'},}

def print_menu():
    print("Welcome to the Green T Member Directory!!")
    print('1. Search')
    print('2. Add Entry')
    print('3. Change Entry')
    print('4. Delete Entry')
    print('5. Exit Program')
    print()

print_menu()

action = input("What would you like to do? ")

if action in '1. Search':
    search = input("Who are you looking for? ")
    if search in 'Chris':
        clarify_chris = input("Which Chris are we talking about? ")
        if clarify_chris in 'Chris Taylor':
            print(gt_registry['Chris T']['name'])
            print(gt_registry['Chris T']['title'])
            print(gt_registry['Chris T']['type'])
        if clarify_chris in 'Chris Kaminski':
            print(gt_registry['Chris K']['name'])
            print(gt_registry['Chris K']['title'])
            print(gt_registry['Chris K']['type'])
    elif search != 'Chris':
        print(gt_registry[search]['name'])
        print(gt_registry[search]['title'])
        print(gt_registry[search]['type'])

if action in '2. Add Entry':
    add_name = input("Who would you like to add? ")
    add_title = input("What is his/her/their title? ")
    add_type = input("What is his/her/their personalite type? ")
    split_name = add_name.split(' ', 1)
    gt_registry[split_name[0]] = {'name': str(add_name),
                                 'title': str(add_title),
                                 'type' : str(add_type)}
    print("Okay, here's what I've got: ")
    print(gt_registry[split_name[0]]['name'])
    print(gt_registry[split_name[0]]['title'])
    print(gt_registry[split_name[0]]['type'])

# if action in '3. Change Entry':
#     change_type = input("Would you like to change a name or a number? ")
#     if change_type.lower() in 'name':
#         change_name = input("Whose name would you like to change? ")
#         new_name = input ("What would you like to change his/her/their name to? ")
#         split_name = change_name.split(' ', 1)
#         phone_book[split_name[1]]['name'] = new_name
#         print("Okay, great. I've changed {}'s name to {}.".format(split_name[0], new_name))
#
#     if change_type.lower() in 'number':
#         change_name = input("Whose number would you like to change? ")
#         new_num = input("What would you like to change his/her/their number to? ")
#         split_name = change_name.split(' ', 1)
#         phone_book[split_name[1]]['number'] = new_num
#         print("Okay, great. I've changed {}'s number to".format(split_name[0]))
#         print("({}) {}-{}".format(phone_book[str(split_name[1])]['number'][0:3],
#         phone_book[str(split_name[1])]['number'][3:6],
#         phone_book[str(split_name[1])]['number'][6:]))
#
# if action in '4. Delete Entry':
#     del_name = input("Whose entry would you like to delete? ")
#     split_name = del_name.split(' ', 1)
#     del phone_book[str(split_name[1])]
#     print("Okay, that should do it. I've removed {} from the directory.".format(del_name))
#
# if action in '5. Exit Program':
#     print("So long!")
