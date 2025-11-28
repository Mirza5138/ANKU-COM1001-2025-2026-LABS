#This code is incomplete by all means but at least it prints out one of the paths correctly. Contact me if you modify and complete the missing parts.
#I may return back to this code again later. Who knows...

import random

size = random.randint(3,5)
matrix = []
path = [] #List to store final path.
stack = [] #List to store which nodes go to which other ones.

def checkPriorNodes(node: int):
    if node == 1:
        path.append(node)
        return True
    for i in stack[node-1]:
        if checkPriorNodes(i):
            path.append(node)
            return True

print("Randomly selected number of nodes: "+str(size)+"\n\nAdjacency Matrix:")

for i in range(size): #Creates the matrix accordingly.
    matrix.append([0 for j in range(i+1)] + [random.randint(0,1) for j in range(size-i-1)])

for i in matrix: #Just prints the matrix line by line.
    print(i)

print(" ")

# startNode = int(input(f"Enter start node (1..{size}): "))
# endNode = int(input(f"Enter end node (1..{size}): "))

for i in range(size):
    stack.append([j+1 for j in range(size) if matrix[j][i]==1])

print(stack)

checkPriorNodes(size)
print(path)