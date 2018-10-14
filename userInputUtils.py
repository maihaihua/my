from  pynput import mouse,keyboard
import time

def mouseMove(x,y):
	mouseTarget = mouse.Controller()
	x0,y0 = mouseTarget.position
	print(x0,y0)
	delX = x - x0
	delY = y - y0
	for step in range(5):
		mouseTarget.move(int(delX/5),int(delY/5))
		time.sleep(1)
	mouseTarget.position = (x,y)

def keyboardPress():
	keyboardTarget = keyboard.Controller()
	with keyboardTarget.pressed(keyboard.Key.alt):
		keyboardTarget.press('a')
	keyboardTarget.release(keyboard.Key.ctrl)

def clearPlayers():
	keyboardTarget = keyboard.Controller()
	keyboardTarget.press(keyboard.Key.f9)
	keyboardTarget.release(keyboard.Key.f9)

def clearShops():
	keyboardTarget = keyboard.Controller()
	with keyboardTarget.pressed(keyboard.Key.alt):
		keyboardTarget.press('h')
		keyboardTarget.release('h')
	keyboardTarget.press('h')
	keyboardTarget.release('h')