import unittest

class paymentreturnTest(unittest.TestCase):
    def paymentreturnbydollar(self):
        print("payment in dollar")
        self.assertTrue(True)

    def paymentreturnbyrupees(self):
        print("payment in rupees")
        self.assertTrue(True)



test4=paymentreturnTest()
test4.paymentreturnbydollar()
test4.paymentreturnbyrupees()
# if __name__== "__main__":
#     unittest.main()