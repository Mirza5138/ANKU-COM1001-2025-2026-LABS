#Credits to Arda Emre Kahriman for submitting the solution to the repository.

import random

def indexlist(list, value=1):
    indexes = []
    while value in list:
        indexes.append(list.index(value))
        list[list.index(value)] = 0
    return indexes

n = random.randint(3, 5)
print(f"Randomly selected number of nodes: {n}")
print("Adjacency matrix: ")
matrix = []
for i in range(n): #Creates the matrix using nested lists.
    row = []
    for k in range(n):
        if k<=i:
            row.append(0)
        else:
            row.append(random.randint(0, 1))
    matrix.append(row)
    print(row)
try:
    startNode = int(input(f"Enter starting node(1..{n}): "))
    endNode = int(input(f"Enter end node(1..{n}): "))
    if not (1 <= startNode <= n and 1 <= endNode <= n):
        print(f"Nodes must be in range 1..{n}")
    else:
        _end = endNode - 1
        _start = startNode - 1
        if 1 not in matrix[_start]:
            print(f"No path exists between {startNode} and {endNode}.")
            exit()
        for i in indexlist(matrix[_start]): #This nest of if structures are pretty much a brute-force. Might not be the best way to write code but still works just fine xd. 
            if i == _end:
                print(f"{startNode} -> {endNode}")
            for j in indexlist(matrix[i]):
                if j == _end:
                    print(f"{startNode} -> {i+1} -> {endNode}")
                for k in indexlist(matrix[j]):
                    if k == _end:
                        print(f"{startNode} -> {i+1} -> {j+1} -> {endNode}")
                    for l in indexlist(matrix[k]):
                        if l == _end:
                            print(f"{startNode} -> {i+1} -> {j+1} -> {k+1} -> {endNode}")
except ValueError as exc1:
    print(exc1)
