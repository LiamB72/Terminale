# Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

# Generating some sample data with NumPy
x = np.linspace(-100, 100, 500)
                #From To   Samples #

y = 2 * x**2 - 4 * x - 30
# Creating a simple plot with Matplotlib
plt.plot(x, y, label='2x^2 - 4x - 30', color='blue')
plt.title(f"Parabola")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a grid for better visualization (optional)
plt.grid(True)

# Show a legend
plt.legend()

# Show the plot
plt.show()