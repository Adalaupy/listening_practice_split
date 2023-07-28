import pyautogui
import keyboard
import win32gui
from screeninfo import get_monitors




# If press stop key, the program will stop the video by pressing "space" on keyboard, then go back to notepad
def on_stop_key(chrome_x,chrome_y,note_x,note_y):



    pyautogui.moveTo(chrome_x,chrome_y)
    pyautogui.click()
    
    keyboard.press("space")
    keyboard.release("space")

    

    # back to notepad
    pyautogui.moveTo(note_x,note_y)
    pyautogui.click()

    
    



# Switch to another window
def on_switch_key(chrome_x,chrome_y,note_x,note_y):


    
    if "Google Chrome" in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        
        Current_wind = 0

    else:

        Current_wind = 1




    if Current_wind == 1:
        pyautogui.moveTo(chrome_x,chrome_y)
        pyautogui.click()


    else:

        pyautogui.moveTo(note_x,note_y)
        pyautogui.click()
 


    


# identify the coordinate of each window, will be used by stop/switch key
def Pause(monitor_number):



    monitor = get_monitors()[monitor_number]
    chrome_x,chrome_y = monitor.x, 0
    note_x,note_y = monitor.x + monitor.width - 10 , 0 

    stop_key = "pause"
    switch_key = "print screen"


    

    keyboard.add_hotkey(stop_key,on_stop_key,args = [chrome_x,chrome_y,note_x,note_y])
    keyboard.add_hotkey(switch_key,on_switch_key, args = [chrome_x,chrome_y,note_x,note_y])

    
    
    
    keyboard.wait("")