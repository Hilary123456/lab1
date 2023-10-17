import numpy as np
import matplotlib.pyplot as plt

# can delete
file_path = "sequence.txt"  # Replace with the actual file path
numbers = []
with open(file_path, "r") as file:
    numbers.append([float(line.strip()) for line in file])
x = np.linspace(start=min(numbers[0]), stop=max(numbers[0]), num=len(numbers[0]))
# print(numbers[0])

# Define the range of x values
x = np.linspace(-10, 10, 500)


'''
file_path = "path/to/your/file.txt"  # Replace with the actual file path

with open(file_path, "r") as file:
    numbers = [int(line.strip()) for line in file]
'''
# Compute the corresponding y values
y = 1 / x

# Plot the graph
plt.plot(x, y)

# Add labels and title
plt.xlabel('x')
plt.ylabel('1/x')
plt.title('Graph of 1/x')

# Display the plot
plt.show()
