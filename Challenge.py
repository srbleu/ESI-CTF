import base64 
from netcat import Netcat

nc = Netcat('52.39.186.232', 1120)

for i in range (0,6):
    output = nc.read()
    print output

    string = output.split(": ")
    nc.write(base64.b64decode(string[1]))
