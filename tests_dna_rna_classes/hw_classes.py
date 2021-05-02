class Sequence:
    """DNA or RNA sequence class"""

    def __init__(self, nucl_acid_string: str):
        if isinstance(nucl_acid_string, str):
            self.nucl_acid_string = nucl_acid_string.upper()
        else:
            raise TypeError("Sequence is not a string object")

    def gc_content(self):
        """:returns GC percent"""
        if len(self.nucl_acid_string) == 0:
            raise ValueError("The sequence must be al least length 1")
        return (self.nucl_acid_string.count("G") + self.nucl_acid_string.count("C")) \
               / len(self.nucl_acid_string) * 100

    def reverse_complement(self):
        """:returns reverse complement sequence"""
        rev_comp_sec = ""
        for nucl in self.nucl_acid_string:
            rev_comp_sec += self.comp_nucl[nucl]
        return type(self)(rev_comp_sec[::-1])

    def __iter__(self):
        for elem in self.nucl_acid_string:
            yield elem

    def __eq__(self, other):
        return self.nucl_acid_string == other.nucl_acid_string \
               and other.nucl_acid_string == self.nucl_acid_string

    def __hash__(self):
        return hash(self.nucl_acid_string)

    def __add__(self, other):
        return Sequence(self.nucl_acid_string + other.nucl_acid_string)

    def __repr__(self):
        return f'{type(self).__name__}({self.nucl_acid_string})'

    def __len__(self):
        return len(self.nucl_acid_string)

    def __getitem__(self, slic_e):
        return self.nucl_acid_string[slic_e]

    def __str__(self):
        return self.nucl_acid_string


class DNA(Sequence):
    """DNA sequence"""
    alph = {'A', 'T', 'G', 'C', 'N'}
    comp_nucl = {'A': 'T',
                 'T': 'A',
                 'G': 'C',
                 'C': 'G',
                 'N': 'N'}

    def __init__(self, nucl_acid_string):
        if self.alph >= set(nucl_acid_string.upper()):
            super().__init__(nucl_acid_string)
        else:
            raise TypeError("Invalid alphabet. Must be 'A', 'T', 'G', 'C', 'N'")

    def transcribe(self):
        """
        :return: Transcribed to RNA DNA sequence
        """
        return RNA(self.nucl_acid_string.replace("T", "U")).reverse_complement()


class RNA(Sequence):
    alph = {'A', 'U', 'G', 'C', 'N'}
    comp_nucl = {'A': 'U',
                 'U': 'A',
                 'G': 'C',
                 'C': 'G',
                 'N': 'N'}

    def __init__(self, nucl_acid_string):
        if set(nucl_acid_string.upper()) <= self.alph:
            super().__init__(nucl_acid_string)
        else:
            raise TypeError("Invalid alphabet. Must be 'A', 'U', 'G', 'C', 'N'")


if __name__ == "__main__":
    s = ""
    seq_0 = Sequence(s)
    seq_1 = DNA("G")
    seq_2 = RNA('GCCAU')
    print(RNA("UUUUU").transcribe())
