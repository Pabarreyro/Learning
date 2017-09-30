# Note: formula is 4.71 (characters/words) + .5 (words/sentence)-21.43
import string

ari_scale = {
         1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
         2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
         3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
         4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
         5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
         6: {'ages': '10-11', 'grade_level':    '5th Grade'},
         7: {'ages': '11-12', 'grade_level':    '6th Grade'},
         8: {'ages': '12-13', 'grade_level':    '7th Grade'},
         9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

punct_list = [".", "!", "?", ",", ";", ":", "'", "-", '"']

file_dict = {
      "1": "on_trade_disputes_bill",
      "2": "blood_toil_tears_sweat",
      "3": "finest_hour",
      "4": "sinews_of_peace",
      "5" : "never_despair"}

def menu():
    running = 0
    while running == 0:
        print('Welcome to the Churchill ARI Query!\n'
              'Select from the following Churchill speeches to see what its modern ARI score would be:\n'
              '1. Speech on Trade Unions and Trade Disputes Bill (1904)\n'
              '2. Blood, Toil, Tears and Sweat (May 1940)\n'
              '3. Finest Hour (June 1940)\n'
              '4. Sinews of Peace (March 1946)\n'
              '5. Never Despair (March 1955)\n'
              '\nor\n\n'
              'm. Learn more about ARI scores\n'
              'q. Quit\n')
        menu_action = input('What would you like to do?  ')
        if menu_action in 'q. Quit':
          print("Thanks for visiting the Churchill ARI Query!")
          running += 1
        elif menu_action in 'm. Learn more about ARI scores':
              print("ARI stands for Automated Readibility Index and is one of many tools used to give a rough indication of a work's readability.\n"
                    "The test generate a score based on characteristics such as statistical average word length (which is used as an unreliable proxy for semantic difficulty)\n "
                    "and sentence length (as an unreliable proxy for syntactic complexity) of the work.\n"
                    "The strength of the ARI is that its accuracy increases when finding the average readability of a large number of works.\n"
                    "In applying ARI to the famous Churchill speeches presented here we applied an arbitrary scale, seen below:\n\n"
                    "1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},\n"
                    "2: {'ages':   '6-7', 'grade_level':    '1st Grade'},\n"
                    "3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},\n"
                    "4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},\n"
                    "5: {'ages':  '9-10', 'grade_level':    '4th Grade'},\n"
                    "6: {'ages': '10-11', 'grade_level':    '5th Grade'},\n"
                    "7: {'ages': '11-12', 'grade_level':    '6th Grade'},\n"
                    "8: {'ages': '12-13', 'grade_level':    '7th Grade'},\n"
                    "9: {'ages': '13-14', 'grade_level':    '8th Grade'},\n"
                    "10: {'ages': '14-15', 'grade_level':    '9th Grade'},\n"
                    "11: {'ages': '15-16', 'grade_level':   '10th Grade'},\n"
                    "12: {'ages': '16-17', 'grade_level':   '11th Grade'},\n"
                    "13: {'ages': '17-18', 'grade_level':   '12th Grade'},\n"
                    "14: {'ages': '18-22', 'grade_level':      'College'}")
              running = 0
        else:
          return menu_action

def import_file(menu_action):
    file = open(file_dict[menu_action], "r")
    file = file.read()
    return file

def remove_punct(file):  # Could use .isalpha instead?
      punct_list = [",", ";", ":", "'", "-", '"']
      for punct in punct_list:
        clean_file = file.replace(punct, "")
        clean_file = file.replace("\n", "")
        return clean_file

def split_sentences(clean_file):
      punct_list = [".", "!", "?"]
      for punct in punct_list:
        sentences = clean_file.split(punct)
        return sentences

def split_words(sentences):
    word_list = []
    for sentence in sentences:
        line_split = sentence.split(" ")
        word_list.append(line_split)
    return word_list

def word_count(word_list):
    word_count_list = []
    for line in word_list:
        if '' in line:
            line.remove('')
        word_count_list.append(len(line))
    return word_count_list

def word_length(word_list):
    word_length_list = []
    for line in word_list:
        for i in line:
            word_length_list.append(len(i))
    return word_length_list

def sum_length(word_list):
    characters = 0
    for i in word_list:
        characters += int(i)
    return character

def ari_scale_calc(ari_scale, formula):
    print("This text has an ARI rating of {}. ".format(str(formula)))
    print("")
    print("This corresponds to a {} reading level; appropriate for {} year-olds.".format(ari_scale[formula]["grade_level"], ari_scale[formula]["ages"]))
    print("")

def remove_space(split_words):
    for line in split_words:
        for i in line:
            if i == "":
                line.remove(i)
    return split_words


def test():
      menu_action = menu()  # Check
      file = import_file(menu_action)  # Check
      clean_file = remove_punct(file)  # Check
      sentences = split_sentences(clean_file)  # Check
      word_list = split_words(sentences)  # Check
      word_count_list = word_count(word_list)  # Check
      word_length_list = word_length(word_list)
      print(word_list)
      print(word_count_list)
      print(word_length_list)


print(test())
