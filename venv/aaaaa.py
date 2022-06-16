import socket
import os
import platform  #импорт требуемых библиотек




ipdress = socket.gethostbyname(socket.gethostname()) #получение локального IP.
host = socket.gethostname() #получение имени компьютера, через хранение в контейнере.


print('Локальный ip - ', ipdress)
print('Название компьютера:', platform.node())
print('Получение имени через контейнер, путем gethostname:',host)