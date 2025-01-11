
import socket

def exit_chat(s):
    s.send('exit'.encode())  # Send 'exit' message to server
    print("Exiting chat...")
    s.close()

s = socket.socket()
host = input('Enter hostname or host IP: ')
port = 8080

try:
    s.connect((host, port))
    print('Connected to chat server')
except socket.error as e:
    print(f"Error connecting to server: {e}")
    exit()

while True:
    incoming_message = s.recv(1024).decode()
    if incoming_message.lower() == 'exit':
        print("Server has exited the chat.")
        break
    print('Server: ', incoming_message)
    message = input('>> ')
    if message.lower() == 'exit':
        exit_chat(s)
        break

    s.send(message.encode())

# Close the socket connection after exiting
s.close()




# Created by Sayan Mandal
# contact me in linkedln - (https://www.linkedin.com/in/codersayan/)