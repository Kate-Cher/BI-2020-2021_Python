import unittest
from hw_classes import Sequence
from hw_classes import DNA
from hw_classes import RNA


class SequenceTestMethods(unittest.TestCase):

    def setUp(self):
        self.sequence = Sequence("ACGGTC")

    def test_not_str_seq(self):
        s = []
        with self.assertRaisesRegex(TypeError, "Sequence is not a string object"):
            Sequence(s)

    def test_length_seq(self):
        self.assertEqual(len(self.sequence), 6)

    def test_iter(self):
        self.assertEquals([elem for elem in self.sequence], ["A", "C", "G", "G", "T", "C"])

    def test_slice(self):
        self.assertEqual(self.sequence[1:3], "CG")

    def test_equal(self):
        self.assertEqual(self.sequence, Sequence("ACGGTC"))

    def test_case_eq(self):
        self.assertEqual(self.sequence, Sequence("acGGtC"))

    def test_null_gc__content(self):
        seq = Sequence("")
        with self.assertRaisesRegex(ValueError, "The sequence must be al least length 1"):
            seq.gc_content()


class DNATestMethods(unittest.TestCase):

    def setUp(self):
        self.dna1 = DNA("ACGGTA")
        self.dna2 = DNA("AAAAAA")
        self.dna3 = DNA("CCCGGG")

    # Sequence tests
    def test_length_seq(self):
        self.assertEqual(len(self.dna1), 6)

    def test_iter(self):
        self.assertEqual([elem for elem in self.dna1], ["A", "C", "G", "G", "T", "A"])

    def test_slice(self):
        self.assertEqual(self.dna1[1:3], "CG")

    def test_equal(self):
        self.assertEqual(self.dna1, DNA("ACGGTA"))

    def test_case_eq(self):
        self.assertEqual(self.dna1, DNA("acGGtA"))

    def test_type_dna(self):
        self.assertEqual(type(self.dna1), DNA)

    def test_dna_wrong_type(self):
        self.assertRaises(TypeError, self.dna2, RNA("AAAAAA"))

    def test_wrong_alphabet(self):
        with self.assertRaisesRegex(TypeError, "Invalid alphabet. Must be 'A', 'T', 'G', 'C', 'N'"):
            DNA("ooh_my")

    def test_real_str(self):
        self.assertEqual(str(self.dna1), "ACGGTA")

    def test_dna_seq(self):
        self.assertTrue(issubclass(type(self.dna1), Sequence))

    def test_gc_cont(self):
        self.assertEqual(self.dna1.gc_content(), 50)
        self.assertEqual(self.dna2.gc_content(), 0)
        self.assertEqual(self.dna3.gc_content(), 100)

    def test_null_gc(self):
        seq = DNA("")
        with self.assertRaisesRegex(ValueError, "The sequence must be al least length 1"):
            seq.gc_content()

    def test_transcribe(self):
        self.assertEqual(self.dna1.transcribe(), RNA("UACCGU"))
        self.assertEqual(self.dna2.transcribe(), RNA("UUUUUU"))
        self.assertEqual(self.dna3.transcribe(), RNA("CCCGGG"))
        with (self.assertRaises(AttributeError)):
            RNA("UUUUU").transcribe()

    def test_rev_compl(self):
        self.assertEqual(self.dna1.reverse_complement(), DNA("TACCGT"))
        self.assertEqual(DNA("A").reverse_complement(), DNA("T"))
        self.assertEqual(DNA(""), DNA(""))


class RNATestMethods(unittest.TestCase):

    def setUp(self):
        self.rna1 = RNA("AUGCUA")
        self.rna2 = RNA("UUUUUU")
        self.rna3 = RNA("CCCGGG")

    # Sequence tests
    def test_length_seq(self):
        self.assertEqual(len(self.rna1), 6)

    def test_iter(self):
        self.assertEqual([elem for elem in self.rna1], ["A", "U", "G", "C", "U", "A"])

    def test_slice(self):
        self.assertEqual(self.rna1[1:3], "UG")

    def test_equal(self):
        self.assertEqual(self.rna1, RNA("AUGCUA"))

    def test_case_eq(self):
        self.assertEqual(self.rna1, RNA("aUgCuA"))

    def test_type_dna(self):
        self.assertEqual(type(self.rna1), RNA)

    def test_dna_wrong_type(self):
        self.assertRaises(TypeError, self.rna2, RNA("AAAAAA"))

    def test_wrong_alphabet(self):
        with self.assertRaisesRegex(TypeError, "Invalid alphabet. Must be 'A', 'U', 'G', 'C', 'N'"):
            RNA("ooh_my")

    def test_real_str(self):
        self.assertEqual(str(self.rna1), "AUGCUA")

    def test_dna_seq(self):
        self.assertTrue(issubclass(type(self.rna1), Sequence))

    def test_gc_cont(self):
        self.assertEqual(self.rna1.gc_content(), 33.33333333333333)
        self.assertEqual(self.rna2.gc_content(), 0)
        self.assertEqual(self.rna3.gc_content(), 100)

    def test_null_gc(self):
        seq = RNA("")
        with self.assertRaisesRegex(ValueError, "The sequence must be al least length 1"):
            seq.gc_content()

    def test_rev_compl(self):
        self.assertEqual(self.rna1.reverse_complement(), RNA("UAGCAU"))
        self.assertEqual(RNA("U").reverse_complement(), RNA("A"))
        self.assertEqual(RNA(""), RNA(""))


if __name__ == "__main__":
    unittest.main()
