import socket
import threading
import os
import ioope
import fail

host = '169.254.0.1'
port = 23
i = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print('Connection Build')
a=0
while a<3:
    s.settimeout(5)
    try:
        with open('receive_file.txt', 'ab') as f:
            s.send(bytes("TR", "utf_8"))
            data = s.recv(100)
            print("data = ",data)
            f.write(data)
            if len(data) is 5:
                i = i + 1
                s.send(bytes("GI8000", "utf_8"))
                with open('Receive_image.bmp', 'wb') as ff:
                    s.settimeout(0.100)
                    while True:
                        try:
                            data = bytes(s.recv(10240))
                            ff.write(data)
                        except socket.timeout:
                            ff.close()
                            threading.Thread(target=fail.fail_image, args=(i,)).start()
                            break
                #threading.Thread(target=fail.fail_image, args=(i,)).start()

            f.close()
    except socket.timeout:
        break
    except ConnectionResetError:
        break
    a=a+1
dat =  open('receive_file.txt').read()
dat = "\n".join(dat.split(':'))
outF = open('ReceiveFile.txt','w')
outF.write(dat)
outF.close()
ioope.conv()
os.remove('receive_file.txt')
s.close()