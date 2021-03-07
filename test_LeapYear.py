import unittest
import LeapYear as LY

from io import StringIO  # Python 3
import sys

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


    def test_Printed_1(self):
        # create a temporary stream to hold STDOut
        temp_out = StringIO()

        #redirect stdout (Print statments) to temporary stram
        sys.stdout = temp_out
        
        #run printLeapYear
        LY.printIsYear(1)

        #check correct statement printed
        self.assertEqual(temp_out.getvalue(), "1 is not a leap year!\n")

        #restore stdout location
        sys.stdout = sys.__stdout__

    def test_Printed_4(self):
        # create a temporary stream to hold STDOut
        temp_out = StringIO()

        #redirect stdout (Print statments) to temporary stram
        sys.stdout = temp_out
        
        #run printLeapYear
        LY.printIsYear(4)

        #check correct statement printed
        self.assertEqual(temp_out.getvalue(), "4 is a leap year!\n")

        #restore stdout location
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main(verbosity=2)