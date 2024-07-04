#Importamos librerias
import csv              #Para exportar archivos csv
from os import system   #Para limpiar pantalla o pausar
import random           #Para numeros random en el ID

sectores_disponibles = ["Concepción","Chiguayante","Talcahuano","Hualpén","San Pedro"]
lista_pedidos = []

def registrar_pedido():
    nombre = input("Escriba el nombre del cliente: ")
    while nombre.isdigit() or len(nombre) < 3:      #Aseguramos que no sean numeros y tenga más de 3 caracteres.
        print("El nombre no es válido, ingrese nuevamente.")
        nombre = input("Escriba el nombre del cliente: ")
    apellido = input("Escriba el apelido del cliente: ")
    while apellido.isdigit() or len(apellido) < 3:
        print("El apellido no es válido, ingrese nuevamente.")
        apellido = input("Escriba el apellido del cliente: ")
    direccion = input ("Ingrese dirección del cliente: ")
    sector = input(f"Comunas disponibles: {sectores_disponibles}\nIngrese comuna del cliente: ")
    sector = sector.title()             #Para que lea strings en mayúscula o minuscula por igual.
    while sector not in sectores_disponibles:
        print("La comuna no es válida. Ingrese nuevamente")
        sector = input(f"Comunas disponibles: {sectores_disponibles}\nIngrese comuna del cliente: ")
        sector = sector.title()
    while True:
        try:
            cant_6lts = int(input("Ingrese la cantidad de dispensadores de 6 litros: "))
            cant_10lts = int(input("Ingrese la cantidad de dispensadores de 10 litros: "))
            cant_20lts = int(input("Ingrese la cantidad de dispensadores de 20 litros: "))
        except ValueError or (cant_6lts + cant_10lts + cant_20lts) <= 0:
            print("Debe al menos registrar un producto. Recuerde solo usar números.")
            continue
        id = random.randint(0,9999)
        pedido = {
            "ID":id,
            "Cliente":f"{nombre} {apellido}",
            "Dirección":direccion,
            "Sector":sector,
            "Disp.6lts":cant_6lts,
            "Disp.10lts":cant_10lts,
            "Disp.20lts":cant_20lts
        }
        lista_pedidos.append(pedido)
        print(f"Pedido registrado con ID {id}.")
        print("")
        system("pause")
        break
    
def listar_pedidos():
    if len(lista_pedidos) == 0:
        print("No hay pedidos registrados.\n")
        system("pause")
    else:    
        print("ID pedido\tCliente\t\tDirección\t\tSector\t\tDisp.6lts\tDisp.10lts\tDisp.20lts")
        for pedidos in lista_pedidos:
            print(f"{pedidos["ID"]}\t\t{pedidos["Cliente"]}\t{pedidos["Dirección"]}\t\t{pedidos["Sector"]}\t{pedidos["Disp.6lts"]}\t\t{pedidos["Disp.10lts"]}\t\t{pedidos["Disp.20lts"]}")
        system("pause")

def imprimir_hoja():
    if len(lista_pedidos) == 0:
        print("No hay pedidos registrados.\n")
        system("pause")
        return

    sector = input(f"Comunas disponibles: {sectores_disponibles}\nIngrese comuna del cliente a imprimir: ")
    sector = sector.title()
    if sector not in sectores_disponibles:
        print("No hay pedidos registrados en esa comuna.")
        system("pause")
    elif sector in sectores_disponibles:
        nombre_archivo = f"Lista_pedidos_{sector}.csv"
        with open(nombre_archivo,mode="w",newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["ID pedido\tCliente\t\tDireccion\t\tSector\t\tDisp.6lts\tDisp.10lts\tDisp.20lts"])
            for pedidos in lista_pedidos:
                if pedidos["Sector"] == sector:
                    writer.writerow([f"{pedidos["ID"]}\t\t{pedidos["Cliente"]}\t{pedidos["Dirección"]}\t\t{pedidos["Sector"]}\t{pedidos["Disp.6lts"]}\t\t\t{pedidos["Disp.10lts"]}\t\t\t{pedidos["Disp.20lts"]}"])
        print(f"Archivo guardado como {nombre_archivo}.")
        system("pause")

def buscar_id():
    if len(lista_pedidos) == 0:
        print("No hay pedidos registrados.\n")
        system("pause")
        return
    
    try:    
        id_busq = int(input("Introduzca la ID a buscar: "))
    except ValueError:
        print("Solo debe ingresar números.")
        system("pause")
        return
    
    for pedidos in lista_pedidos:
        print("ID pedido\tCliente\t\tDirección\t\tSector\t\tDisp.6lts\tDisp.10lts\tDisp.20lts")
        if pedidos["ID"] == id_busq:
            print(f"{pedidos["ID"]}\t\t{pedidos["Cliente"]}\t{pedidos["Dirección"]}\t\t{pedidos["Sector"]}\t{pedidos["Disp.6lts"]}\t\t{pedidos["Disp.10lts"]}\t\t{pedidos["Disp.20lts"]}")
    system("pause")


def menu_principal():
    while True:
        system("cls")
        print("""
 ** Menú CleanWasser **
1.	Registrar pedido
2.	Listar los todos los pedidos
3.	Imprimir hoja de ruta
4.	Buscar un pedido por ID
5.	Salir del programa
              """)
        opcion = input("Introduzca una opción: ").strip()
        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            listar_pedidos()
        elif opcion == "3":
            imprimir_hoja()
        elif opcion == "4":
            buscar_id()
        elif opcion == "5":
            print("Gracias por usar.")
            break
        else:
            print("Opción ingresada no válida")
            print("")
            system("pause")

if __name__ == "__main__":
    menu_principal()