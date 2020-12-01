from dice import Dice

# Create a D6.
dice = Dice()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
