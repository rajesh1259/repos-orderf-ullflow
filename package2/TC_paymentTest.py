import unittest

class paymentTest(unittest.TestCase):
    def paymentbydollar(self):
        print("payment in dollar")
        self.assertTrue(True)

    def paymentbyrupees(self):
        print("payment in rupees")
        self.assertTrue(True)



test4=paymentTest()
test4.paymentbydollar()
test4.paymentbyrupees()

# if __name__== "__main__":
#     unittest.main()