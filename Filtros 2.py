import math

print("Programa para el calculo de condensadores")
continuar = True
while continuar == True:
    C = float(input("Ingrese el valor del condensador de entrada(en farads): "))
    while C < 0 :
            R = float(input("Valor invalido, ingrese de nuevo: "))
    f = float(input("Ingrese la frecuencia de corte (Hz): "))
    while f < 0 :
            f = float(input("Valor invalido, ingrese de nuevo: "))
    R = float(0.1125*math.sqrt(2)/(f*C))
    print("Valor de la resistencia de salida: " +str(R))
    continuar = bool(input("Desea continuar: "))
            
