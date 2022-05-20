import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('null'),'Null')
    def test2(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('null'),'Null')
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()