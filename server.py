from socket import *
import time
import osascript
from multiprocessing import Process, Manager, Value
import os
#osascript -e 'display notification "{}" with title "{}"'

volume = 0

def recieve_data(val):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind(('', 7777))
    serverSock.listen(1)
    connectionSock, addr = serverSock.accept()
    print("Client address : ", str(addr))
    
    while True:
        print("val : ", val.value)
        try : 
            vol = int(connectionSock.recv(4).decode('utf-8'))
            if vol == 1111:
                print("mute")
                osascript.osascript('set volume output muted TRUE')
                val.value = 0
                while True:
                    vol = int(connectionSock.recv(4).decode('utf-8'))
                    if vol == 2222:
                        osascript.osascript('set volume output muted FALSE')
                        break
                    
            if vol == 3333:
                print("screenshot")
                os.system("screencapture screen.png")
                vol = 0
                
            if vol == 4444:
                print("fix volume")
                osascript.osascript('tell app "System Events" to shut down')
                time.sleep(5)
            if vol < 300:
                val.value = vol
        except:
            pass
        
            
def volume_control(val):
    while True:
        print("volume : ", val.value)
        osascript.osascript("set volume output volume " + str(val.value))
        time.sleep(0.1)
        
if __name__ == '__main__':
    v = Value('i', 0)
    p0 = Process(target = recieve_data, args = (v,))
    p0.start()
    
    p1 = Process(target = volume_control, args = (v,))
    p1.start()
    
    p0.join()
    p1.join()