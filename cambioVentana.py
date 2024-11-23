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
        driver.get("https://www.google.com/")
        #time.sleep(2)
        driver.execute_script("window.open('');") #abre una ventana nueva
        #time.sleep(2)
        driver.switch_to.window(driver.window_handles[1]) #salta a la nueva ventana
        #time.sleep(2)
        driver.get("https://stackoverflow.com")
        #time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
