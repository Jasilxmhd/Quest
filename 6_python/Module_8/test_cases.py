
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
# from calculataion import division




# class jasil(unittest.TestCase):
    
#     def test_division(self):

#        with self.assertRaisest(ZeroDivisionError):
#            division(10,0)

# unittest.main()









'................................................................................'




def get_data():
    None


"""assertTrue   | assertFalse | assertIn  | assertNotIn"""


class TestLetters(unittest.TestCase):
    def test_uppercase(self):
        self.assertTrue("PYTHON".isupper())
        
        
    def test_lower(self):
        self.assertFalse("python".isupper())
        
        
    def test_mebershop(self):
        fruits = ['apple','banana','orange']
        self.assertIn("apple",fruits)
          
    def test_mebershop2(self):
        fruits = ['apple','banana','orange']
        self.assertNotIn("mango",fruits)
        
        
    def test_none(self):
        self.assertIsNone(get_data())
    
    def test_is(self):
        a=[1,2] 
        b=a
        self.assertIs(a,b)       
        
         
        
    def test_is(self):
        self.assertAlmostEqual(20/3,6.66667,places=3)        
        
        
unittest.main()