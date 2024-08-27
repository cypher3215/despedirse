import pywhatkit as kit
import time
import pyautogui
import keyboard

center_x = 434
center_y = 278

box_width = 200
box_height = 150

left = center_x - (box_width // 2)
top = center_y - (box_height // 2)

region = (left, top, box_width, box_height)


while True:
    time.sleep(10)
    pyautogui.moveTo(x=420, y=278)
    pyautogui.click()
    pyautogui.write("Usuario se encuentra deshabilitado. Si de verdad te importa hablar con él, búscalo en Instagram "
                 "https://www.instagram.com/_________king_______dark______/ Si de verdad no te importa esta persona, por favor "
                 "evitar todo contacto con él. Recuerda que yo soy un bot y por lo tanto borraré este chat en 10 segundos para "
                 "que mi creador no tenga que lidiar con ningún tipo de estrés por responder mensajes de este tipo.")
    keyboard.press('enter')
    time.sleep(0.2)
    keyboard.release('enter')
    pyautogui.moveTo(x=434, y=286)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(x=480, y=401)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x=837, y=451)
    time.sleep(1)
    pyautogui.click()
