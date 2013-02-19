#!/usr/bin/env python

import socket 

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

## read from tiny_html.html

import email
html = open('tiny_html.html','r')

## TODO: figure out how to make the timestamp different each time

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    data = client.recv(size)
    if data: # if the connection was closed there would be no data
      timestamp = email.Utils.formatdate()
      def ok_response(body, nowtime):
        first_line = "HTTP/1.1 200 OK"
        header = "Content-Type: text/html"
        timestamp = "Date: %s"%nowtime
        empty = ""
        response = "\r\n".join([first_line,header,timestamp,empty,body.read()])
        return response
      
      data = ok_response(html,timestamp)
      
    print "sending this: %s"%data
    client.send(data) 
    client.close()