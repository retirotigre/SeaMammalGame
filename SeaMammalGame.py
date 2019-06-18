import random

words = 'seal whale dolphin otter walrus narwhal manatee'.split()
lc_alphabet = "abcdefghijklmnopqrstuvwxyz"

def getrandomword(wordList):
    x1 = random.randint(0, len(wordList)-1)
    return wordList[x1]

answer = getrandomword(words)

spelled_out = []
for character in list(answer):
    spelled_out.append(character)

blanks = []

for x2 in range(0, len(spelled_out)):
    blanks.append(["_"])

def print_blanks(blanks):
    for x3 in blanks:
        print " ".join(x3),

wrong_guess = []

while (True):
    def print_wrong(wrong_guess):
        for x4 in wrong_guess:
            print " ".join(x4),
    print
    print "word:",
    print_blanks(blanks)
    print
    print "wrong guesses:",
    print_wrong(wrong_guess)
    print
    print "Guess character or whole message?"
    print "Press 1 for character"
    print "Press 2 for message"
    s = raw_input("Selection: ")
    try:
        response = int(s)
    except:
        print "ERROR: please make a selection: 1 or 2"
        continue
    if response == 1 or response == 2:
        if response == 1:
            guess_char = raw_input("Guess a letter: ")
            if guess_char in lc_alphabet:
                if guess_char in answer:
                    count = 0
                    for x4 in spelled_out:
                        if guess_char == spelled_out[count]:
                            blanks[count] = guess_char
                        count += 1
                    if ["_"] in blanks:
                        continue
                    else:
                        print_blanks(blanks)
                        print
                        print "You are correct"
                        break
                else:
                    wrong_guess.append(guess_char)
            else:
                print "Guess a lowercase letter"
        elif response == 2:
            guess_string = raw_input("Guess the message: ")
            print guess_string
            if guess_string == answer:
                print "You are correct"
                break
            else:
                print "Incorrect"
                raw_input("Press Enter to Continue")
    else:
        print "ERROR: choose either 1 or 2"
        raw_input("Press Enter to Continue")

print "GAME OVER"
