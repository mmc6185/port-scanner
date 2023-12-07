import socket 
import subprocess
import sys
from datetime import datetime

# Oturumu temizliyoruz
subprocess.call(["clear"])

# Kullanicidan ip aliyoruz
server = input("Enter the server you want to scan: ")
ServerIPAddress = socket.gethostbyname(server)

print("Scanning server " + ServerIPAddress)

timeStart = datetime.now()

try:
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket = sock.connect_ex((ServerIPAddress, port))
        
        if server_socket == 0:
            print ("Port {}:        Open".format(port))
        
        sock.close() 
        
except KeyboardInterrupt: 
    print("You pressed Ctrl+C")
    sys.exit()
 
except socket.gaierror: 
    print("Hostname could not be resolved. Exiting")
    sys.exit()
    
except socket.error:
    print("Couldn't connect to server")
    sys.exit
    
finally:
    timeEnd = datetime.now()
    total = timeEnd - timeStart
    print("Scanning Completed in in " + total)



