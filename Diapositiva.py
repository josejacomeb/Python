#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import random 
import platform
from datetime import date
import time
import os

__author__="José Jácome"
__date__ ="$29/10/2013 05:05:26 PM$"

lista=[]
apellidos=[]
aux=0
asignacion=[]
longitud=0
integrantes=int(input('Ingrese el numero de integrates: '))
diapositivas=int(input('Ingrese el numero de diapositivas: '))
while(diapositivas<integrantes):
    print('Valor invalido de diapositivas, ingrese de nuevo')
    diapositivas=int(input('Ingrese el numero de diapositivas: '))
if diapositivas%integrantes>4:
  razon=int(diapositivas/integrantes)+1
else:
  razon=int(diapositivas/integrantes)
for i in range(integrantes-1):
  lista.append(str(aux+1)+'-'+str(aux+razon))
  aux+=razon
  if i==integrantes-2:
    lista.append(str(aux+1)+'-'+str(diapositivas))
    break
for i in range(integrantes):
    apellidos.append(input('Ingrese el apellido del integrante ['+str(i+1)+']: '))
    if len(apellidos[i]) > longitud :
        longitud = len(apellidos[i])
#Saca aleatorios sin reemplazo y le añaden a la lista     
for i in range(integrantes): 
    laux=random.sample(range(integrantes),integrantes)
for i in range(integrantes):
    while len(apellidos[i]) < longitud:
        apellidos[i]+=' '
    apellidos[i]+=' = '
for i in range(integrantes):
    asignacion.append(apellidos[laux[i]]+lista[i]) 
#Imprime en orden el diccionario
asignacion.sort()
day = str(date.today().day)
month = str(date.today().month)
year = str(date.today().year)
hora = str(time.localtime()[3])
minuto = str(time.localtime()[4])
segundo = str(time.localtime()[5])#Crea un log para todos los integrantes
log = open('integrantes.log','w')
log.write(day+ "/" + month + "/" +year+ ","+hora+":"+minuto+":"+segundo + " Generado en python"+platform.python_version())
log.write("\n" + platform.node() + " " + platform.system() + " " + platform.release() + "\n")
for i in range(integrantes):
    log.write(asignacion[i] + "\n");
    print(asignacion[i])
log.close()
print(day+ "/" + month + "/" +year+ ","+hora+":"+minuto+":"+segundo + " Generado en python"+platform.python_version())
print(platform.node() + " " + platform.system() + " " + platform.release())
print("Guardado en el archivo " + os.getcwd() + "/integrantes.log")
input()
