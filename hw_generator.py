import itertools
from Bio.Seq import Seq


def generate(n):
    i = 1
    while i <= n:
        for elem in itertools.product('ACGT', repeat=i):
            yield ''.join(list(elem))
        i += 1


def trans(fasta, gene_code="Standard"):
    coding = ''
    with open(fasta) as file:
        rec = file.readline()
        for line in file:
            if line[0] != '>':
                coding += line[:-1]
            else:
                coding_seq = Seq(coding)
                output = rec + str(coding_seq.translate(table=gene_code))
                yield output
                coding = ''
                rec = line
        coding_seq = Seq(coding)
        output = rec + str(coding_seq.translate(table=gene_code))
        yield output


# print(list(generate(2)))

'''for line in trans('reference.fasta'):
    print(line)'''
