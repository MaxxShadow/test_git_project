import unittest

from utils import TemperatureConverter, StringUtils

class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        # Metoda ktera se pusti před každým testem
        self.tc = TemperatureConverter()
        pass
   
    def test_TemperatureConverter(self):
         # F-C C-F čísla
        self.assertEqual(self.tc.c_to_f(0), 32)
        self.assertEqual(self.tc.f_to_c(32), 0)
        self.assertEqual(self.tc.c_to_f(100), 212)
        self.assertEqual(self.tc.f_to_c(212), 100)
        # desetinná čísla, vyjímky na ne-čísla
        #self.assertEqual(self.tc.c_to_f(37.5), 99.5)
        self.assertAlmostEqual(self.tc.c_to_f(37.5), 99.5, places=1)
        self.assertEqual(self.tc.f_to_c(99.5), 37.5)
        pass

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        # Metoda ktera se pusti před každým testem
        self.su = StringUtils()
        pass
    
    def test_StringUtils(self):
        # revers rovnost stringů vyjímky, palindrom true/false vyjímky
        self.assertEqual(self.su.reverse("hello"), "olleh")
        self.assertEqual(self.su.reverse("12345"), "54321")
        self.assertNotEqual(self.su.reverse("hello"), "hello")
        self.assertEqual(self.su.reverse(""), "")
        self.assertTrue(self.su.is_palindrome("racecar"))
        self.assertTrue(self.su.is_palindrome("madam"))
        self.assertFalse(self.su.is_palindrome("hello"))
        self.assertFalse(self.su.is_palindrome("world"))
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)