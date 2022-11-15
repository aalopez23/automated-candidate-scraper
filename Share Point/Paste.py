import pyautogui #pip install pyautogui
import os
import time
import codecs 

def paste():
    open('doc.txt', 'w').close() # Clears the txt file
    path = "doc.txt"              
    path = os.path.realpath(path)
    os.startfile(path)
    time.sleep(1)                     

    pyautogui.hotkey('ctrl','v')        #paste copied text from clipboard 
    pyautogui.hotkey('ctrl','s')        #save the file
    pyautogui.hotkey('alt','f4')        #close the file and back to program
    
    with codecs.open('doc.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
    #try:
    #    with codecs.open('doc.txt', 'r', encoding = 'utf-8') as f:
    #        text = f.read()
    #except:
    #    text = 'ERROR'
        
    return text