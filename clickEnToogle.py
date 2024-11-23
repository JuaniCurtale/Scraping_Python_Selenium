import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_main(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(2)
        toogle = driver.find_element(By.XPATH,"//*[@id='main']/label[3]/div")
        toogle.click()
        time.sleep(1)
        toogle.click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
