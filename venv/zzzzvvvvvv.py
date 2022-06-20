import subprocess

a = range(100, 105)

text = subprocess.check_output('ping 192.168.1.3')
decoded = text.decode('cp866')

print(text)