import win32api, win32con
import math
import time

def movePlayerCharacter(angleToTarget):
    if math.fabs(angleToTarget) < math.pi/5:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 3 * int(math.degrees(angleToTarget)), 0, 0, 0)  # move mouse
        win32api.keybd_event(0x57, 0, 0, 0)  # Press "w" key
    else:
        win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 3 * int(math.degrees(angleToTarget)), 0, 0, 0)  # move mouse
    # press spacebar every few seconds 
    if int(time.time())  % 15 == 0:
        win32api.keybd_event(0x20, 0, 0, 0)  # Press "spacebar" keywwww
        #unpress spacebar
        win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release "spacebar" key
