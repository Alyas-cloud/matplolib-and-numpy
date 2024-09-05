import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = np.sin(x)

# 1. Line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='sin(x)', color='b', linewidth=2)
plt.title('Line Plot of sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar chart
categories = ['Category A', 'Category B', 'Category C']
values = [10, 20, 15]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='g')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 3. Scatter plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

plt.figure(figsize=(8, 5))
plt.scatter(x_scatter, y_scatter, color='r')
plt.title('Scatter Plot Example')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

# 4. Histogram
data = np.random.randn(1000)  # 1000 random numbers from normal distribution

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='c', edgecolor='k', alpha=0.7)
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 5. Subplots (multiple plots in one figure)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Top left: Line plot
axs[0, 0].plot(x, y, 'b')
axs[0, 0].set_title('Line Plot')

# Top right: Bar chart
axs[0, 1].bar(categories, values, color='g')
axs[0, 1].set_title('Bar Chart')

# Bottom left: Scatter plot
axs[1, 0].scatter(x_scatter, y_scatter, color='r')
axs[1, 0].set_title('Scatter Plot')

# Bottom right: Histogram
axs[1, 1].hist(data, bins=30, color='c', edgecolor='k')
axs[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()
