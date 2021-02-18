# Coding Challenge 2.4
# User Input

# Use if/elif to print statement depending on whether the person's age is below or above 65
age = int(input("What is your age?"))
if age < 65:
    retire_age = 65 - age
    print("You will reach retirement age in {0} year(s).".format(retire_age))
elif age > 65:
    print("You have reached retirement age.")
