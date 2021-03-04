# Coding Challenge 2.3
# Given a single phrase, count the occurrence of each word

# Create string for words in the phrase
string = 'hi dee hi how are you mr dee'


# Define a function to count the words, then create dictionary to hold keys:inputs,
# and finally split inputs into list by each individual item
def word_count(str):
    counts = dict()
    words = str.split()

    # Use for loop to check if items are in the dictionary and get print statement with counts
    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

#Feedback, again good job, well commented and very neat code. Impressive.

# Print the word plus the count
print(word_count(string))
