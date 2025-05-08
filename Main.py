#Necesitamos un sistema para alojar a los empleados de la empresa , los mismos tienen que tener un legajo, un nombre, su edad y el sueldo que tienen
#Dentro de la empresa hay 3 empleados

#Aplicamos el concepto de arrays paralelos para estructurar los datos
#Son distintos arrays que estan relacionados entre si por su indice, cada uno de estos represanta un dato en particular
#Estos mismos deben tener la misma cantidad de elementos

from Funciones import *
import os

array_legajos = [0,0,0]
array_nombres = [0,0,0]
array_edades = [0,0,0]
array_sueldos = [0,0,0]
bandera_carga = False

#MOSTRANDO

# mostrar_empleados(array_legajos,array_sueldos,array_nombres,array_edades)
# cargar_empleados(array_legajos,array_sueldos,array_nombres,array_edades)
# mostrar_empleados(array_legajos,array_sueldos,array_nombres,array_edades)

#1.Cargar empleados
#2.Mostrar empleados
#3.Calcular promedio de sueldos
#4.Mostrar el empleado con mayor salario
#5.Salir

saludar()

while True:
    #Muestra el menu
    print("1.Cargar Empleados \n2.Mostrar Empleados\n3.Calcular promedio sueldos\n4.Mostrar el empleado con mayor salario\n5.Salir")
    #Me pide la opcion a elegir
    opcion = int(input("Ingrese la opcion: "))
    while opcion > 5 or opcion < 1:
        print("OPCION ERRONEA")
        opcion = int(input("Reingrese la opcion(1-5): "))
    #La elige
    if opcion == 1:
        respuesta = cargar_empleados(array_legajos,array_sueldos,array_nombres,array_edades)
        
        if respuesta == True:
            print("EMPLEADOS CARGADOS CON EXITO")
            bandera_carga = True
        else:
            print("HUBO ERROR AL CARGAR")
    elif opcion == 2:
        if bandera_carga == True:
            mostrar_empleados(array_legajos,array_sueldos,array_nombres,array_edades)
        else:
            print("No se pueden mostrar los empleados porque no fueron cargados")
    elif opcion == 3:
        if bandera_carga == True:
            suma_sueldos = sumar_array(array_sueldos)
            promedio = calcular_promedio(suma_sueldos,len(array_sueldos))
            print(f"El promedio de sueldos es de ${promedio}")
        else:
            print("No es posible calcular el promedio de sueldos porque no se cargo ningun empleado")
    elif opcion == 4:
        if bandera_carga == True:
            print("MOSTRANDO AL EMPLEADO CON MAYOR SUELDO")
            indice_mayor_sueldo = buscar_maximo_array(array_sueldos)
            mostrar_empleado(array_legajos,array_sueldos,array_nombres,array_edades,indice_mayor_sueldo)
        else:
            print("No se puede mostrar el empleado con mayor sueldo porque no se cargo nada.")
    else:
        print("Saliendo...")
        break
    
    #Punto de control en el que usuario tiene que tocar cualquier tecla para continuar
    input("Presione cualquier tecla para continuar...")
    #os.system("cls")
    os.system("clear")