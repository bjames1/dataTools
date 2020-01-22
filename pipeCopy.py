import pickle
import time
import sys
import pyautogui as pag
import clipboard
import keyboard
from pynput.keyboard import Key, Listener

def mouse_xy():
    currentMouseX, currentMouseY = pag.position() # Get the XY position of the mouse.
    myVars = currentMouseX, currentMouseY;
    return myVars


def setDest():
    setDestination=mouse_xy()
    filename = 'setDestination'
    outfile = open(filename,'wb')
    pickle.dump(setDestination,outfile)
    outfile.close()


def pipePaste():
    sourceDestination = pag.position()
    filename = 'sourceDestination'
    outfile = open(filename,'wb')
    pickle.dump(sourceDestination,outfile)
    outfile.close()

    filename = 'setDestination'
    infile = open(filename,'rb')
    setDestination = pickle.load(infile)
    infile.close()

    time.sleep(.01)
    pag.mouseDown(button='left', x=setDestination[0], y=setDestination[1])
    pag.mouseUp(button='left', x=setDestination[0], y=setDestination[1])

    time.sleep(.01)
    pag.hotkey('command', 'v')

    time.sleep(.01)
    filename = 'sourceDestination'
    infile = open(filename,'rb')
    sourceDestination = pickle.load(infile)
    infile.close()

    pag.moveTo(sourceDestination[0], sourceDestination[1])

def on_release(key):

    if key == Key.shift_l:
        time.sleep(.01)
        setDest()

        time.sleep(.01)
        pag.mouseDown(button='left')
        pag.mouseUp(button='left')

        time.sleep(.01)
        pag.hotkey('command', 'a')

        time.sleep(.01)
        pag.hotkey('delete')

    if key == Key.shift_r:
        time.sleep(.01)
        pag.click(button='left', clicks=3, interval=0.10)

        time.sleep(.01)
        pag.hotkey('command', 'c')
        pipePaste()

    if key == Key.esc:
        return False

with Listener(on_release=on_release) as listener:
    listener.join()
