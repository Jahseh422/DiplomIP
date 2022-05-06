import socket
from datetime import datetime

net = input("Ввести IP: ")
net1 = net.split('.')
a = '.'
ф
net2 = int(input('Порт от: ')) # запрос порта о

st1 = int(input("Введите начальное число: "))
en1 = int(input("Введите конечное число: "))
en1 = en1 + 1
t1 = datetime.now()


def scan(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr, 445))
    if result == 0:
        return 1
    else:
        return 0


def run1():
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        if (scan(addr)):
            print(addr, "is live")


run1()
t2 = datetime.now()
total = t2 - t1
print("Scanning completed in: ", total)