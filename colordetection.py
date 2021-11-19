import win32gui
from PIL import ImageGrab
import cv2


hwnd = win32gui.FindWindow(None, "Photos")
if hwnd:
	win32gui.SetForegroundWindow(hwnd)
	x, y, x1, y1 = win32gui.GetClientRect(hwnd)
	x, y = win32gui.ClientToScreen(hwnd, (x, y))
	x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))

	image=ImageGrab.grab(bbox=(x,y,x1,y1))
	image.save("temp.png");

	print(image.getpixel((764, 134)))

else:
	print(hwnd)
