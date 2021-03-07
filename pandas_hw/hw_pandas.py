import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv("train.csv")
# Selecting columns and rows (> mean)
df1 = df.loc[df['matches'] > np.mean(df['matches'])]
df1 = df1[['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']]
print(df1.head())
print(f'mean value of matches is {np.mean(df["matches"])}')

# Stacked bar plot
df.index = df.pos
df[['A', 'T', 'G', 'C']].plot(kind='bar', stacked=True)
plt.title('Stacked barplot')
plt.xlabel('Position')
plt.ylabel('Nucleotide frequency')
plt.show()

