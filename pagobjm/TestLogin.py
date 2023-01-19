class testLogin():
    inp_varb="//*[@id='Email address / mobile ']"
    inp_varc="password"
    inp_clk="//*[@id='sign-in-btn']/span[1]"

    def __init__(self,driver):
        self.driver=driver

    def test_username(self,username):
        self.driver.find_element(By.XPATH,inp_varb)

    def test_password(self,password):
        self.driver.find_element(By.ID,inp_varc)

    def test_clk(self):
        self.driver.find_element(By.XPATH)


