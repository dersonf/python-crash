import matplotlib.pyplot as plt

x_values = range(5001)
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.winter ,s=10)

# Set chart title and label axes.
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 5_100, 0, 130_000_000_000])

# Show graph
plt.show()
