import cv2
import numpy as np
from PIL import ImageGrab
from PIL import Image
import win32gui

encounter_img = cv2.imread("images/gamecap.png", cv2.IMREAD_UNCHANGED)
celebi_img = cv2.imread("images/celebi2.png", cv2.IMREAD_UNCHANGED)

celebi_img_gray = cv2.cvtColor(celebi_img, cv2.COLOR_RGB2GRAY)
encounter_img_gray = cv2.cvtColor(encounter_img, cv2.COLOR_RGB2GRAY)

celebi_canny = cv2.Canny(celebi_img_gray, 100, 200)
encounter_canny = cv2.Canny(encounter_img_gray, 100, 200)

cv2.imshow('Celebi Edge', celebi_img_gray)
cv2.imshow('Encounter Edge', encounter_img_gray)

cv2.imshow('Celebi BW', celebi_canny)
cv2.imshow('Encounter BW', encounter_canny)

threshold = .9

print(encounter_img.shape)
print(celebi_img.shape)

cv2.imshow('Celebi', celebi_img)

result = cv2.matchTemplate(encounter_canny, celebi_canny, cv2.TM_CCOEFF_NORMED)

yLoc, xLoc = np.where(result >= threshold)

if (len(xLoc) > 0):

	bColor, gColor, rColor = encounter_img[(114, 294)]

	rgbColor = '(' + str(rColor) + ', ' + str(gColor) + ', ' + str(bColor) + ')'
	print(rgbColor)

	cv2.imshow('Result', result)

	if (rgbColor == '(248, 120, 120)'):
		print('shiny found!')

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

	print("minimum value: " + str(min_val))
	print("maximum value: " + str(max_val))

	print("minimum location: " + str(min_loc))
	print("maximum location: " + str(max_loc))

	poke_width = celebi_img.shape[1]
	poke_height = celebi_img.shape[0]

	cv2.rectangle(encounter_img, (xLoc[0], yLoc[0]), (xLoc[0] + poke_width, yLoc[0] + poke_height), (0,255,0), 2)

cv2.imshow('Encounter', encounter_img)

cv2.waitKey()
