import socket
import threading
import hashlib 
import sqlite3



def signup():
  connection = sqlite3.connect("database_mine.db", timeout=10)
  cursor = connection.cursor()


  cursor.execute("""
  CREATE TABLE IF NOT EXISTS database_mine (
  id INTEGER PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
  )
  """)


  username = input("Enter a username: ")
  password = input("Enter a password: ")
  username1, password1 = "Treveen", hashlib.sha256("123".encode()).hexdigest()
  username2, password2 = "John", hashlib.sha256("lovehacking".encode()).hexdigest()
  username3, password3 = "Harold", hashlib.sha256("ipython".encode()).hexdigest()
  username4, password4 = username, hashlib.sha256(password.encode()).hexdigest()
  cursor.execute("INSERT INTO database_mine (username, password) VALUES (?, ?)", (username1, password1))
  cursor.execute("INSERT INTO database_mine (username, password) VALUES (?, ?)", (username2, password2))
  cursor.execute("INSERT INTO database_mine (username, password) VALUES (?, ?)", (username3, password3))
  cursor.execute("INSERT INTO database_mine (username, password) VALUES (?, ?)", (username4, password4))

  connection.commit()

def login(username, password):


    password_hash = hashlib.sha256(password).hexdigest()
    con_db = sqlite3.connect("database_mine.db")
    cursor = con_db.cursor()

    cursor.execute("SELECT * FROM database_mine WHERE username = ? AND password = ?", (username, password_hash))
    if cursor.fetchall():
      print(f"Logged in as {username}")
      dashboard()
    else:
      print(f"{username} or {password} was incorrect")




def join_group():
    ip = str(input("Enter the ip of the group: "))
    port = int(input("Enter it's port: "))
    nickname = input("Enter a nickname: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    def receive():
      while True:
        try:
          message = client.recv(1024).decode('ascii')
          if message == 'NICK':
            client.send(nickname.encode('ascii'))
          else:
            print(message)

            
        except:
          print("There was an error in the server x010")
          client.close()
          break

    def write():
      while True:
        message = f'{nickname}: {input("Type a message: ")}'
        client.send(message.encode('ascii'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

def new_group():



    host = str(input("Enter your ip: "))
    port = int(input("Enter a port: "))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()


    clients = []
    nicknames = []

    def show(message):
      for client in clients:
        client.send(message)

    def handle(client):

      while True:
        try:
          message = client.recv(1024)
          show(message)
        except:
          index = clients.index(client)
          clients.remove(client)
          client.close()
          nickname = nicknames[index]
          show(f'{nickname} left the chat due to an error'.encode('ascii'))
          nicknames.remove(nickname)
          break

    def receive():
      while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        print('===============================')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        show(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

    print("Server is listening ...")
    print("You are hosting this group")
    print("Join it using your ip.")
    print(f"Invite your friends with this ip: {host}")
    receive()

def dashboard():
  dashboard = """
   [ * - * - * - * -  * - * - ]
   [        ~ THB NET ~       ]
   [                          ]
   [      1 - New group       ]
   [      2 - Join group      ]
   [                          ]
   [ * - * - * - * -  * - * - ]
  """
  print(dashboard)
  option = int(input("Enter an option: "))
  if option == 1:
    new_group()
  elif option == 2:
    join_group()


def main():
  main = """
  [ * - * - * - * -  * - * - ]
  [        ~ THB NET ~       ]
  [                          ]
  [      1 - Signup          ]
  [      2 - Login           ]
  [                          ]
  [ * - * - * - * -  * - * - ]
  """
  print(main)
  option = int(input("Enter an option: "))

  if option == 1:
    signup()

  elif option == 2:
    username = input("Enter an username: ")
    password = input("Enter a password: ").encode()
    login(username=username, password=password)

  else:
    print("Option undefined")

main()