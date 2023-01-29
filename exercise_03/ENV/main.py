import numpy as np

# Generate a list of random numbers
list_random = np.random.uniform(0,1, size=(10))

mean = np.mean(list_random)

median = np.median(list_random)

standard_deviation = np.std(list_random)



print('Random numbers:')
print(list_random)
print('Mean:', mean, 'Median:', median, 'Standard Deviation:', standard_deviation)