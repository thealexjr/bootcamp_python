def text_analyzer(txt = ""):
        """This function counts the number of upper characters, lower characters,punctuation and spaces in a given text."""
        if txt=="":
                print("What is the text to analyse? ")
                text_analyzer(input())
                return
        upper = 0
        lower = 0
        punct = 0
        spaces = 0

        for each in txt:
                if each.isupper():
                        upper += 1
                elif each.islower():
                        lower += 1
                elif each.isspace():
                        spaces += 1
                else:
                        punct += 1
        total=int(upper)+int(lower)
        print("The text contains "+ str(total) +" characters:")
        print("-"+str(upper) + " upper characters")
        print("-"+str(lower) + " lower characters")
        print("-"+str(punct) + " punctuation characters")
        print("-"+str(spaces) + " spaces")
text_analyzer()
#text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
print(text_analyzer.__doc__)
