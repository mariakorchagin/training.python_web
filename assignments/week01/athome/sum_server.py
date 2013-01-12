import socket
import sys

# Create a TCP/IP socket

server = socket.socket()

# Bind the socket to the port
server_address = ('127.0.0.1', 50000)
server.bind(server_address)

# Listen for incoming connections
server.listen(1)

try:

  while True:
	  # Wait for a connection
	  con, addr = server.accept()
  
	  try:
		  # Receive the data and send it back
		  msg = con.recv(4096)
		  print "Numbers received:", msg
		  numbers = msg.split(",")
		  sum = 0
		  for n in numbers:
		    sum += int(n)

		  print "Sum of them is:", sum
		  
		  con.sendall(str(sum))
  
	  finally:
		  # Clean up the connection
		  con.close()

except KeyboardInterrupt:
  server.close()
  # del server
  # sys.exit()