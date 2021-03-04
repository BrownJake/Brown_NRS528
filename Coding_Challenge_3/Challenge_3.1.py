# Coding Challenge 3.1
# Simple Directory Tree

# First, import the os system
import os

# Create a temporary directory to store the folders
tree_branch = "C:\Temp_Dir"
os.mkdir(tree_branch)

# Create the folders from first branch and join them in temporary directory
branch_one = ["draft_code", "includes", "layouts", "site"]

for folder in branch_one:
    os.mkdir(os.path.join(tree_branch, folder))

# Create the folders from second branch and join them in draft_code folder
branch_two = ["pending", "complete"]

for folder in branch_two:
    os.mkdir(os.path.join(tree_branch, "draft_code", folder))

# Create the folders from third branch and join them in layouts folder
branch_three = ["default", "post"]

for folder in branch_three:
    os.mkdir(os.path.join(tree_branch, "layouts", folder))

# Add the posted folder into the post folder within the layouts folder
os.mkdir(os.path.join(tree_branch, "layouts", "post", "posted"))

# Import shutil to delete the directory tree
import shutil

shutil.rmtree(tree_branch)

#Feedback - Beautiful code. Very well done on this one Jake.
