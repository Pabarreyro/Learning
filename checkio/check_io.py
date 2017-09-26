#  MOST WANTED LETTER: Find and return the most common letter in a input string.
# import string
#
# def checkio_mwl(text):
#     """
#     We iterate through latin alphabet and count each letter in the text.
#     Then 'max' selects the most frequent letter.
#     For the case when we have several equal letter,
#     'max' selects the first from they.
#     """
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)  # ascii_lowercase orders the letters already, breaking a tie
#
#
# checkio = lambda text: max(string.ascii_lowercase, key=text.lower().count)  # lambda replaces def f():
#
# print(checkio_mwl('THIS IS JUST A TEST OF MY FIRST FUNCTION'))
#
#
# def checkio(text):
#     count = 0
#     lower = text.lower()
#     m_w_l = lower[0]
#     for i in lower:
#         if i.isalpha():
#             if lower.count(i) > count:
#                 m_w_l = i
#                 count = lower.count(i)
#             elif lower.count(i) == count:
#                 if i < m_w_l:
#                     m_w_l = i
#                     count = lower.count(i)
#     return m_w_l

#  NON-UNIQUE ELEMENTS:
#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    output = []
    for i in data:
        if data.count(i) > 1:
            output.append(i)
    return output


def checkio(data):
    return [i for i in data if data.count(i) > 1]


# checkio=lambda d:[x for x in d if d.count(x)>1]



