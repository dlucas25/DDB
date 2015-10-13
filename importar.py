import socket, os
from threading import *
class Servidor ( Thread ):
	def _init_ ( self ):
		Thread._init_( self )
	def run ( self ):
		self.process()
	def bindFileSocket ( self ):
		self.fileSocket = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
		self.fileSocket.bind(( '' , 9090))
		self.fileSocket.listen(1)
		print "Esperando conexion"
	def acceptFileSocket ( self ):
		self.fileConnection, self.fileAddr - self.fileSocket.accept()
		print "Conectado"
	def bindControlSocket ( self ):
		self.controlSocket = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
		self.controlSocket.bind(( '' , 9091))
		self.controlSocket.listen(1)
		print "Esperando conexion"
	def acceptControlSocket ( self ):
		self.controlConnection, self.controlAddr = self.controlSocket.accept()
		print "Conectado"
		while 1:
			datos = self.controlConnection.recv(1024)
			if not datos: break
			if datos [0:4] == "SEND":
				self.filename = datos[5:]
				break
	def transferencia( self ):
		ruta = "/home/daniel"
		f = open(ruta+self.fileName, "wb")
		w = ruta+self.fileName
		while 1:
			datos = self.fileConnection.recv(1024)
			if not datos: break
			f.write(datos)
			os.popen("mysqldump -u root -pdlucas importado < "+w)
			print "datos insertados"
		f.close()
	def cerrar ( self ):
		self.controlConnecction.close()
		self.fileConnection.close()
		self.controlSocket.close()
		self.fileSocket.close()
	def process ( self ):
		while 1:
			self.bindControlSocket()
			self.acceptControlSocket()
			self.bindFileSocket()
			self.acceptFileSocket()
			self.transferencia()
			self.cerrar()
servidor = Servidor()
servidor.start() 

	
	

