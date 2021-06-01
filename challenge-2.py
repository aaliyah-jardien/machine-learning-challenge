import matplotlib.pyplot as plt
import numpy as np

data = np.array([0.5, 0.7, 1., 1.2, 1.3, 2.1])
bins = [0, 1, 2, 3]

plt.title("Histogram of nums against bins")
plt.hist(data, bins, color="red")
plt.xlabel("Nums")
plt.ylabel("Bins")
plt.show()
