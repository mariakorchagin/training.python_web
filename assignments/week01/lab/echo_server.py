 # Create a TCP/IP socket
 
server = socket.socket()

 # Bind the socket to the port
server_address = ('127.0.0.1', 50000)
server.bind(server_address)
server_address = ('localhost', 50000)
 
 # Listen for incoming connections
server.listen(1)
 
try:
while True:
    # Wait for a connection
 
  while True:
	  # Wait for a connection
	  con, addr = server.accept()
  
	  try:
		  # Receive the data and send it back
		  msg = con.recv(4096)
		  con.sendall(msg)
  
	  finally:
		  # Clean up the connection
		  con.close()
    try:
        # Receive the data and send it back
        
 
except KeyboardInterrupt:
  server.close()
  # del server
  # sys.exit()
    finally:
        # Clean up the connection