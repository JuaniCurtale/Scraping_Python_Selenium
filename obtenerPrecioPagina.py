from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("url")
time.sleep(2)

precio = driver.find_element(By.CLASS_NAME,"a-price-whole")
print(precio.text)