#! /usr/bin/env python

import random
import platform
from datetime import date
import time
import os

__author__="JosÃ© JÃ¡come"
__date__ ="$27/11/2013 05:05:26 PM$"

apellidos =[]
aux = 0
longitud = int(0)
integrantes = 0
razon = 0
print('Ingrese el nombre de los integrantes presione solo enter para finalizar')
while True:
	ingreso = input('['+str(integrantes + 1)+']: ')
	if ingreso == '':
		break
	else:
		apellidos.append(ingreso)
		if longitud < len(apellidos[integrantes]):
			longitud = len(apellidos[integrantes])
		integrantes += 1
def nDiapositivas():
	error = ValueError
	while error == ValueError:
		try:
			diapositivas=int(input('Ingrese el numero de diapositivas: '))
			error = 0
		except ValueError:
			error = ValueError
			print('Ingrese un numero por favor!')
	while(diapositivas < integrantes):
		print('Valor invalido de diapositivas, ingrese de nuevo')
		diapositivas=int(input('Ingrese el numero de diapositivas: '))
	if diapositivas%integrantes > 4:
		razon=int(diapositivas/integrantes)+1
	else:
		razon=int(diapositivas/integrantes)
	random.shuffle(apellidos)
	for i in range(0,len(apellidos)):
		while len(apellidos[i]) < longitud:
			apellidos[i] += " "
		if i < integrantes - 1 :
			apellidos[i]+=' = ' + str(aux+1) +"-"+str(aux+razon)
		else:
			apellidos[i]+=' = ' + str(aux+1) +"-"+str(diapositivas)
		aux += razon
		
	#Imprime en orden el diccionario
	apellidos.sort()
	print(integrantes)
	day = str(date.today().day)
	month = str(date.today().month)
	year = str(date.today().year)
	hora = str(time.localtime()[3])
	minuto = str(time.localtime()[4])
	segundo = str(time.localtime()[5])#Crea un log para todos los integrantes
	log = open('integrantes.log','w')
	for i in range(0,len(apellidos)):
		log.write(apellidos[i] + "\n");
		print(apellidos[i])
	log.write("\n<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\n")
	log.write("Numero de Diapositivas = " + str(diapositivas) + ", Numero de Integrantes = "+ str(integrantes)+"\n")
	log.write(day+ "/" + month + "/" +year+ ","+hora+":"+minuto+":"+segundo + " Generado en python "+platform.python_version()+"\n")
	log.write(platform.node() + " " + platform.system() + " " + platform.release() + "\n")
	log.close()
	print(day+ "/" + month + "/" +year+ ","+hora+":"+minuto+":"+segundo + " Generado en python"+platform.python_version())
	print(platform.node() + " " + platform.system() + " " + platform.release())
	print("Guardado en el archivo " + os.getcwd() + "/integrantes.log")
def nTemas():
	

input()
