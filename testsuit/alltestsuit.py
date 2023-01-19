import unittest
from seleniumpackage.package1.TC_LoginTest import Logintest
from seleniumpackage.package1.TC_SignupTest import signupTest

from seleniumpackage.package2.TC_paymentTest import paymentTest
from seleniumpackage.package2.paymentreturnstest import paymentreturnTest

tc1=unittest.TestLoader().loadTestsFromTestCase(Logintest)
tc2=unittest.TestLoader().loadTestsFromTestCase(signupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(paymentreturnTest)

sanitytestsuit=unittest.TestSuite([tc1,tc2])
functionaltestsuit=unittest.TestSuite([tc3,tc4])
unittest.TextTestRunner().run(functionaltestsuit)
