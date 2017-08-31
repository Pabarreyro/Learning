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


def punct_scrub(file_path):
    file = open(file_path, 'w')
    file.translate(string.maketrans("", ""), string.punctuation)

def word_count(file_path):
    file = open(file_path, 'r')
    count = {}
    stop_words = ['a', 'the', 'is', 'i', 'an', 'is', 'me', 'my', 'he', 'his', 'her',
                  'they', 'them', 'their', 'we', 'our', 'us', 'to', 'from', 'and',
                  'but', 'was', 'be', 'in', 'on', 'have', 'it', 'that', 'she', 'with', 'do',
                  'this', 'that', 'not', 'or', 'as', 'what', 'go', 'can', 'who', 'get', 'if',
                  'would', 'all', 'make', 'when', 'which', 'some', 'into', 'see', 'your', 'now',
                  'than', 'like', 'how', 'these', 'want', 'way', 'look', 'first', 'also', 'new',
                  'day', 'more', 'use', 'no', 'yes', 'man', 'find', 'here', 'thing', 'give', 'many',
                  'well', 'one', 'very', 'by']
    words = file.read().lower().split()
    for word in words:
        if word not in stop_words:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
    print(count)
    lst_count = (word, count[word])
    print(lst_count)


punct_scrub('metamorphosis.txt')


# word_count('metamorphosis.txt')
