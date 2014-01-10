#!/usr/bin/env python
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Jose Jacome"
__date__ ="$27/10/2013 06:08:02 PM$"
grados=float(1)
decimales=10
salida='{0:.3f}.'
tipovariable=''
import math
"""Esta funcion imprime los dos valores pasados
como parametros"""
def hacer(entrada):
    print('Entro')
    if 'help' in entrada:
        print("Presione ans para obtener la respuetas anterior")
        print('Inserte config para configurar la calculadora')
    if 'config' in entrada:
        config()
        
def config():
    print('Inserte la opcion deseada: 1)Configurar la unidad de grados\n2) Numero de decimales')
    print('Presione S para salir')
    input=input('>: ')
    while(input != 'S'):
        if input=='1':
            if 'gra' in input('Ingrese radianes o grados: '):
                grados = float(180/math.pi)
        if input=='2':
            decimales = int(input('>:'))
            while decimales <= 0:
                decimales = int(input('Numero no permitido, ingrese de nuevo: '))
        salida='{0:.'+decimales+'f}.'        
def tipo(entrada):
    entrada=str(entrada)
    if "/_" in entrada:
        s=entrada.split("/_")
        entrada=str(float(s[0]) * math.cos(grados*float(s[1])))
        entrada = complex(entrada)
        entrada=entrada+complex(str(float(s[0]) * math.sin(grados*float(s[1])))+"j")
        return entrada
    elif "j" in entrada:
        entrada = complex(entrada)
        return entrada
    else:
        try:
            entrada=float(entrada)
            print(1)
        except:
            tipovariable='string'
            print(tipovariable)
            entrada=str(entrada)
        return entrada
def comprobar(entrada):
    entrada=str(entrada)
    if "/_" in entrada: 
        return "C"
    if "j" in entrada:
        return "C"
    if "help" in entrada or 'conf' in entrada:
        return "help"
    if "S" in entrada:
        return "S"
    return "N" 
def imprimir(entrada):
    print(tipovariable)
    if tipovariable == 'C' or tipovariable == 'string':
        print(entrada)
    else:
        print(salida.format(entrada))
def ingreso():
    try:
        entrada = input('>: ')
    except Mierror as e:
        print('Ocurrio el siguiente error: '+e+'\n Revise la ayuda para continuar')
    return entrada
print("Bienvenidos a mi programa")
print("Escribe help en la pantalla para ayuda")
entrada = ''
while entrada != "S":
    ingreso()
    if comprobar(entrada) == 'S':
       print("Gracias por entrar :)")
       break
    if comprobar(entrada) == 'help':
        hacer(entrada)
        entrada=entrada()
        continue
    entrada=tipo(entrada)    
    imprimir(entrada)
    ans=entrada
    



