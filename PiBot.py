#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Jose Jacome"
__date__ ="$19-nov-2013 7:27:37$"
import RPi.GPIO as GPIO
import time

#Declaracion de la configuracion de la placa
GPIO.setmode(GPIO.BOARD)

#Pines ultrasonido
Trigger = 10
Echo = 12

#Pines sensor de linea
LD1 = 7 
#LD2 = 
#LI1 = 
#LI2 = 

#Pines Motores
D1 = 13
D2 = 11
I1 = 5
I2 = 3

GPIO.setwarnings(False)

#Inicializacion de Pines
GPIO.setup(Trigger,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)
GPIO.setup(LD1,GPIO.IN)
#GPIO.setup(L2,GPIO.IN)
#GPIO.setup(L3,GPIO.IN)
#GPIO.setup(L4,GPIO.IN)
GPIO.setup(D1,GPIO.OUT)
GPIO.setup(D2,GPIO.OUT)
GPIO.setup(I1,GPIO.OUT)
GPIO.setup(I2,GPIO.OUT)

def _ultra_():
    """Funcion que realiza la comprobracion del sensor ultrasonid HR-S04"""
    print("Ultra")
    try:
	GPIO.output(Trigger,False)
	time.sleep(0.5)
	GPIO.output(Trigger,True)
	time.sleep(0.00001)
	GPIO.output(Trigger,False)
	inicio = time.time()
	while GPIO.input(Echo)==0:
		inicio = time.time()
	while GPIO.input(Echo)==1:
		final = time.time()
	transcurrido = final - inicio
	distancia = transcurrido*34000
	distancia = distancia/2
	print distancia
	if distancia <=20 and distancia >3:
		return True
	else:
		return False
    except KeyboardInterrupt:
	print "Ultrasonido finalizado"
	GPIO.cleanup()			

def _linea_(): 
    """Funcion para controlar los sensores de linea"""
    print "Inicio Linea"
    while GPIO.input(LD1) == 1:
        Motor(D1,D2,0.5)
	Parar(D1,D2,0.3,1)	
	#while GPIO.input(LD2) == 1:
	#	Motor(D2,D1,0.5)
	#	Parar(D1,D2,0.3,1)
#	while GPIO.input(LI1) == 1:
#		Motor(I1,I2,0.5)
#		Parar(I1,I2,0.3,1)	
#	while GPIO.input(LI2) == 1:
#		Motor(I2,I1,0.5)	
#		Parar(I1,I2,0.3,1)	

def _motores_(HIGHI,HIGHD,delay):
    """Funcion para controlar los dos motores de una vez"""
    print "Mover los Motores"
    if HIGHI == I1 and HIGHD == D1: 	
            GPIO.output(HIGHI,True)
            GPIO.output(HIGHD,True)	
            time.sleep(delay)
            GPIO.output(I2,False)
            GPIO.output(D2,False)
            time.sleep(delay)
    elif HIGHI == I2 and HIGHD == D1:
            GPIO.output(HIGHI,True)
            GPIO.output(HIGHD,True)	
            time.sleep(delay)
            GPIO.output(I1,False)
            GPIO.output(D2,False)
            time.sleep(delay)
    elif HIGHI == I1 and HIGHD == D2:
            GPIO.output(HIGHI,True)
            GPIO.output(HIGHD,True)	
            time.sleep(delay)
            GPIO.output(I2,False)
            GPIO.output(D1,False)
            time.sleep(delay)
    else:
            GPIO.output(HIGHI,True)
            GPIO.output(HIGHD,True)	
            time.sleep(delay)
            GPIO.output(I1,False)
            GPIO.output(D1,False)
            time.sleep(delay)
	
def _motor_(LOW, HIGH ,delay):
    """Funcion que realiza giros con el motor en la busqueda"""
    print "Mover un motor"	
    GPIO.output(HIGH,True)
    time.sleep(delay)
    GPIO.output(LOW,False)
    time.sleep(delay)	
def _main_(): 
    print("Main")
    try:
        while True:
            Parar(D1,I1,0.3,2)	
            while Ultra() == False:
                Linea()			
                Motor(D1,D2,0.5)
                Parar(D1,D2,0.3,1)
                while Ultra() == True:
                    Parar(D1,D2,0.1,1)	
                    Linea()			
                    Motores(D1,I1,0.5)

    except KeyboardInterrupt:
            print("Programa Finalizado")

def _parar_(LOW, HIGH, delay,motores):
    """Hace una parada de un motor o de motores """
    print "Parar los motores"
    if motores == 1:	
	GPIO.output(HIGH,False)
	time.sleep(delay)
	GPIO.output(LOW,False)
	time.sleep(delay)
    else:
	GPIO.output(D1,False)
	time.sleep(delay)
	GPIO.output(D2,False)
	time.sleep(delay)
	GPIO.output(I1,False)
	time.sleep(delay)
	GPIO.output(I2,False)
	time.sleep(delay)
def _buscar_():
    print "Inicio Busqueda"
    U = ultra()
    while U == True:
        j 

_main_()	
