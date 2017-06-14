# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def hangman():
    word = choose_word(wordlist)
    #print word
    list2 = []
    list3 = []
    n = len(word)
    for ltr in word:
        list2.append ("_")
        list3.append (ltr)
    print list2
    head = " O"
    torso = "/|]"
    legs = " /\ "
    print head
    print torso
    print legs
    g = 7
    while g > 1:
        g = (g-1)
        print "you have"
        print g
        print "guesses left"
        usript1 = raw_input("guess a letter (no caps): ")
        if len(usript1) > 1:
            print "I said one letter"
            continue
        if usript1 in word:
            print "you guessededed correct!"
            print head
            print torso
            print legs
            g = (g+1)
            for num in range (len(word)):
                if usript1 == word[num]:
                    list2 [num] = usript1
            if list2 == list3:
                print "you win"
                print list3
                break
            print list2
        else:
            print "Wrong! try aganz"
            if g == 6:
                legs = " \ "
                print head
                print torso
                print legs
            if g == 5:
                legs = " "
                print head
                print torso
                print legs
            if g == 4:
                torso = " |]"
                legs = " "
                print head
                print torso
                print legs
            if g == 3:
                torso = " | "
                legs = " "
                print head
                print torso
                print legs
            if g == 2:
                torso = " "
                legs = " "
                print head
                print torso
                print legs
            if g == 1:
                head = " X"
                torso = "XXX"
                legs = "XX"
                print head
                print torso
                print legs
                print "you loose."








hangman()