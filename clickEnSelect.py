import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_main(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        #time.sleep(2)
        select = driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select")
        opcion = select.find_elements(By.TAG_NAME,"option") #guardo los elementos del select
        #time.sleep(3)

        for option in opcion:
            print("Los valores son: %s" % option.get_attribute("value"))
            option.click()
            time.sleep(1)

        seleccionar = Select(driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")    


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
