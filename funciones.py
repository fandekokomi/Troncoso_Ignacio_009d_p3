import msvcrt as tecla
#validaciones
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_piso(min:int,max:int):
    while True:
        try:
            piso = int(input(f"Ingrese número de piso ({min},{max}):"))
            if piso >= min and piso <= max:
                return piso
            else:
                print("ERROR! PISO INCORRECTO")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def validar_habitacion(min:int,max:int):
    while True:
        try:
            habitacion = int(input(f"Ingrese número de habitación ({min},{max}):"))
            if habitacion >= min and habitacion <= max:
                return habitacion
            else:
                print("ERROR! HABITACIÓN INCORRECTA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def validar_opcion(min:int,max:int):
        while True:
            try:
                opcion = int(input("Ingrese opción: "))
                if opcion >= min and opcion <= max:
                    return opcion
                else:
                    print("¡ERROR! ¡OPCIÓN INCORRECTA!")
            except:
                print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_nombremascota():
    while True:
        nombre = input("Ingrese nombre de mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
def menu():
    print("""MENU: 
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir""")
    opcion = validar_opcion(1,4)
    return opcion
def cantidad_dias():
    while True:
        try:
            dias = int(input("Ingrese cantidad de días que permanecera en la guardería: "))
            if dias >= 1:
                return dias
            else:
                print("ERROR! Ingrese almenos un dia")
        except:
            print("DEBE INGRESAR UN NÚMERO ENTERO!")
def verhabitaciones(habitacion):
    print("\tHabitaciones: \n")
    for x in range(2):
        print(" Piso",x+1)
        for y in range(5):
            print("\nHabitación",y+1,": ",habitacion[x][y], end= " ")
        print()
    print("Ingrese una tecla para continuar...")
    tecla.getch()
def posc(rut,lruts):
    for x in range(100):
        if rut == lruts[x]:
            posicion_encontrada = x
            return posicion_encontrada
