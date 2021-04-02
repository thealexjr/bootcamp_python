import sys

def main():
        usage = "Usage: python operations.py <number1> <number2>\n"\
                        "Example:\n\tpython operations.py 10 3"
        if len(sys.argv) < 3:
                print(usage)
                return
        if len(sys.argv) >  3:
                print("InputError: too many numbers\n\n" + usage)
                return
        for each in sys.argv[1:]:
                for c in each:
                        if c.isdigit() == 0:
                                print("InputError: only numbers\n" + usage)
                                return
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print("Sum:             " + str(x + y))
        print("Difference:      " + str(x - y))
        print("Product: " + str(x * y))
        if (y == 0):
                print("ERROR (div by zero)")
                print("ERROR (modulo by zero)")
        else:
                print("Quotient:        " + str(x / y))
                print("Remainder:       " + str(x % y))



if __name__ == "__main__":
        main()
