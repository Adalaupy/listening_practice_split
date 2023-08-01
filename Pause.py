import pyautogui
import keyboard
import win32gui,win32com.client
from screeninfo import get_monitors
import time

def active_win(wind):


    win32gui.BringWindowToTop(wind)
    win32gui.SetForegroundWindow(wind)        





def on_stop_key(chrome_win,notepad_win):

    active_win(chrome_win)

    

    keyboard.press("space")  
    keyboard.release("space")

    time.sleep(0.1)

    active_win(notepad_win)

    





def on_switch_key(chrome_win,notepad_win):

    
    
    if "Google Chrome" in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
    
        active_win(notepad_win)

    else:

        active_win(chrome_win)





def Pause(chrome_win,notepad_win):
    
    stop_key = "pause"
    switch_key = "print screen"

    

    keyboard.add_hotkey(stop_key,on_stop_key,args = [chrome_win,notepad_win])
    keyboard.add_hotkey(switch_key,on_switch_key, args = [chrome_win,notepad_win])

    
    
    
    keyboard.wait("")


