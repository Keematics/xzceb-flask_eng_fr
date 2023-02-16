import unittest
class TestAdd(unittest.TestCase):
    """ Test case for translating language """
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # translates and outputs 'Bonjour' to 'Hello'
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # translates and outputs 'Hello' to 'Bonjour'
        self.assertIsNone(french_to_english('')) # bool : True if no parameter is added
        self.assertIsNone(english_to_french(''))  # bool : True if no parameter is added
if __name__ == '__main__':
    unittest.main()
    