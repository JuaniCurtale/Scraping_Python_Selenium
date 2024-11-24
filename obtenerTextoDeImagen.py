import cv2
import pytesseract

preguntas_final = []#aca irian las imagenes

for i in preguntas_final:
    imagen = cv2.imread(i)
    pytesseract.pytesseract.tesseract_cmd = "ruta"
    texto = pytesseract.image_to_string(imagen)
    print(texto)
    print("")
