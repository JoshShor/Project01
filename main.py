# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8000  # Prepare a server socket on a particular port
serverHost = '127.0.0.1'
# Fill in code to set up the port
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print("test ouside while")
while True:
    # Establish the connection
    print("inside while")
    print(' Ready to serve ...')
    connectionSocket, addr = serverSocket.accept()  # Fill in code to get a connection
    print("connection address: " + addr)
    print("test test test test test")
    try:
        print("at the try block")
        message = connectionSocket.recv(1024).decode()  # Fill in code to read GET request
        filename = message.split()[1]
        if "/../" in filename:
            connectionSocket.send('HTTP/1.1 403 Forbidden\r\n\r\n')  # Fill in security code
            connectionSocket.close()
            break
        f = open(filename)
        outputdata = f.read()  # Fill in code to read data from the file
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')  # Send HTTP header line ( s ) into socket
        # Fill in code to send header ( s )
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send(" \r \n ".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())  # Send response message for file not found
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Fill in
        connectionSocket.close()  # Close client socket
    # Fill in
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
