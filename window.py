import win32gui,win32com.client,win32con,win32api
import subprocess
from screeninfo import get_monitors
import time



# Minimize all opened window 
def mini_window():

    windows = []
    win32gui.EnumWindows(lambda hwnd,windows: windows.append(hwnd) , windows )


    for hwnd in windows:

        if win32gui.IsWindowVisible(hwnd)  :

            window_title = win32gui.GetWindowText(hwnd)
            
            if window_title !='':                

                win32gui.ShowWindow(hwnd,win32con.SW_SHOWMINNOACTIVE)





# Find the coordinate of all monitor in case more than 1 monitor
def Monitor():

    global Mon_List
    
    Mon_List = []
    mons = get_monitors()



    for i in range(len(mons)):

        mon_x_start,mon_y_start,mon_x_end,mon_y_end = mons[i].x, mons[i].y ,mons[i].x + mons[i].width , mons[i].y + mons[i].height

        Mon_List.append((mon_x_start,mon_y_start,mon_x_end,mon_y_end))







# Find the position where User click on and identify which monitor
def which_monitor(x,y):

    for i in range(len(Mon_List)):

        if Mon_List[i][0] <= x <= Mon_List[i][2]:

            break

    return i





# Find the corresponding coordinates for spliting windows
def split_coord(x,y):

  
        monitors_list = win32api.EnumDisplayMonitors()


        monitor_number = which_monitor(x,y)
        required_monitor = monitors_list[monitor_number][2]

        new_x = required_monitor[0]
        new_y = required_monitor[1]



        new_width = int((required_monitor[2] - required_monitor[0])/2)
        new_height = required_monitor[3] - required_monitor[1]

              

        left = (new_x, new_y, new_width, new_height)
        right = (new_width + new_x, new_y, new_width, new_height)

        
        
        return left,right,monitor_number





# Open notepad + google chrome
def open_win(Win_Title):


    if Win_Title == "notepad":   


        subprocess.Popen('notepad.exe')

        
        
        hwnd = 0

        while hwnd == 0 or win32gui.GetWindowText(hwnd) == "":
            
            hwnd = win32gui.FindWindow('Notepad', None)



        win32gui.BringWindowToTop(hwnd)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hwnd)

               


    
    elif Win_Title == "googlechrome":
    
        subprocess.Popen("start chrome", shell=True)





# After open chrome + notepad, split them into half
def open_size_win(Win_Title,move_win):

    
    Init_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    Not_opened = True
    
    
    open_win(Win_Title)

    time.sleep(0.5)

    while Not_opened:

        Curr_window = win32gui.GetForegroundWindow()
        Curr_window_title = win32gui.GetWindowText(Curr_window)


        if Curr_window_title != Init_window_title:            

            Not_opened = False 

            win32gui.MoveWindow(Curr_window, move_win[0], move_win[1], move_win[2], move_win[3]  , True)
            


