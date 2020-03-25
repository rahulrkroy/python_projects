#Note - set this to launch at startup using sudo crontab -e, then write @reboot python3 file/path/website_blocker.py in linux  or mac
# or using windows task manager and set to launch as admin using highest priority
import os
import time

# hostsPath=r'/home/shikari/hosts'
hostsPath=r'/etc/hosts' 
redirect='127.0.0.1'
sitesList=['www.facebook.com','facebook.com','www.youtube.com','www.fb.com','youtube.com']

startTime=(9,00)
endTime=(17,00)
flag1=True
flag2=True

while(True):
    if time.localtime()[3:5]<endTime and time.localtime()[3:5]>startTime:
        if flag1:
            #this means we are in working hours
            flag1=False
            flag2=True
            print("Work hours")
            print(time.localtime()[3:5])
            with open(hostsPath,'r+') as file:
                content=file.read()

                for site in sitesList:
                    if site in content:
                        pass
                    else:
                        file.write(redirect+' '+site+'\n')  
    else:
        if flag2:
            flag1=True
            flag2=False
            print("Fun hours")
            with open(hostsPath,'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(site in line for site in sitesList):
                        file.write(line) 
                file.truncate()
    time.sleep(60)
