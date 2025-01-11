
import socket

def exit_chat(conn):
    conn.send('exit'.encode())  # Notify client that server is exiting
    print("Server is exiting...")
    conn.close()
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
print('Server will start on host:', host)
print('Waiting for connection...')
s.listen(1)
conn, addr = s.accept()
print(addr, 'Has connected to the server')

while True:
    message = input('>> ')
    if message.lower() == 'exit':
        exit_chat(conn)
        break
    message = message.encode()
    conn.send(message)
    incoming_message = conn.recv(1024).decode()
    if incoming_message.lower() == 'exit':
        print("Client has exited the chat.")
        break

    print('Client: ', incoming_message)

# Close the connection after exiting
conn.close()




# Created by Sayan Mandal
# contact me in linkedln - (https://www.linkedin.com/in/codersayan/)