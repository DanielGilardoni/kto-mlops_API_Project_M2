import unittest

NOMBRE_SEUIL = 7

"""
Count names with more than NOMBRE_SEUIL letters
"""
def count_long_names(prenoms: list[str]) -> int:
    more_than_seuil = 0
    for prenom in prenoms:
        if len(prenom) > NOMBRE_SEUIL:
            more_than_seuil += 1
    return more_than_seuil

class TestNamesMethod(unittest.TestCase):
     def test_count_long_names(self):
        prenoms_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seuil = count_long_names(prenoms=prenoms_list)
        self.assertEqual(more_than_seuil, 4)

if __name__ == '__main__':
    unittest.main()