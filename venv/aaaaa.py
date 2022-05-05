import socket
import os
import platform





ipdress = socket.gethostbyname(socket.gethostname())
host = socket.gethostname()


print('Твой локальный ип - ', ipdress)
print ('Название твоего компа:', platform.node())
print('Более точная проверка путем gethostname:',host)