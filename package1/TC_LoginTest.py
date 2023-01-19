import unittest

class Logintest(unittest.TestCase):
    def loginbyEmail(self):
        print("login through maiL")
        self.assertTrue(True)

    def loginbyFacebook(self):
        print("login through facebook")
        self.assertTrue(True)

    def loginbyTwitter(self):
        print("login through twitter")
        self.assertTrue(True)

test1=Logintest()
test1.loginbyEmail()
test1.loginbyFacebook()
test1.loginbyTwitter()
# if __name__== "__main__":
#     unittest.main()