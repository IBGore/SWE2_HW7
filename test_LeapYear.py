import unittest
import LeapYear as LY

class TestCase(unittest.TestCase):
    #Check if leap year is determined correctly
    def test_IsLeap1(self):
        self.assertEqual(LY.isLeapYear(1), False)

    def test_IsLeap4(self):
        self.assertEqual(LY.isLeapYear(4), True)

    def test_IsLeap100(self):
        self.assertEqual(LY.isLeapYear(100), False)

    def test_IsLeap400(self):
        self.assertEqual(LY.isLeapYear(400), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)