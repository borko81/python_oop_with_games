import subprocess

cmd = 'ipconfig'
open_notepad = 'notepad'

ip = subprocess.Popen(cmd, shell=True)

notepad = subprocess.Popen(open_notepad, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(ip.wait())