from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Grupo%20Kelsoft/Desktop/primerScraping/formulario.html")
time.sleep(2)

filesheet = "./ejemplo.xlsx"
wb = load_workbook(filesheet)
nombres = wb['Hoja 1'] 
wb.close() #cierro el archivo para seguir


#me recorre las filas de la 1 a la 6(la 7 no la cuenta porque arranque en 1)
for i in range(1,7):
    nomb,apell,edad = nombres[f'A{i}:C{i}'][0] #recorro desde la columna a a la c
    print(nomb.value,apell.value,edad.value)
    driver.find_element(By.ID,"nom").send_keys(nomb.value)
    time.sleep(1)
    driver.find_element(By.ID,"ape").send_keys(apell.value)
    time.sleep(1)
    driver.find_element(By.ID,"edad").send_keys(edad.value)
    time.sleep(1)
    driver.find_element(By.ID,"enviar").click()
    print('Datos enviados ----')
driver.close()