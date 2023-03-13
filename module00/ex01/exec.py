import sys
if len(sys.argv) > 1:
    argv = " ".join(sys.argv[1:])
    argv = "".join(reversed(argv.swapcase()))
    print(argv)
