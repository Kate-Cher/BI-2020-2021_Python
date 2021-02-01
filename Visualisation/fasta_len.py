import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Fasta distribution
def fasta_lenghts(fasta_path):
    with open(fasta_path) as fasta:
        all_read_lens = []
        fasta.readline()
        read_length = 0
        for fa_line in fasta:
            if fa_line[0] == '>':
                all_read_lens.append(read_length)
                read_length = 0
            else:
                read_length += len(fa_line[:-1])
    return np.array(all_read_lens)

fasta_path = input("Path to a fasta file: ")
len_distr = fasta_lenghts(fasta_path)
# For testing may try this:
#len_distr = fasta_lenghts("example_ecoli.fasta")
f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.histplot(len_distr, color='teal', kde=True,  bins=30, ax=axs[0])
sns.histplot(len_distr, color='teal', kde=True, bins=30, log_scale=True, ax=axs[1])
axs[0].set_title('Sequence length distribution')
axs[1].set_title('Log scale sequence length distr')
axs[0].set_xlabel('Length')
axs[1].set_xlabel('Length (log)')
f.tight_layout()
plt.show()

