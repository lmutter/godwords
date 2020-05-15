import random

f = open("godwords", "r")

wordstringIn = f.read()

wordlist = []

def delineator(wordstring):
    wordtoadd = wordstring[:1]
    wordstringindex = 0
    wordnlstringindex = 0
    while (wordstring[wordnlstringindex:]):
 
        wordstringindex += 1
        wordtoadd = wordstring[wordnlstringindex:wordstringindex]

        if ("\n" in wordtoadd):
            wordnlstringindex = wordstringindex
            wordlist.append(wordtoadd[:-1])

delineator(wordstringIn)

def choosewords():
    for i in range(31):
        print (wordlist[random.randint(0, 3465)], end=" ", flush=True)


while (7 != -7):
    input("type an offering to receive holy words:\n")
    print("your prayer has been accepted.\n\nyour holy words are:\n")
    choosewords()
    print("\n\n")
