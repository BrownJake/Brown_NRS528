# Coding Challenge 2.1
# List Values

# Original List
OG_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]

# Create new list that selects the items from the original, which are less than 5
new_list = OG_list[0:3]

# Print new list that has elements less than 5 from original list
print(new_list)

# Writing this in one line of Python
print(OG_list[0:3])


## Feedback - Technically correct, but what if the ordering of the
# list was not as such, your code would not work to extract values < 5
# use a for loop and an if to pull out the values required.
new_list2 = []
for i in OG_list:
    if i < 5:
        new_list2.append(i)
print(new_list2)