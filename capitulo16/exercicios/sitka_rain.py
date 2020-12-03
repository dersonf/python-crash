import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '../data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get dates, high and low temperatures from this file.
    # Create two empty lists
    # dates, highs, lows  = [], [], []
    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])
        # low = int(row[6])
        dates.append(current_date)
        # highs.append(high)
        # lows.append(low)
        rainfalls.append(rainfall)

# print(highs)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
# alpha make a shade
# ax.plot(dates, highs, c='red', alpha=0.5)
# ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, rainfalls, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily rainfall - 2018", fontsize=24)
# Change just the font size
plt.xlabel('', fontsize=16)
# Draw labels diagonally
fig.autofmt_xdate()
plt.ylabel("Amount of rainfall", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
