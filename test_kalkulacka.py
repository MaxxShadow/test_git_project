
import unittest

import kalkulacka

class TestKalkulacka(unittest.TestCase):
    def setUp(self):
        # Metoda ktera se pusti před každým testem
        self.kalk = kalkulacka.Kalkulacka()

    def test_soucet(self):
        self.assertEqual(self.kalk.soucet(5, 4), 9)
        self.assertEqual(self.kalk.soucet(0, 1), 1)

    def test_rozdil(self):
        self.assertEqual(self.kalk.rozdil(5, 4), 1)
        self.assertEqual(self.kalk.rozdil(0, 1), -1)
        self.assertNotEqual(self.kalk.rozdil(5, 4),self.kalk.rozdil(4, 5))

    def test_soucin(self):
        self.assertEqual(self.kalk.soucin(5, 4), 20)
        self.assertEqual(self.kalk.soucin(0, 1), 0)
        
    def test_podil(self):
        self.assertEqual(self.kalk.podil(8, 4), 2)
        self.assertEqual(self.kalk.podil(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.kalk.podil(5, 0)   


if __name__ == '__main__':
    unittest.main()


