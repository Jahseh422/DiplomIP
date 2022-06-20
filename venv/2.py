import netifaces
import datetime


now = datetime.datetime.now()
a: object = (netifaces.interfaces())


#loopback = (netifaces.ifaddresses('{ED29E33C-B605-41DC-A0F5-A6A25C1852C3}'))
#eth0 = (netifaces.ifaddresses('{93123211-9629-4E04-82F0-EA2E4F221468}'))




try:
 file = open("out.txt", "a+")
 file.write("\n")
 file.write("Р”Р°С‚Р° Р·Р°РїРёСЃРё:\n")
 file.write(str())
 file.write("\n")
 file.write("РЎРїРёСЃРѕРє РёРЅС‚РµСЂС„РµР№СЃРѕРІ:\n")
 file.write(str(a))
 file.write("\n")
 file.write(":\n")
 file.write("")
 #file.write(str(loopback))
 file.write("\n")
 file.write("")
 #file.write(str(eth0))
 file.write("\n")

except FileNotFoundError:
    print("")

import netifaces
import datetime
import ipaddress


now = datetime.datetime.now()
a: object = (netifaces.interfaces())


#loopback = (netifaces.ifaddresses('{F51A6749-68F2-11EC-A5E7-806E6F6E6963}'))
#eth0 = (netifaces.ifaddresses('{6948DD58-3D26-4F83-BE20-52F15DA55416}'))




try:
 file = open("out.txt", "a+")
 file.write("======================================\n")
 file.write(":\n")
 file.write(str(now.isoformat()))
 file.write("\n")
 file.write(":\n")
 file.write(str(a))
 file.write("\n")
 file.write(":\n")
 file.write("loopback:     ")
 #file.write(str(loopback))
 file.write("\n")
 file.write("eth0:         ")
 #file.write(str(eth0))
 file.write("\n================================================")

except FileNotFoundError:
    print(".")

