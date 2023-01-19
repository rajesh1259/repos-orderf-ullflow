import unittest

class signupTest(unittest.TestCase):
    def signupbyEmail(self):
        print("login through mail")
        self.assertTrue(True)

    def signuobyFacebook(self):
        print("login through facebook")
        self.assertTrue(True)

    def signupbyTwitter(self):
        print("login through twitter")
        self.assertTrue(True)

test2=signupTest()
test2.signupbyEmail()
test2.signuobyFacebook()
test2.signupbyTwitter()
# if __name__== "__main__":
#     unittest.main()