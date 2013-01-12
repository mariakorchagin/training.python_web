import socket
import sys

# Create a TCP/IP socket
client = socket.socket()

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)
client.connect(server_address)

try:
    # generate two numbers
    while True:
        try:
            number_one = int(raw_input("Enter the first number in the sum: "))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
    
    while True:
        try:
            number_two = int(raw_input("Enter the second number in the sum: "))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
    
    message = str(number_one)+","+str(number_two)
    print "Numbers sent:", message
    
    # Send data
    client.sendall(message)
    
    # print the response
    print "Sum of them is:", client.recv(4096)

finally:
    # close the socket to clean up
    client.close()