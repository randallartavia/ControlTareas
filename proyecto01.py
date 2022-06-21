global lista
lista = list()

class Tarea:
    nombre= ""
    materia= ""
    porcentaje=0


def agregar(nom, mat, porc):
    p = Tarea()

    p.nombre=nom
    p.materia=mat
    p.porcentaje=porc
    lista.append(p)
    print("Se ha agregado la Tarea "+ p.nombre + " a la lista de tareas.")
    
    input("Presione enter para continuar.")
def consultarMateria (mat):
    for p in lista:
       if p.materia== mat:
           print("Tarea: "+p.nombre+" / Porcentaje: "+p.porcentaje)
    input("Presione enter para continuar.")
def CantidadTareas ():
    cantTareas = len(lista)
    print("Tiene un total de " + str(cantTareas) + " tareas.")
    input("Presione enter para continuar.")
def salir ():
    print("Salir")

def menu ():
    salir = False


    while not salir:
        print("       Menú     ")
        print("****************")
        print("1. Agregar Tarea")
        print("2. Consultar Tareas")
        print("3. Total de Tareas")
        print("4. Salir")

        opc=int(input("Digite una opcion: "))

        if opc == 1:
            nom = input("Ingrese el nombre de la tarea que desea agregar: ")
            mat = input("Ingrese la materia a la cuál pertenece la tarea: ")
            porc = input("Ingrese porcentaje que vale la tarea: ")
            agregar(nom, mat, porc)

        elif opc == 2:
            mat = input("Ingrese el nombre de la materia que desea consultar: ")
            consultarMateria(mat)
        elif opc == 3:
            CantidadTareas()
        else:
            print("Salir")
            salir= True

menu()
