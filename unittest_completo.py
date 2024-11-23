import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_main(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        input_username = driver.find_element(By.NAME, "q")  # Usar NAME en lugar de ID
        input_username.send_keys("Escribiendo algo...")
        input_username.send_keys(Keys.ENTER)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

