
# import unittest

# from calculataion import add
# from calculataion import reverse
# from calculataion import number



# class jasil(unittest.TestCase):
#     def test_addPositiveNumber(self):
#         self.assertEqual(add(20,5), 25)


#     # def test_addNegativeBumber(self):
#     #     self.assertEqual(add(-20,-8), -28)

    
#     def test_reverseString(self):
#         self.assertEqual(reverse("jasil"), "lisaj")
        



#     def test_reverseNumber(self):
#         self.assertEqual(number(123), 321)







#     def test_reversnegative(self):
#         self.assertEqual(number(-123), -321)





# unittest.main()


'...............................................'

import unittest
from calculataion import division




class jasil(unittest.TestCase):
    
    def test_division(self):

       with self.assertRaisest(ZeroDivisionError):
           division(10,0)

unittest.main()

