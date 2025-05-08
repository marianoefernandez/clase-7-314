import random

def mostrar_empleados(array_legajos:list, array_sueldos:list,array_nombres:list,array_edades:list) -> None:
    for i in range(len(array_legajos)):
        print(f"MOSTRANDO EMPLEADO {i+1}")
        mostrar_empleado(array_legajos,array_sueldos,array_nombres,array_edades,i)
        print("")
        
def cargar_empleados(array_legajos:list, array_sueldos:list,array_nombres:list,array_edades:list) -> bool :
    retorno = False
    
    for i in range(len(array_edades)):
        print(f"CARGANDO EMPLEADO {i+1}")
        nombre = input("Ingrese su nombre: ")
        #Validar esto
        edad = int(input("Ingrese su edad: "))
        #Validar
        sueldo = float(input("Ingrese su sueldo: "))
        #Validar
        #El legajo no se pide, el sistema lo genera
        #Puede ser autoincremental 
        #Random
        legajo = random.randint(11111,99999)
        
        array_legajos[i] = legajo
        array_nombres[i] = nombre
        array_sueldos[i] = sueldo
        array_edades[i] = edad
        
        print("EMPLEADO CARGADO")
        
        retorno = True
        
    return retorno
        
def sumar_array(array:list) -> float | int:
    acumulador = 0
    for i in range(len(array)):
        if type(array[i]) == int or type(array[i]) == float:
            acumulador += array[i]
    
    return acumulador

def calcular_promedio(acumulador:float | int, contador:int) -> float | None:
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
        
    return promedio

def buscar_maximo_array(array:list) -> int:
    bandera = False
    
    for i in range(len(array)):
        if bandera == False:
            maximo = array[i]
            indice = i
            bandera = True
        else:
            if array[i] > maximo:
                maximo = array[i]
                indice = i 
                
    return indice

def mostrar_empleado(array_legajos:list, array_sueldos:list,array_nombres:list,array_edades:list,indice_empleado:int) -> None:
    print(f"Legajo: {array_legajos[indice_empleado]}")
    print(f"Nombre: {array_nombres[indice_empleado]}")
    print(f"Edad: {array_edades[indice_empleado]}")
    print(f"Sueldo: $ {array_sueldos[indice_empleado]}")
    
def saludar():
    print("HOLA MUNDO")