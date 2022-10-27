import pyautogui #pip install pyautogui
import os
import time

def paste():
    open('doc.txt', 'w').close() # Clears the txt file
    path = "doc.txt"              
    path = os.path.realpath(path)
    os.startfile(path)
    time.sleep(1)                     

    pyautogui.hotkey('ctrl','v')        #paset copied text from clipboard 
    pyautogui.hotkey('ctrl','s')        #save the file
    pyautogui.hotkey('alt','f4')        #close the file and back to program
    
    with open('doc.txt', 'r') as f:
        text = f.read()
    
    return text
paste()