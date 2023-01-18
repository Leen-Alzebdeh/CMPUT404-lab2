import socket

BYTES_TO_READ = 4096

def get(host,port):
  
  request_data = b"GET / HTTP/1.1\www.google.com\n\n"

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))  #because we are a client
    s.send(request_data)  #making a request
    s.shutdown(socket.SHUT_WR) #shuts the write part of the socket, we can be sent a response
  result = s.recv(BYTES_TO_READ)
  while(len(result) > 0):  # in case message is longer than 4kb
    print(result)
    result = s.recv(BYTES_TO_READ)
    
    print("Waiting for response!")

    chunk = s.recv(BYTES_TO_READ)
    result = b'' + chunk

    while len(chunk) > 0:
      chunk = s.recv(BYTES_TO_READ)
      result += chunk

  return result

print(get("127.0.0.1", 8080))