import socket 

BYTES_TO_READ = 4096  #we don't make it too big because it might be interrupted

def get(host, port):

  request_data = b"GET / HTTP/1.1\nHost:" + host.encode("utf-8") + b"\n\n"  #preparing data for a request

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # this will be an internet socket and we will use it as a stream
  s.connect((host,port))  #because we are a client
  s.send(request_data)  #making a request
  s.shutdown(socket.SHUT_WR) #shuts the write part of the socket, we can be sent a response
  result = s.recv(BYTES_TO_READ)
  while(len(result) > 0):  # in case message is longer than 4kb
    print(result)
    result = s.recv(BYTES_TO_READ)

  s.close()

get("www.google.com", 80)
