import os
import time
from numpy import *
from funciones import *
os.system("cls")
lruts = []
lnombres = []
lmascotas = []
ldias = []
lhabitacion = []
lpiso = []
idunico = []
acumulador = 0
habitacion = zeros((2,5), int)
while True:
    os.system("cls")
    menu_mascotasegura = menu()
    if menu_mascotasegura == 1:
        if 0 not in habitacion:
            continue
        rut = validar_rut()
        nombre = validar_nombre()
        nombre_mascota = validar_nombremascota()
        dias = cantidad_dias()
        id_unico = acumulador + 1
        while True:
            verhabitaciones(habitacion)
            piso = validar_piso(1,2)
            habi = validar_habitacion(1,5)
            if habitacion[piso-1][habi-1] == 0:
                habitacion[piso-1][habi-1] = 1
                break
            else:
                print("Habitación llena! porfavor elija otro piso o otra habitación.")
        idunico.append(id_unico)
        lruts.append(rut)
        lnombres.append(nombre)
        lmascotas.append(nombre_mascota)
        ldias.append(dias)
        lpiso.append(habi-1)
        lhabitacion.append(piso-1)
        print("Su mascota ha sido registrada correctamente!")
        time.sleep(2)
    elif menu_mascotasegura == 2:
        os.system("cls")
        rut = validar_rut()
        if rut in lruts:
            pos = posc(rut,lruts)
            print(f"Su mascota se encuentra en piso: {lpiso[pos]}, habitación: {lhabitacion[pos]}")
            time.sleep(3)
        else:
            print("RUT NO EXISTE!")
            time.sleep(2)
    elif menu_mascotasegura == 3:
        os.system("cls")
        rut = validar_rut()
        if rut in lruts:
            pos = posc(rut,lruts)
            total = ldias[pos] * 15000
            print(f"Su total a pagar es: ${total}")
            time.sleep(3)
        else:
            print("RUT NO EXISTE!")
            time.sleep(2)
    else:
        break