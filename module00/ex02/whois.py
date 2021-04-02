import sys

arg = sys.argv
if arg[1].isnumeric():
        if len(arg)==2:
                if int(arg[1])==0:
                        print("I'm Zero")
                elif int(arg[1])%2==0:
                        print("I'm even")
                else:
                        print("I'm odd")
        else:
                print('ERROR')
else:
        print("ERROR")
