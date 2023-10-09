import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for x
x = np.linspace(-2, 2, 400)

# Calculate corresponding y values using the heart equation for the upper half
y1 = np.sqrt(1 - (abs(x) - 1) ** 2)

# Calculate corresponding y values using the heart equation for the lower half
y2 = -3 * np.sqrt(1 - (abs(x) / 2) ** 0.5)

# Create the plot
plt.figure(figsize=(6, 6))

# Plot the upper half in the first quadrant
plt.plot(x, y1, 'r')

# Plot the lower half in the fourth quadrant
plt.plot(x, y2, 'r')

# Reflect the upper and lower halves in the second and third quadrants
plt.plot(-x, y1, 'r')
plt.plot(-x, y2, 'r')

# Set plot limits and labels
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.xlabel("x")
plt.ylabel("y")

# Title
plt.title("Descartes Heart Equation in Four Quadrants")

# Show the plot
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()

