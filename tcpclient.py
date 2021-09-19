from socket import *
host_name ="DESKTOP-3524G8U" #192.168.0.113
port_num=1200

clientSocket=socket(AF_INET, SOCK_STREAM) #IPV4, tcp连接
clientSocket.connect((host_name, port_num)) #建立socket连接
message=input("enter your message:")
clientSocket.send(message.encode()) #str字符串通过编码才能发送
fromservMessage=clientSocket.recv(1024).decode() #buffer接受
print("the message from server: " +fromservMessage+" server said")
clientSocket.close() #关闭socket



