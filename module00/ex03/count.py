import string
import sys
def text_analyzer(s = None):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    if not s:
        s = input("What is the text to analyze?\n")
    ucase = 0
    lcase = 0
    marks = 0
    space = 0
    if not isinstance(s, str):
        print("AssertionError: argument is not a string")
        return
    for i in s:
        if i.isupper():
            ucase += 1
        elif i.islower():
            lcase += 1
        elif i.isspace():
            space += 1
        elif i in string.punctuation:
            marks += 1
    print("The text contains " + str(len(s)) + " character(s)")
    print("- " + str(ucase) + " upper letter(s)")
    print("- " + str(lcase) + " lower letter(s)")
    print("- " + str(marks) + " punctuation mark(s)")
    print("- " + str(space) + " space(s)")

if len(sys.argv) > 2:
    sys.exit("ERROR! Incorrect number of arguments")
if len(sys.argv) == 1:
    text_analyzer()
else:
    text_analyzer(sys.argv[1])
