import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)
# RGB color as notation 1 means 255
# ax.scatter(x_values, y_values, c=(1, 0, 0), s=10)
# Kind of as thermometer
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.inferno, s=10)

# Set chart title and label axes.
ax.set_title("Squares Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1_100, 0, 1_100_000])

# To show a graph
# plt.show()

# Save to file, a tight bord
plt.savefig('squares_plot.png', bbox_inches='tight')

# Save to file, a large bord, but cut the x label
# plt.savefig('squares_plot2.png')
