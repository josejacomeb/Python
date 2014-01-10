import math

print("Programa para el calculo de condensadores")
continuar = True
while continuar == True:
    R = float(input("Ingrese el valor de la resistencia de entrada(en ohms): "))
    while R < 0 :
            R = float(input("Valor invalido, ingrese de nuevo: "))
    g = float(input("Ingrese la ganancia: "))
    while g < 0 :
            g = float(input("Valor invalido, ingrese de nuevo: "))
    R2 = g*R
    f = float(input("Ingrese la frecuencia de corte (Hz): "))
    while f < 0 :
            f = float(input("Valor invalido, ingrese de nuevo: "))
    w = float(2*math.pi*f)
    total = 1/(w*R2)
    print("Valor del capacitor: " + str(total))
    print("Valor de la resistencia de salida: " +str(R2))
    continuar = bool(input("Desea continuar: "))
            
