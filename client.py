# -*- coding: utf-8 -*-
 
import socket
import threading

 
 
inString = ''
outString = ''
 
def DealOut(s):
    global outString
    outString = '\x01\x05\x00\x01\xFF\x00\xDD\xFA'
    s.send(outString)
 
def DealIn(s):
    global inString
    while True:
        try:
            inString = s.recv(1024)
            if not inString:
                break
            if outString != inString:
                print inString
        except:
            break

ip = '192.168.1.2'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, 40000))
 
thin = threading.Thread(target = DealIn, args = (sock,))
thin.start()
thout = threading.Thread(target = DealOut, args = (sock,))
thout.start()
 
#sock.close()