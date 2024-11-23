import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import cv2 

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_main(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        driver.save_screenshot('img2.png')
        time.sleep(3)

    def test_comparando_imagenes(self):
        img1 = cv2.imread('img1.png')
        img2 = cv2.imread('img2.png')

        
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))  # (ancho, alto)
        diferencia = cv2.absdiff(img1,img2) #comparacion de imagenes
        imagen_gris = cv2.cvtColor(diferencia,cv2.COLOR_BGR2GRAY) #lo pasa a escala de grises
        contours,_ = cv2.findContours(imagen_gris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #declaramos una coleccion de datos

        for c in contours:
            if cv2.contourArea(c) >= 20:
                posicion_x,posicion_y,ancho,alto = cv2.boundingRect(c)
                cv2.rectangle(img1,(posicion_x,posicion_y),(posicion_x+ancho,posicion_y+alto),(0,0,255),2)

        while(1):
            cv2.imshow('Imagen1',img1)
            cv2.imshow('Imagen2',img2)
            cv2.imshow('diferencias detectadas',diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado  == 27:
                break
        cv2.destroyAllWindows()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()