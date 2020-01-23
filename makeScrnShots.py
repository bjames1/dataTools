import pickle
import time
import sys
import pyautogui as pag
import keyboard
from pynput.keyboard import Key, Listener

# begin_xy = (99, 134);

path = '/Users/jamesbrown/Desktop/epiStuff/testIms';

def mouse_xy():
    currentMouseX, currentMouseY = pag.position() # Get the XY position of the mouse.
    myVars = currentMouseX, currentMouseY;
    return myVars


def on_release(key):
    if key == Key.shift_r:
        begin_xy = mouse_xy();
        time.sleep(2)
        pag.mouseDown(button='left', x=begin_xy[0], y=begin_xy[1])
        pag.mouseUp(button='left', x=begin_xy[0], y=begin_xy[1])

        for page in range(10):
            time.sleep(2)
            file = '/test' + str(page) + '.png';
            out = path + file;
            im = pag.screenshot(out,region=(678,95, 780, 920))
            time.sleep(2)
            pag.hotkey('down')

    if key == Key.esc:
        return False


with Listener(on_release=on_release) as listener:
    listener.join()
