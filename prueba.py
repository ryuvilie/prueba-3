## registro de estudiantes
## comprobar rut
## visualizacion de todos los estudiantes
## buscar estudiante por RUT
## exportacion a csv

import csv

lista_estudiantes={'estudiantes':[]}

def registrar_estudiante():
    
    rut=input("rut (formato: 11.111.111-1): ")
    nombre=input("nombre: ")
    n1=float(input("nota 1: "))
    n2=float(input("nota 2: "))
    n3=float(input("nota 3: "))
    n4=float(input("nota 4: "))
    estudiante={
        'rut': rut,
        'nombre': nombre,
        'n1': n1,
        'n2': n2,
        'n3': n3,
        'n4': n4
    }
    lista_estudiantes['estudiantes'].append(estudiante)
    print(lista_estudiantes)
    print("estudiante registrado con exito")


def visualizar_estudiantes():
    print("lista de estudintes: ")
    for estudiantes in lista_estudiantes.items():
        for estudiante in estudiantes:
            nombre=estudiante['nombre']
            rut= estudiante('rut')
            n1= estudiante('n1')
            n2= estudiante('n2')
            n3= estudiante('n3')
            n4= estudiante('n4')
            print(f"{nombre} {rut} {n1} {n2} {n3} {n4}")

def exportacion_csv():
    with open("nuevo_archivo.csv", "w", newline="") as archivo_csv:
     escritor_csv= csv.writer(archivo_csv)
     escritor_csv.writerow(["nombre ",  "  rut  ",  " nota 1", " nota 2", " nota 3", " nota 4", " nota presentacion", " nota final"])
     for estudiantes in lista_estudiantes.items():
        for estudiante in estudiantes:
            nombre=estudiante['nombre']
            rut= estudiante('rut')
            n1= estudiante('n1')
            n2= estudiante('n2')
            n3= estudiante('n3')
            n4= estudiante('n4')
            escritor_csv.writerow([nombre, rut, n1, n2, n3 ,n4])

def buscar_estudiante(rut_buscado):
      for estudiantes in lista_estudiantes.items():
        for estudiante in estudiantes:
            nombre=estudiante['nombre']
            rut= estudiante('rut')
            n1= estudiante('n1')
            n2= estudiante('n2')
            n3= estudiante('n3')
            n4= estudiante('n4')
            if rut_buscado == rut:
                print(f"{nombre} {rut} {n1} {n2} {n3} {n4}")

while True:
    print("menu")
    print("1. registar estudiante")
    print("2. ver todos los estudiantes")
    print("3. buscar estudiante por rut")
    print("4. exportar a csv")

    opcion=input()
    if opcion =='1':
        registrar_estudiante()
    elif opcion == '2':
        visualizar_estudiantes()
    elif opcion == '3':
        rut_buscado=input("ingrese el rut del estudiante que desea buscar: ")
    elif opcion == '4':
        exportacion_csv()