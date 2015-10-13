import socket, os
os.popen("mysqldump -u root -pdlucas bdd >  /home/daniel/backupdb/respaldo.sql")
ruta = "/home/daniel/backupdb/"
filename = "respaldo.sql"
HOST = "192.168.43.111"

CPORT = 9091
FPORT = 9090

control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
control.connect((HOST,CPORT))
control.send("SEND" + filename)
control.close()

archivo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
archivo.connect((HOST,FPORT))

f= open(ruta+filename,"rb")
datos=f.read()
f.close()

archivo.send(datos)
archivo.close()
