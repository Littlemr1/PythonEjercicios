import fbchat
from getpass import getpass
username = str(input("Ingresar usuario: "))
client = fbchat.Client(username,getpass())
numFriends = int(input("Numero de amigo: "))
for i in range(numFriends):
    name = str(input("Nombre: "))
    friends = client.getUsers(name)
    friend = friends[0]
    msg = str(input("Ingresa mensaje: "))
    sent = client.send(friend.uid,msg)
    if sent:
        print("Mensaje enviado!")
