#!/usr/bin/python3

import os
import sys

import pyglet
from ventana_reproductor import VentanaReproductor
from reproductor import Reproductor
from cola_reproduccion import ColaDeReproduccion, EXTENSIONES_ACEPTADAS
from cancion import Cancion
EXTENSIONES_ACEPTADAS = (".wav", ".mp3", ".flac", ".ogg", ".wma")

def agregar_canciones(cola, ruta_directorio):
	""" Agrega a la cola las canciones que se encuentran en el directorio y en los directorios
	que se encuentran en el, recursivamente. Las extensiones aceptadas son las que se listan en
	ColaDeReproduccion."""
	path=os.getcwd()
	print(path)
	for (path, ficheros, archivos) in os.walk(path):
		for fichero in archivos:
			(nombreFichero, extension) = os.path.splitext(fichero)
			if(extension in EXTENSIONES_ACEPTADAS):
				print(path+"/"+fichero)
				cola.agregar_cancion(path+"/"+fichero)

def main():
		cola = ColaDeReproduccion()
		ruta_directorio = sys.argv[1] if len(sys.argv) > 1 else "."
		print(ruta_directorio)
		if not os.path.isdir(ruta_directorio):
			print("Ruta no válida: " + ruta_directorio)
			sys.exit(-1)
		agregar_canciones(cola, ruta_directorio)
		reproductor = Reproductor(cola)
		ventana_reproductor = VentanaReproductor(reproductor)
		ventana_reproductor.actualizar()

		pyglet.app.run()
		sys.exit(0)
if __name__ == '__main__':
	main()
