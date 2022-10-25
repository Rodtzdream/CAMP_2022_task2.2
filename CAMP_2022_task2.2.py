from re import L
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import copy


def ChangeStateOfCell(cell, count):
    if (cell == 0 and count == 3):
        return (1)

    if (cell == 1 and (count == 2 or count == 3)):
        return (1)
    else:
        return (0)


def FindNeighbours(matrix, i, j):
    count = 0

    if (matrix[i - 1][j - 1]):
        count += 1
    if (matrix[i - 1][j]):
        count += 1
    if (matrix[i - 1][j + 1]):
        count += 1
    if (matrix[i][j - 1]):
        count += 1
    if (matrix[i][j + 1]):
        count += 1
    if (matrix[i + 1][j - 1]):
        count += 1
    if (matrix[i + 1][j]):
        count += 1
    if (matrix[i + 1][j + 1]):
        count += 1

    return count


print("Enter the size of matrix:")
print("x:")
size_x = int(input())
print("y:")
size_y = int(input())

initial_matrix = [[randint(0, 1) for _ in range(size_x)]
                  for _ in range(size_y)]

modified_matrix = copy.deepcopy(initial_matrix)

# print("\nInitial matrix:")
# for row in initial_matrix:
#     print(row)

plt.title('Initial matrix:', fontweight="bold")
plt.imshow(initial_matrix)
plt.show()

counter_it = 0
while True:
    counter_it += 1

    for i in range(1, size_y - 2):
        count = 0
        for j in range(1, size_x - 2):
            count = FindNeighbours(initial_matrix, i, j)
            modified_matrix[i][j] = ChangeStateOfCell(initial_matrix[i][j], count)

    # print("\nModified matrix(' + str(counter_it) + '):")
    # for row in modified_matrix:
    #     print(row)

    plt.title('Modified matrix(' + str(counter_it) + '):', fontweight="bold")
    plt.imshow(modified_matrix)
    plt.show()

    print("\nContinue? (Enter 0 or 1)")
    cont = int(input())
    if (cont == 0):
        break
    elif (cont == 1):
        initial_matrix = copy.deepcopy(modified_matrix)
    else:
        print("Input error!")
        break
