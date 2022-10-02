import os
import socket



def main():
    
    lhost ='0.0.0.0'
    lport = 9999
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((lhost, lport))
        server.listen(1)
        print(f"Waiting for a connection on {lhost}:{lport}")
        client, addr = server.accept()
    except KeyboardInterrupt:
        print("   See yaa")
        quit()
    except:
        print("Could not socket for some reason")
        quit()    

    
    cnx = client.recv(1024).decode()
    print(cnx)
    
    def taichou():
        try:
            while True:
                
                cmd= input("have_fun_$ ")
                
                if cmd == '':
                    continue
                if cmd == 'clear':
                    os.system("clear")
                    continue
                if cmd == 'exit':
                    exit()
                else:
                    try:
                        client.send(cmd.encode())
                        output = client.recv(8192).decode()
                        print(output)
                        continue
                    except KeyboardInterrupt:
                        continue
        except:
            print("Something went wrong")
            quit()
    taichou()

if __name__ == "__main__":
    main()