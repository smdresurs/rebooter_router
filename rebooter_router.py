import sys
import telnetlib
import time
import subprocess


def rebootroter():
    import time
    HOST = "192.168.100.1"
    tn = telnetlib.Telnet(HOST)
    time.sleep(1)
    tn.write(b"reboot\n")
    time.sleep(1)
    tn.close()
    print("Reboot comand was send to "+HOST)




for ping in range(1):
    address = "8.8.8.8"
    res = subprocess.call(['ping', '-c', '6', address])
    if res == 0:
        print ("ping to", address, "OK")
    elif res == 2:
        print ("no response from", address)
    else:
        print ("ping to", address, "failed!")
        print("Start rebooter function")
        rebootroter()
        time.sleep(5)#Задержка на прогрузку
        print("Send mail")
