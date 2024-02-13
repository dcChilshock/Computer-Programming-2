# pip install rsa
# import rsa 
# import socket
# import threading 

# public_key, private_key = rsa.newkeys(1024) #1024 bits
# DEFAULT_IP_PORT = ("127.0.0.1", 9999)
# choice = input("Do you want to be server or client? (type s(server) or c(cancel)):")

# if choice == "s": #choice server 
#   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   server.bind(DEFAULT_IP_PORT) #open TCP connection
#   server.listen() #looking for connection 
#   print("waiting for connection.... get some friends you loser ahahhaaahahhahahhh")
#   client, addr = server.accept() #accept client joining server?
#   print("Connected to", addr)
#   client.send(pubic_key.save_pkcs1())
#   public_partner = rsa.PublicKey.load_pkcs1(client.rev(1024))
#   print("Use 'Ctrl+C' to disconnect") #disconnect button
  
# elif choice == "c": #choice client
#   print("connecting to server.....", end="") 
#   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #can be changed to be bluetooth
#   client.connect(DEFAULT_IP_PORT)
#   print("success! Connected to", client.getpeername()) #getpeername gets the ip address of client
#   public_partner = rsa.PubicKey.load_pkcs1(client.recv(1024))
#   client.send(public_key.save_pkcs1())
#   print("use ctrl+c to disconnect")
  
# else: exit()


# #sending and getting messages
# #going to run in infinite loops
# def sendMsg(c): #sending messages
#   while True:
#     try: # if error happens just move on 
#       msg = input()
#       print('\033[1A' + '\033[K', end='')
#       c.send(rsa.encrypt(msg.encode(), public_partner))
#       print("\033[91mYou: \033[0m" + msg )
#     except: exit()

# def recvMsg(c): #recieve messages 
#   while True: # <- does infinite loop #needs to have both ends doing infinite loops to wait for sending and recieving 
#     try:
#       msg = rsa.decrypt(c.recv(1024), private_key)
#       print("\033[94mPartner: \033[0m" + msg.decode())
#     except:
#       input("partner has disconnected. press enter to exit.")
#       exit()
# try: #like managing the threads of sending and recieving stuff
#   send_thread = threading.Thread(target=sendMsg, args =(client,)).start()
#   recv_thread = threading.Thread(target=recvMsg, args = (client,)).start()
# except: pass
import threading
import socket
import rsa  # pip install rsa

public_key, private_key = rsa.newkeys(1024)  # 1024 bits
DEFAULT_IP_PORT = ("127.0.0.1", 9999)
choice = input("Do you want to be the server or client? (s/c): ")

if choice == "s":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(DEFAULT_IP_PORT)  # Open TCP connection
  server.listen()
  print("Waiting for connection...")
  client, addr = server.accept()
  print("Connected to", addr)
  client.send(public_key.save_pkcs1())
  public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
  print("Use 'Ctrl+C' to disconnect.")
elif choice == "c":
  print("Connecting to server...", end="")
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(DEFAULT_IP_PORT)
  print("success! Connected to " + str(client.getpeername()))
  public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
  client.send(public_key.save_pkcs1())
  print("Use 'Ctrl+C' to disconnect.")
else: exit()

def sendMsg(c):
  while True:
    try:
      msg = input()
      print('\033[1A' + '\033[K', end='')  # Delete input line
      c.send(rsa.encrypt(msg.encode(), public_partner))
      print("\033[91mYou: \033[0m" + msg)
    except: exit()

def recvMsg(c):
  while True:
    try:
      msg = rsa.decrypt(c.recv(1024), private_key)
      print("\033[94mPartner: \033[0m" + msg.decode())
    except:
      input("Partner has disconnected. Press enter to exit.")
      exit()

try:
  send_thread = threading.Thread(target=sendMsg, args=(client,)).start()
  recv_thread = threading.Thread(target=recvMsg, args=(client,)).start()
except: pass