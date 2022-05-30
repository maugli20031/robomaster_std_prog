import socket
import sys
import time

def move_forwards(x, y, s):
    string = 'chassis move x '+str(x)+' y '+str(y)+';'
    print(string)
    s.send(string.encode('utf-8'))
    status=s.recv(1024)
    time.sleep(1)
    while(status.decode('utf-8')[0] != '1'):
        s.send('chassis status ?;'.encode('utf-8'))
        status=s.recv(1024)
        

def rotate(deg, s):
    check = 'chassis position ?'
    s.send(check.encode('utf-8'))
    status=s.recv(1024)
    print(status.decode('utf-8'))
    string = 'chassis move z '+str(deg)+';'
    s.send(string.encode('utf-8'))

host = "192.168.2.1"
port = 40923
def main ():
    address = (host, int (port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Connecting...") 
    s.connect(address)
    print ("Connected!")
    while True:
        msg = input (">>> please input SDK cmd: ")
        if msg.upper() == 'Q':
            break
        #s.send(msg.encode('utf-8'))
        
        s.send('command;'.encode('utf-8'))
        time.sleep(1)
        move_forwards(1, 0, 0, s)
        move_forwards(0, 0, 180, s)
        move_forwards(1, 0, 0, s)
        """
        s.send('robotic_gripper close 3;'.encode('utf-8'))
        time.sleep(2)
        s.send('robotic_arm moveto x 140 y 140;'.encode('utf-8'))
        time.sleep(3)
        s.send('chassis move x 2;'.encode('utf-8'))
        """
        try:
            buf=s.recv(1024)
            print(buf.decode('utf-8'))
        except socket.error as e:
            print ("Error receiving :", e)
            sys.exit (1)
        if not len(buf):
            break
    s.shutdown(socket.SHUT_VR)
    s.close ()

if __name__ == '__main__':
    main()