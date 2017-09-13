# 1. Read text from a file
# 2. Check text for curse words
import urllib


def read_text(file):
    doc = open(file)  # We are creating an object of a file
    text = doc.read()  # We use this notation because we are working with object "doc"
    print(text)
    check_profanity(text)
    doc.close()  # Don't forget to close the document...

read_text('movie_quotes.txt')


def check_profanity(text):
    # Will refer to existing website, but could easily replace with reading doc file
    connection = urllib.urlopen(
        "http://www.wdyl.com/profanity?q={}".format(text))  # Fetches data from URL and creates file-like object
    output = connection.read()
    print(output)
    connection.close()
    if 'true' in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


# In the background...
