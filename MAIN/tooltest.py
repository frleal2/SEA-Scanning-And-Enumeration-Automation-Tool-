import subprocess

cmd = "/bin/nmap -v -sn 192.168.0.0/16 10.0.0.0/8"

toolPath = ""
optionandargs = ""
whitelise = ""

cmd = toolPath

p = subprocess.Popen(cmd, shell = True, stderr = subprocess.PIPE)
