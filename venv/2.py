import netifaces
import datetime        # импорт требуемых библиотек


now = datetime.datetime.now() #переменная для записи даты в начало файла
a: object = (netifaces.interfaces()) #использование импортированной библиотеки netifaces, с помощью которой выводится список интерфейсов


loopback = (netifaces.ifaddresses('{ED29E33C-B605-41DC-A0F5-A6A25C1852C3}')) #интерфейс loopback
eth0 = (netifaces.ifaddresses('{93123211-9629-4E04-82F0-EA2E4F221468}')) #ethernet интерфейс




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

