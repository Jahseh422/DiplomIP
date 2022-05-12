import netifaces
import datetime
import ipaddress # импорт требуемых библиотек


now = datetime.datetime.now() #переменная для записи даты в начало файла
a: object = (netifaces.interfaces()) #использование импортированной библиотеки netifaces, с помощью которой выводится список интерфейсов


loopback = (netifaces.ifaddresses('{F51A6749-68F2-11EC-A5E7-806E6F6E6963}')) #интерфейс loopback
eth0 = (netifaces.ifaddresses('{6948DD58-3D26-4F83-BE20-52F15DA55416}')) #ethernet интерфейс




try:
 file = open("out.txt", "a+")                                      #команда file=open с аргументом a+ создает файл out.txt /если создан, дозаписывает
 file.write("================================================\n")  #запись для удобства чтения, /n - переход на новую строку
 file.write("Дата записи:\n")
 file.write(str(now.isoformat()))                                  # использование переменной new в формате iso
 file.write("\n")
 file.write("Список интерфейсов:\n")
 file.write(str(a))                                                #запись интерфейсов в файл out.txt
 file.write("\n")
 file.write("Информация о интерфейсе loopback и eth0 :\n")
 file.write("loopback:     ")
 file.write(str(loopback))                                        # записывает информацию о интерфейсе loopback в файл
 file.write("\n")
 file.write("eth0:         ")
 file.write(str(eth0))                                            #записывает информацию о интерфейсе eth0 в файл
 file.write("\n================================================")

except FileNotFoundError:                                         #на случай ошибки доступа python к созданию/редактированию файлов (вывод в консоль ошибки "Файл не найден"
    print("Файл не найден.")

