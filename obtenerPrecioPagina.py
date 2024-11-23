from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/-/es/ASUS-Port%C3%A1til-juegos-Strix-pantalla/dp/B0CRDCXRK2/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.5b60f7cf-8cdf-42b5-80ee-74f9ab340b5d&dib=eyJ2IjoiMSJ9.2rOL9di6pz9eX8oIJXU9AyKIN6jUYaZRdPZgDNovZ3bS57XIHx_25MqFi-flVml1HbYE5cp4rUAJnOkjKVYh1LDzSYpDiUw3OiYwr-1RLcPPJFdH9dTFqdQYWXcJGg23RbpZ5EFDeuFzZiNYyL-vJHKQcBFqYOtxuLFp2wPqczED3NusjibHDrfTM9AuTHH7zjbMNB-MqpGNO1Kj3KMnPL8NzdFpVxDQQacNgnf7GDSZJeK0n3NIo76FLvuKK89rCjIGco6TZdyGYl5o2G58-AfHLp81p5x-r_FMCPyuvbg.eky0D6rRbumCXMhoNVCPJzeHKUszYbXhi6mQHTC3LNM&dib_tag=se&keywords=gaming&pd_rd_r=f0809da1-cbb6-4a35-a2f3-b36cdfe5db82&pd_rd_w=NsIBv&pd_rd_wg=KLVrj&pf_rd_p=5b60f7cf-8cdf-42b5-80ee-74f9ab340b5d&pf_rd_r=V9QHWSD2FS70KA88KAS3&qid=1732385991&sr=8-1&th=1")
time.sleep(2)

precio = driver.find_element(By.CLASS_NAME,"a-price-whole")
print(precio.text)