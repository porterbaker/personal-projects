import numpy as np
import math as math
import matplotlib.pyplot as plt
iteration = 1

# Instantiate array and record size/copy for later use

a = np.ones(shape=(1, 1))

# Function to expand the original matrix

def expand_array():
    global a
    previous_array = a
    previous_size = int(math.sqrt(a.size))
    a = np.zeros(shape=((previous_size * 2), (previous_size * 2)))

    count = 1
    while count != 4:
        if count == 1:
            for i in range(previous_size):
                for j in range(previous_size):
                    a[i][j] = previous_array[i][j]
            count = count + 1

        if count == 2:
            for i in range(previous_size):
                for j in range(previous_size):
                    a[i + previous_size][j] = previous_array[i][j]
            count = count + 1

        if count == 3:
            for i in range(previous_size):
                for j in range(previous_size):
                    a[i + previous_size][j + previous_size] = previous_array[i][j]
            count = count + 1

print("Each iteration from the original 1x1 matrix will double the dimensions of the array, thus quadrupuling the overall size.")
print("How many iterations from the original 1x1 matrix would you like?")
iteration = int(input("Please type an integer >= 1: "))

for i in range(iteration):
    expand_array()

plt.imshow(a)
plt.colorbar()
plt.show()

