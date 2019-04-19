# Very experimental many changes in code will take place

# plotting linear graphs

# Imported necessary modules and libraries (FINALLY!!!)

import sympy as sy

import matplotlib.pyplot as plt

# Asking for user input to graph

mx = int(input('Enter mx portion of equation: '))
b = int(input('Enter b portion of equation: '))

print("y =", mx + b)

x = [100, 200, 300, 400]
y = [287, 487, 587, 687]

plt.plot(x, y)
plt.show()
