import keyboard
import pyautogui
import sys
from pynput.keyboard import Key, Listener


def mouse_xy():
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    myVars = currentMouseX, currentMouseY;
    return myVars

def run():
    myVars=mouse_xy()
    print(myVars)

def on_release(key):
    if key == Key.space:
        run()

    if key == Key.esc:
        return False

with Listener(on_release=on_release) as listener:
    listener.join()
