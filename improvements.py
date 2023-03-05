import cv2
import numpy as np
from PIL import ImageGrab
from PIL import Image
import win32gui
import win32com.client as comclt
import keyboard as kb
import time
import mss
from pynput.keyboard import Key, Controller
from multiprocessing import Process
from twilio.rest import Client
from threading import Thread

keyboard = Controller()

client = Client(twilio_sid,twilio_auth)
msg = 'Shiny celebi has been found!'

lower_green = np.array([80,248,0], dtype="uint8")
upper_green = np.array([82,240,0], dtype="uint8")

lower_gray = np.array([57,57,57], dtype="uint8")
upper_gray = np.array([57,57,57], dtype="uint8")

lower_gray = np.array([57,57,57], dtype="uint8")
upper_gray = np.array([57,57,57], dtype="uint8")

def up():
	keyboard.press('w')
	time.sleep(.075)
	keyboard.release('w')

def down():
	keyboard.press('s')
	time.sleep(.075)
	keyboard.release('s')

def left():
	keyboard.press('a')
	time.sleep(.075)
	keyboard.release('a')

def right():
	keyboard.press('d')
	time.sleep(.075)
	keyboard.release('d')

def pressA():
	keyboard.press('x')
	time.sleep(.075)
	keyboard.release('x')

def pressB():
	keyboard.press('z')
	time.sleep(.075)
	keyboard.release('z')

def runAway():
	time.sleep(3)
	pressA()
	time.sleep(6)
	right()
	time.sleep(.75)
	down()
	time.sleep(.75)
	pressA()
	time.sleep(.75)
	pressA()
	time.sleep(3)
	pressA()
	time.sleep(5)
	pressA()
	time.sleep(.75)
	left()
	time.sleep(.75)
	left()
	time.sleep(.75)
	left()
	time.sleep(.75)
	left()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	left()
	time.sleep(.75)
	left()
	time.sleep(.75)
	left()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(.75)
	down()
	time.sleep(5)
	main()

def getDimensions():
	

	hwnd = win32gui.FindWindow(None, "mGBA - Pokemon - Emerald Version (USA, Europe) - 0.10.1")
	if hwnd:
		x, y, x1, y1 = win32gui.GetClientRect(hwnd)
		x, y = win32gui.ClientToScreen(hwnd, (x, y))
		x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))

		dimensions = {
			'left': x,
			'top': y + 21,
			'width': x1,
			'height': y1 - 21
		}

		return dimensions
	else:
		print('Window not found!')
		exit()

def processFrames():
	sct = mss.mss()
	pokemonFound = False

	while True:
		encounter_img = np.array(sct.grab(getDimensions()))

		

		pokemon_img = cv2.imread("images/mew.png", cv2.IMREAD_UNCHANGED)
		pokemon_img_gray = cv2.cvtColor(pokemon_img, cv2.COLOR_RGB2GRAY)
		encounter_img_gray = cv2.cvtColor(encounter_img, cv2.COLOR_RGB2GRAY)

		pokemon_canny = cv2.Canny(pokemon_img_gray, 100, 200)
		encounter_canny = cv2.Canny(encounter_img_gray, 100, 200)

		threshold = .3

		result = cv2.matchTemplate(encounter_canny, pokemon_canny, cv2.TM_CCOEFF_NORMED)

		cv2.imshow('Bot Brain', result)
		cv2.waitKey(1)

		yLoc, xLoc = np.where(result >= threshold)

		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

		poke_width = pokemon_img.shape[1]
		poke_height = pokemon_img.shape[0]

		if (len(xLoc) > 0):
			(w, h), _ = cv2.getTextSize('Mew ' + str(round((max_val * 100), 2)) + '%', cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
			detect = cv2.rectangle(encounter_img, (xLoc[0], yLoc[0] - 20), (xLoc[0] + w, yLoc[0]), (0,0,255), -1)
			detect = cv2.rectangle(encounter_img, (xLoc[0], yLoc[0]), (xLoc[0] + poke_width, yLoc[0] + poke_height), (0,0,255), 2)

			cv2.putText(detect, 'Mew ' + str(round((max_val * 100), 2)) + '%', (xLoc[0], yLoc[0] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)

		cv2.imshow('Bot Vision', encounter_img)
		cv2.waitKey(1)

		if (len(xLoc) > 0):

			pokemonFound = True

			encounter_img_RGB = encounter_img[:,:,:3]

			bColor, gColor, rColor = encounter_img_RGB[(190, 520)]

			rgbColor = '(' + str(rColor) + ', ' + str(gColor) + ', ' + str(bColor) + ')'
			# print(rgbColor)

			if (pokemonFound == True and max_val > .9 and rgbColor != '(181, 148, 148)' and rgbColor != '(255, 255, 255)' and rgbColor != '(156, 132, 132)' and rgbColor != '(231, 181, 181)' and rgbColor != '(206, 165, 165)'):
				pokemonFound = False
				thread = Thread(target=catch)
				thread.start

def SR():
    keyboard.press('x')
    keyboard.press('z')
    keyboard.press(Key.enter)
    keyboard.press(Key.backspace)
    time.sleep(.1)
    keyboard.release('x')
    keyboard.release('z')
    keyboard.release(Key.enter)
    keyboard.release(Key.backspace)

    time.sleep(1)

    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press('w')
    time.sleep(1)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release('w')

def catch():
    keyboard.press('x')
    time.sleep(.25)
    keyboard.release('x')
    time.sleep(.25)

    time.sleep(5)

    keyboard.press('s')
    time.sleep(.25)
    keyboard.release('s')
    time.sleep(.25)

    keyboard.press('x')
    time.sleep(.25)
    keyboard.release('x')
    time.sleep(.5)

    keyboard.press('d')
    time.sleep(.25)
    keyboard.release('d')
    time.sleep(.25)

    count = 0

    while count < 4:
        keyboard.press('s')
        time.sleep(.25)
        keyboard.release('s')
        time.sleep(.25)

        count += 1

    keyboard.press('x')
    time.sleep(.25)
    keyboard.release('x')
    time.sleep(.25)

    keyboard.press('x')
    time.sleep(.25)
    keyboard.release('x')
    time.sleep(.25)

def encounter():
	up()
	time.sleep(.75)
	up()
	time.sleep(4)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	right()
	time.sleep(.75)
	right()
	time.sleep(.75)
	right()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	up()
	time.sleep(.75)
	right()
	time.sleep(.75)
	right()
	time.sleep(.75)
	right()
	time.sleep(.75)
	right()
	time.sleep(.75)
	up()
	time.sleep(.75)
	pressA()
	time.sleep(.75)

def main():
	time.sleep(3)
	encounter()
	time.sleep(7)
	runAway()

hwnd = win32gui.FindWindow(None, "mGBA - Pokemon - Emerald Version (USA, Europe) - 0.10.1")
if hwnd:
	win32gui.SetForegroundWindow(hwnd)

thread = Thread(target=processFrames)
thread.daemon = True
thread.start()
time.sleep(3)
main()