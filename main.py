# import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket ( AF_INET , SOCK_STREAM )
# Prepare a server socket on a particular port
# Fill in code to set up the port
while True :
# Establish the connection
	print (' Ready to serve ...')
	connectionSocket , addr = serverSocket.accept()
	try :
		message = # Fill in code to read GET request
		filename = message . split () [1]
		# Fill in security code
		f = open ( filename )
		outputdata = # Fill in code to read data from the file
		# Send HTTP header line ( s ) into socket
		# Fill in code to send header ( s )
		# Send the content of the requested file to the client
		for i in range (0 , len ( outputdata ) ) :
			connectionSocket . send ( outputdata [ i ]. encode () )
		connectionSocket . send ( " \ r \ n " . encode () )
		connectionSocket . close ()
	except IOError :
		# Send response message for file not found
		# Fill in
		# Close client socket
		# Fill in
serverSocket.close()
sys . exit () # Terminate the program after sending the corresponding data