import unittest
import pytest
import FizzBuzz as FB

from io import StringIO  # Python 3
import sys



# Replace default stdout (terminal) with our stream



class TestCase(unittest.TestCase):
    #Check correct strings generaged
    def test_Num1(self):
        self.assertEqual(FB.toStr(1), "1")

    def test_Num7(self):
        self.assertEqual(FB.toStr(7), "7")

    def test_Num3(self):
        self.assertEqual(FB.toStr(3), "Fizz")

    def test_Num5(self):
        self.assertEqual(FB.toStr(5), "Buzz")

    def test_Num15(self):
        self.assertEqual(FB.toStr(15), "FizzBuzz")


    #Check correct number of strings printed
    def test_Printed_100_Lines(self):
        # create a temporary stream to hold STDOut
        temp_out = StringIO()

        #redirect stdout (Print statments) to temporary stram
        sys.stdout = temp_out
        
        #run printFizzBuzz to print 100 lines
        FB.printFizzBuzz()

        #check 100 lines have been printed
        self.assertEqual(temp_out.getvalue().count("\n"), 100)

        #restore stdout location
        sys.stdout = sys.__stdout__


    #Check correct strings are printed
    def test_Printed_Num(self):
        # create a temporary stream to hold STDOut
        temp_out = StringIO()

        #redirect stdout (Print statments) to temporary stram
        sys.stdout = temp_out
        
        #run printFizzBuzz to print 100 lines
        FB.printFizzBuzz()

        #creat an array of lines
        lines = temp_out.getvalue().split("\n")

        #check line 1 == "1"
        self.assertEqual(lines[0], "1")

        #restore stdout location
        sys.stdout = sys.__stdout__

    def test_Printed_Fizz(self):
        # create a temporary stream to hold STDOut
        temp_out = StringIO()

        #redirect stdout (Print statments) to temporary stram
        sys.stdout = temp_out
        
        #run printFizzBuzz to print 100 lines
        FB.printFizzBuzz()

        #creat an array of lines
        lines = temp_out.getvalue().split("\n")

        #check line 3 == "Fizz"
        self.assertEqual(lines[2], "Fizz")

        #restore stdout location
        sys.stdout = sys.__stdout__

    def test_Printed_Buzz(self):
        # create a temporary stream to hold STDOut
        temp_out = StringIO()

        #redirect stdout (Print statments) to temporary stram
        sys.stdout = temp_out
        
        #run printFizzBuzz to print 100 lines
        FB.printFizzBuzz()

        #creat an array of lines
        lines = temp_out.getvalue().split("\n")

        #check line 5 == "Buzz"
        self.assertEqual(lines[4], "Buzz")

        #restore stdout location
        sys.stdout = sys.__stdout__

    def test_Printed_FizzBuzz(self):
        # create a temporary stream to hold STDOut
        temp_out = StringIO()

        #redirect stdout (Print statments) to temporary stram
        sys.stdout = temp_out
        
        #run printFizzBuzz to print 100 lines
        FB.printFizzBuzz()

        #creat an array of lines
        lines = temp_out.getvalue().split("\n")

        #check line 15 == "FizzBuzz"
        self.assertEqual(lines[14], "FizzBuzz")

        #restore stdout location
        sys.stdout = sys.__stdout__
    


    
if __name__ == '__main__':
    unittest.main(verbosity=2)

