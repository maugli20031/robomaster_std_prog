import socket
import sys
import time

#function takes float value of movement on x axis and y axis in METERS
#(haven't tested, but in docs -5 < x < 5 and -5 < y < 5 as well)
#and connection socket(just type 's' as second argument)
def directional_movement(x, y, s):
    string = 'chassis move x '+str(x)+' y '+str(y)+';'
    s.send(string.encode('utf-8'))
    status=s.recv(1024)
    while(status.decode('utf-8')[0] != '1'):
        s.send('chassis status ?;'.encode('utf-8'))
        status=s.recv(1024)
        time.sleep(0.5)
        
#function takes degree of robot rotation(from -1800 = 5 full rotations to 1800)
#and connection socket(just type 's' as second argument)
def rotation(deg, s):
    #check = 'chassis position ?'
    #s.send(check.encode('utf-8'))
    status=s.recv(1024)
    print(status.decode('utf-8'))
    string = 'chassis move z '+str(deg)+';'
    s.send(string.encode('utf-8'))
    time.sleep(2)#have to think about rotation time-out. Code from directional_movement doesn't work
                 #'cause rotation doesn't change the status of chassis to 'not static'
                 #maybe use 'chassis chassis attitude https://robomaster-dev.readthedocs.io/en/latest/text_sdk/protocol_api.html#chassis-control
                 #and compare the 'before rotation' status and the 'after rotation' status

#Here you can write your algorithm to run on robot
def program():
    pass

#Do not change anything here if you dont know what you are doing.
host = "192.168.2.1"
port = 40923
def main ():
    address = (host, int (port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Connecting...") 
    s.connect(address)
    s.send('command;'.encode('utf-8'))
    time.sleep(1)
    print ("Connected!")
    msg = input (">>> please input 'S' to start program: ")
    if msg.upper() == 'S':
        program()
    s.shutdown(socket.SHUT_VR)
    s.close ()

if __name__ == '__main__':
    main()