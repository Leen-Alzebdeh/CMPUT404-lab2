import socket

BYTES_TO_READ = 4096
HOST = "127.0.0.1"  #it will host on our own machine
PORT = 8080

def handle_connection(conn, addr):   #conn is a socket, but a different socket, it is directly to the client
   with conn: 
    print(f"Connected by {addr}")  #Print who connected to us
    while True:
      data = conn.recv(BYTES_TO_READ)
      if not data:
        break
      print(data)
      conn.sendall(data)  #send is different in that it doesn't garuntee all the data is sent

def start_server():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  #with block auto closes s
    s.bind((HOST,PORT))

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #SO_RESUSEADDR allows a socket to rebind to the same address 
    #mapages.debian
    s.listen()

    conn, addr = s.accept()
    handle_connection(conn, addr)  # we can get connection and address of the client


start_server()