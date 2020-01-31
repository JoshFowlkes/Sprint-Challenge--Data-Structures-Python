import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

'''
# The original
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''


'''
Bringing in the binary search tree + the stacks and queueus from the week
'''
from binary_search_tree import BinarySearchTree
# Inserting the values into the tree
bst = BinarySearchTree(names_1[0])
for name in names_1:
    bst.insert(name)
duplicates = []
# using pythons .contains and getting any names that are in the binary search tree and appending them to 
    # the list of duplicates
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


# Nice, this one returns a runtime: 0.12014889717102051 seconds






end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?


# Using a set for best time 

duplicates = []
names_2_set = set(names_2)
for name in names_1:
    if name in names_2_set:
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# Best time was runtime: 0.0036118030548095703 seconds using a python set, nice 
