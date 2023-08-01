from pynput import mouse
from window import *
from Pause import *



def on_click(x, y, button, pressed):

    global left
    global right
    global monitor_number


    

    mouse_listener.stop()

    if button == mouse.Button.left and pressed:
       
        left,right,monitor_number = split_coord(x,y)






if __name__ == "__main__":
    
    Monitor()
    mini_window()

    with mouse.Listener(on_click=on_click) as mouse_listener:

        mouse_listener.join()       
        
        
        chrome_win = open_size_win("googlechrome",left)
        notepad_win = open_size_win("notepad",right)
        
    
        #Pause(monitor_number)

        Pause(chrome_win,notepad_win)

    

        
