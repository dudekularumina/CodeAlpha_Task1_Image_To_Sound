import pytesseract as pyt
import cv2
from gtts import gTTS
import os

pyt.pytesseract.tesseract_cmd = r"C:\\Program Files\\tesseract.exe"

def convert_to_sound():
    try:
        image = cv2.imread("image.jpg")
        text = pyt.image_to_string(image)
        print(text)
        sound = gTTS(text, lang="en")
        sound.save("sound.mp3")
        os.system("sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while executing code\n", bug)
        return

convert_to_sound()
