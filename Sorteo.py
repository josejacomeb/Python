#! /usr/bin/env python

import random


__author__="José Jácome"
__date__ ="$05/12/2013 05:05:26 PM$"

e=0
a=0
pot1 = ["Brasil", "España", "Alemania", "Argentina", "Colombia", "Bélgica", "Uruguay","Suiza"]
pot2 = ["Chile", "Costa de Marfil", "ECUADOR", "Ghana", "Argelia", "Nigeria","Camerún"]
pot3 = ["Estados Unidos", "México", "Costa Rica", "Honduras", "Japón", "Irán","Corea del Sur" , "Australia"]
pot4 = ["Holanda", "Italia", "Inglaterra", "Portugal", "Grecia", "Bosnia-Herzegovina", "Crocia", "Rusia" , "Francia"]
rand = 0
america = ["Argentina", "Brazil", "Colombia", "Chile", "ECUADOR", "Uruguay"]
europa = ["Holanda", "Italia", "Inglaterra", "Portugal", "Grecia", "Bosnia-Herzegovina", "Croacia", "Rusia" , "Francia", "España", "Alemania", "Bélgica", "Suiza"]
grupoA = []
grupoB = []
grupoC = []
grupoD = []
grupoE = []
grupoF = []
grupoG = []
grupoH = []
def _main_():
  _init_()
  _sorteo_(grupoA)
  _sorteo_(grupoB)
  _sorteo_(grupoC)
  _sorteo_(grupoD)
  _sorteo_(grupoE)
  _sorteo_(grupoF)
  _sorteo_(grupoG)
  _sorteo_(grupoH)
  print("\tPosible sorteo Copa Mundial FIFA\t")
  print("\n\t\t\tGrupo A\t")
  _imprimir_(grupoA)
  print("\n\t\t\tGrupo B\t")
  _imprimir_(grupoB)
  print("\n\t\t\tGrupo C\t")
  _imprimir_(grupoC)
  print("\n\t\t\tGrupo D\t")
  _imprimir_(grupoD)
  print("\n\t\t\tGrupo E\t")
  _imprimir_(grupoE)
  print("\n\t\t\tGrupo F\t")
  _imprimir_(grupoF)
  print("\n\t\t\tGrupo G\t")
  _imprimir_(grupoG)
  print("\n\t\t\tGrupo H\t")
  _imprimir_(grupoH)
  input()
      
def _validar_(pot, nrand):
  global a
  global e
  if pot[nrand] in europa:
    e += 1
  elif pot[nrand] in america:
    a += 1
  else:
    g = 0
  if pot[nrand] in europa and e==3:
    e-=1
    return False
  elif pot[nrand] in america and a==2:
    a-=1
    return False
  else:
    return True
      
def _init_():
  rand = random.randint(0, len(pot4)-1)
  pot2.append(pot4[rand])
  del(pot4[rand])
  for i in range(0,4):
    random.shuffle(pot1)
    random.shuffle(pot2)
    random.shuffle(pot3)
    random.shuffle(pot4)
def _sorteo_(grupo):
  global e
  global a
  rand = random.randint(0, len(pot1)-1)
  _validar_(pot1,rand)
  grupo.append(pot1[rand])
  del(pot1[rand])
  rand = random.randint(0, len(pot2)-1)
  while _validar_(pot2,rand) == False:
    rand = random.randint(0, len(pot2)-1)
  grupo.append(pot2[rand])
  del(pot2[rand])
  rand = random.randint(0, len(pot3)-1)
  while _validar_(pot3,rand) == False:
    rand = random.randint(0, len(pot3)-1)
    print(pot3[rand])
    print(grupo)
  grupo.append(pot3[rand])
  del(pot3[rand])
  rand = random.randint(0, len(pot4)-1)
  while _validar_(pot4,rand) == False:
    rand = random.randint(0, len(pot4)-1)
    print(pot4[rand])
  grupo.append(pot4[rand])
  del(pot4[rand])
  e = a = 0
def _imprimir_(grupo):
  print("\n \t" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\t \n")
  for i in range(0,4):
	  print("\t\t"+ grupo[i]) 
	      
_main_()	
