import psutil

a = psutil.net_connections(kind='tcp')
print(a)



try:
 file = open("outnetstat.txt", "a+")
 file.write(str(a))
except FileNotFoundError:
    print("")
