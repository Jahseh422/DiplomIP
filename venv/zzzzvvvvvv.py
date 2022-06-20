import subprocess

text = subprocess.check_output('netstat')
decoded = text.decode('cp866')

print(text)