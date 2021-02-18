# Coding Challenge 2.2
# List Overlap

# The two original lists
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

# Find items present in both lists using for loop
for i in list_a:
    for j in list_b:
        if i == j:
            print(i)

# Find items that don't overlap using two for loops
for i in list_a:
    if i not in list_b:
        print(i)

for j in list_b:
    if j not in list_a:
        print(j)
