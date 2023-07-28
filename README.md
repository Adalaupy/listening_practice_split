## Table of contents
* [General Information](#general-information)
* [Step of using](#step-of-using)
* [Key Introduction](#key-introduction)
* [Installation](#installation)
* [Room for Improvement](#room-for-improvementlimitation)
* [remark](#remark)


# General Information
Listening is important for learning a new language, personally speaking, I like to practice it by my playing video on Youtube and use notepad to mark down what I have listened. But in most case, it's quite hard to follow the speed of the video and forced to drag the mouse pointer from notepad to my browser to press a "stop" button or seek backward, and vice versa to continue. This program is designed for consolidating these several actions into just one step and enhancing your listening practicing efficiency.

# Step of Using
1. Execute main.py
```
python main.py
```
2. Click on any position of your screen to choose the prefered monitor (in case you have more than 1 monitor)
3. A browser and a notepad application will be opened and splited into half automatically
4. Search the video by using the opened browser as usual
5. Press the key on keyboard to run the function

# Key Introduction

**Pause:**
1. Mouse pointer move from notepad to Chrome to activate it
2. Press "space" to stop the video
3. Mouse pointer move back to notepad to continue typing


**Print Screen (for switching active window):**
1. Identify the current active window
2. Move the mouse pointer to activate another one



# Installation
```
pip install -r requirements.txt
```
 

# Room for Improvement/Limitation
- Not allow to resize and move the window manually after opened
- Only available to Google Chrome and Notepad
- Sometimes the window fail to resize in a proper position
- Not available for selecting other keys

# Remark
- User can still change the key in defined function **Pause(monitor_number)** of file **Pause.py** 
```
    stop_key = "pause"
    switch_key = "print screen"
```

