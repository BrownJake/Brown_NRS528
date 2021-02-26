# Coding Challenge 3.2
# Push sys.argv to the limit

# Use scrabble score code to find out how much each monster scores using sys.argv inputs
# This is done with 10 lines of code

# First, import sys (1 line of code)
import sys

# Copy over letters and their associated scores (5 lines of code)
score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1,  "f": 4,
         "g": 2, "h": 4,"i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4,"z": 10}

# Create and put arguments into list (1 line of code)
# Adding each argument using .append takes up more lines of code
monster_list = [sys.argv[1], sys.argv[2], sys.argv[3]]

# Use for loop to obtain and print scrabble score for each monster (3 lines of code)
# monster.lower will convert letters to lowercase to avoid errors
# Open the .bat file outside of Pycharm to view printed statement
for monster in monster_list:
    score_scrabble = sum(score[m] for m in monster.lower())
    print(monster.lower() + " gets a score of " + str(score_scrabble) + "!")
