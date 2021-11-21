import matplotlib as mpl
print(mpl.get_cachedir())
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))

import seaborn as sns
import matplotlib.pyplot as plt
s = np.random.normal(3,40,150)
AA1_plot  = sns.distplot(s, kde=True, rug=False)
plt.show()