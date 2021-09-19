from socket import *
serverSocket=socket(AF_INET, SOCK_STREAM)
serverSocket.bind((gethostname(), 1200))

serverSocket.listen(2) #serversocket只起连接监听的作用
print("the server is ready to accept the message...")

connectionSocket,address=serverSocket.accept() #connectionsocket 起接受发送信息的作用
fromclientMessage=connectionSocket.recv(1024).decode()
print("got the message from the client:"+fromclientMessage)
connectionSocket.send(fromclientMessage)
connectionSocket.close()
