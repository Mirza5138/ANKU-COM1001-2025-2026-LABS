#Credits to Kerem Gökcek for submitting the solution to the repository.

import random

N = random.randint(3, 5)
print("Randomly selected number of nodes:", N)

matrix = [[] for _ in range(0, N)] #Creates the matrix using nested lists.
for i in range(0, N):
    for n in range(0, N):
        if n > i:
            matrix[i].append(random.randint(0, 1))
        else:
            matrix[i].append(0)

print("Adjacency Matrix:")
[print(node) for node in matrix]

try:
    start_node = int(input("Enter start node (1..{}): ".format(N)))
except ValueError:
    raise TypeError("Start node must be an integer")
if not (1 <= start_node <= N):
    raise ValueError("Start node must be in range of 1 to {}".format(N))

try:
    end_node = int(input("Enter end node (1..{}): ".format(N)))
except ValueError:
    raise TypeError("End node must be an integer")
if not (1 <= end_node <= N):
    raise ValueError("End node must be in range of 1 to {}".format(N))

paths = []
current_path = []
def check_paths(node): #Editor Note: I didn't understand all the steps to this algorithm but you can understand it better using a debugger.
    current_path.append(node)
    for i in range(0, N):
        if matrix[node - 1][i]:
            if i != end_node - 1:
                check_paths(i + 1)
            else:
                current_path.append(end_node)
                paths.append(current_path.copy())
                del current_path[-1]
    del current_path[-1]

check_paths(start_node)

if paths:
    for path in paths:
        print(" -> ".join([str(node) for node in path]))
else:

    print("No paths exist between {} and {}".format(start_node, end_node))
