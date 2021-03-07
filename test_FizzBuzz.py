import unittest
import FizzBuzz as FB


class TestCase(unittest.TestCase):
    def test_fb1(self):
        self.assertEqual(FB.toStr(1), "1")

    def test_fb2(self):
        self.assertEqual(FB.toStr(7), "7")

    def test_fb3(self):
        self.assertEqual(FB.toStr(3), "Fizz")

    def test_fb4(self):
        self.assertEqual(FB.toStr(5), "Buzz")

    def test_fb5(self):
        self.assertEqual(FB.toStr(15), "FizzBuzz")


    



    # def test_fb#(self):
    #     with self.assertRaises(AssertionError):
    #         #function that errors


        

    


if __name__ == '__main__':
    unittest.main(verbosity=2)

