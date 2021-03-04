# Coding Challenge 2.5
# User Input 2

# Create dictionary for letters and their scores
score = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
         "d": 2, "g": 2,
         "b": 3, "c": 3, "m": 3, "p": 3,
         "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
         "k": 5,
         "j": 8, "x": 8,
         "q": 10, "z": 10}


# First, define function with the parameter "word,"
# then, set variable total to an int or 0,
# then, use for loop to pass through each letter in the word entered,
# while i.lower will convert letters to lowercase to avoid errors,
# finally, return the score for the word entered
def scrabble_score(word):

    word = word.lower()

    not_in_dict = []

    for k in word:
        if not k in score:
            not_in_dict.append(k)

    if len(not_in_dict) > 0:
        print("Sorry, I cannot run as you have provided an incorrect character")
    else:
        total = 0
        for i in word:
            total = total + score[i.lower()]
        print("Here is your score: " + str(total))
        return


# Print score for the word entered (e.g., dog, zebra, elephant, etc.)
scrabble_score("Enter")

#Feedback- your code threw an error, as "Enter word here", contains whitespace that does not
#match your dict, so I suggest using some other way to pull in the needed string, but also
# you should try to pick up on a key error such as a unknown character being added. I've extended
# your code with a basic test to capture this.