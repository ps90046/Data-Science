import numpy as np
a = np.random.randn(100)
N = 1000
idx = np.random.randint(0,a.size,(N,a.size))
means = a[idx].mean(axis=1)
confint = np.percentile(means, [2.5,7.5])
print(confint)