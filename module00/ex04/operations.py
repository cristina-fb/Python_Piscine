import sys
if len(sys.argv) < 3:
    sys.exit("Usage: python operations.py <number1> <number2>\nExample:\n  python operations.py 10 3")
elif len(sys.argv) > 3:
    sys.exit("AssertionError: too many arguments")
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except:
    sys.exit("AssertionError: only integers")
print("Sum: " + str(num1 + num2))
print("Difference: " + str(num1 - num2))
print("Product: " + str(num1 * num2))
try:
    print("Quotient: " + str(num1 / num2))
except:
    print("Quotient: ERROR (division by zero)")
try:
    print("Remainder: " + str(num1 % num2))
except:
    print("Remainder: ERROR (modulo by zero)")

