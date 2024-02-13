import rsa # pip install rsa
import socket
import threading 

public_key, private_key = rsa.newkeys(1024) #1024 bits
DEFAULT_IP_PORT = ("127.0.0.1", 9999)
choice = input("Do you want to be server or client? (type s(server) or c(cancel)):")


if choice == "s": #choice server 
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(DEFAULT_IP_PORT) #open TCP connection
  server.listen() #looking for connection 
  print("waiting for connection.... get some friends you loser ahahhaaahahhahahhh")
  client, addr = server.accept() #accept client joining server?
  print("Connected to", addr)
  client.send(pubic_key.save_pkcs1())
  public_partner = rsa.PublicKey.load_pkcs1(client.rev(1024))
  print("Use 'Ctrl+C' to disconnect") #disconnect button
elif choice == "c": #choice client
  print("connecting to server.....", end="") 
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #can be changed to be bluetooth
  client.connect(DEFAULT_IP_PORT)
  print("success! Connected to", client.getpeername()) #getpeername gets the ip address of client
  public_partner = rsa.PubicKey.load_pkcs1(client.recv(1024))
  client.send(public_key.save_pkcs1())
  print("use ctrl+c to disconnect")
  