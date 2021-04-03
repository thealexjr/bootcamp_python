from sys import argv
from re import sub
def filter():
        if len(argv) != 3 or not argv[2].isdigit():
                print("ERROR")
                return
        n = int(argv[2])
        if n == 0:
                return
        words = argv[1].split(' ')
        words[:] = [sub("\W", '', each) for each in words]
        longwords = []
        for each in words:
                if len(each) > n:
                        longwords.append(each)
        if len(longwords) == 0:
                print("ERROR")
        else:
                print(longwords)
        return

filter()
