import unittest

from lab6.lvl3.src.KMP_alg import kmp


class KmpTest(unittest.TestCase):
    def test_full_match(self):
        self.assertEqual(
            kmp("aaaaaaaaaaaaaaa", "aaa"), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        )

    def test_no_match(self):
        self.assertEqual(kmp("aaaaaaa", "bbbb"), [])

    def test_few_match(self):
        self.assertEqual(kmp("abrakadabraabra", "abra"), [0, 7, 11])
