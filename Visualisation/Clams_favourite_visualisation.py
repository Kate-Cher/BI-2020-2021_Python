# It is convenient to be able to quickly evaluate the
# dependencies between vars in a big data frame.
# So here is an example of visualising such dependencies
# in data frame with different clam's parameters.
# Data from 1st R project.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Ivanov.csv', sep=',')
df = df.drop(df.columns[[5, 6, 7, 8]], axis=1)
g = sns.PairGrid(df, hue="Sex")
g.map_upper(sns.scatterplot)
g.map_lower(sns.scatterplot)
g.map_diag(sns.kdeplot, lw=3, legend=False, shade=True)
plt.suptitle("Clam's parameters")
g.add_legend(title='Sex', loc="center right", labels=['uvenil', 'male', 'female'])
plt.show()
plt.savefig("Clams.png")