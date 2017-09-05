# Objective: Write a python module to analyze a given text file containing a
# book for is vocabulary frequency and display the most frequent words to the user in the terminal.

# Instructions:
# 1. Open the file and deal with any decoding error that arise.

# 2.  Normalize all of the words so differences in capitalization and punctuation attached to words don't affect the counts.
#
# 3.  Count how often each unique word is used, then print the most frequent top 10 out with their counts.
#
# 4. Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.
#
# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         contents = file.readlines()
#         for line in contents:  # With a for loop...
#             print(line)
#     print(contents)
#

import string
import operator

def word_count(file_path):
    ct_dict= {}
    stop_words = ['a', 'the', 'is', 'i', 'an', 'is', 'me', 'my', 'he', 'his', 'her',
                  'they', 'them', 'their', 'we', 'our', 'us', 'to', 'from', 'and',
                  'but', 'was', 'be', 'in', 'on', 'have', 'it', 'that', 'she', 'with', 'do',
                  'this', 'that', 'not', 'or', 'as', 'what', 'go', 'can', 'who', 'get', 'if',
                  'would', 'all', 'make', 'when', 'which', 'some', 'into', 'see', 'your', 'now',
                  'than', 'like', 'how', 'these', 'want', 'way', 'look', 'first', 'also', 'new',
                  'day', 'more', 'use', 'no', 'yes', 'man', 'find', 'here', 'thing', 'give', 'many',
                  'well', 'one', 'very', 'by', 'of', 'had', 'him', 'at', 'for', 'room', 'there', 'been',
                  'so', 'back', 'even', 'did', 'were', 'are', 'about', 'only', 'just', 'said', 'any', 'other',
                  'could', 'other', 'then', 'up', 'you', 'out', 'still', 'made', 'while', 'mother', 'father',
                  'sister', 'brother', 'again', 'with', 'without', 'much', 'after', 'before', 'where', 'down',
                  'open', 'close', 'it', 'its', 'himself', 'herself', 'time', 'went', 'come', 'away', 'soon',
                  'family', 'came', 'left', 'right', 'too', 'though', 'look', 'hear', 'everything', 'little', 'big',
                  'thought', 'over', 'quite', 'looked', 'wanted', 'something', 'let', 'two', 'against', 'seemed',
                  'being', 'work', ]
    file = open(file_path, 'r')
    for line in file:
        scrub_list = line.replace(',', '').replace('(', '').replace(')', '').replace('\'', '').replace('.', '').replace(
            ';', '').replace('!', '').replace('"', '').replace('?', '').replace(':', '').replace('-', '').lower().split()
        for word in scrub_list:
            if word not in stop_words:
                    if word in ct_dict:
                        ct_dict[word] += 1
                    else:
                        ct_dict[word] = 1
    sort_ct_dict = sorted(ct_dict.items(), key=operator.itemgetter(1),  reverse=True)
    print("Here are the ten most common * unique * words in your book:\n")
    print("1.\t'{}', {} times".format(sort_ct_dict[0][0], sort_ct_dict[0][1]))
    print("2.\t'{}', {} times".format(sort_ct_dict[1][0], sort_ct_dict[1][1]))
    print("3.\t'{}', {} times".format(sort_ct_dict[2][0], sort_ct_dict[2][1]))
    print("4.\t'{}', {} times".format(sort_ct_dict[3][0], sort_ct_dict[3][1]))
    print("5.\t'{}', {} times".format(sort_ct_dict[4][0], sort_ct_dict[4][1]))
    print("6.\t'{}', {} times".format(sort_ct_dict[5][0], sort_ct_dict[5][1]))
    print("7.\t'{}', {} times".format(sort_ct_dict[6][0], sort_ct_dict[6][1]))
    print("8.\t'{}', {} times".format(sort_ct_dict[7][0], sort_ct_dict[7][1]))
    print("9.\t'{}', {} times".format(sort_ct_dict[8][0], sort_ct_dict[8][1]))
    print("10.\t'{}', {} times".format(sort_ct_dict[9][0], sort_ct_dict[9][1]))

word_count('kafka.txt')