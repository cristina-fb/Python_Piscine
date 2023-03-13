import sys
l = len(sys.argv)
if l != 2:
    if l > 2:
        print("AssertionError: more than one argument are provided")
    sys.exit()
try:
    num = int(sys.argv[1])
except:
    print("AssertionError: argument is not an integer")
    sys.exit()
if num == 0:
    print("I'm zero.")
elif num % 2 == 0:
    print("I'm even.")
else:
    print("I'm odd.")
