import json



def abrirArchivo():
    with open("info.json", encoding="utf-8") as file:
        usuario = json.load(file)
        return usuario
    



def abrirArchivoServicio():
    with open("otro.json", encoding="utf-8") as file2:
        ver = json.load(file2)
        return ver
    
    
def abrirRegulares():
     with open("regulares.json", encoding="utf-8") as file:
        regulares = json.load(file)
        return regulares
    
def guardarArchivo(file):
    with open("./info.json","w") as file:
        guardado = json.dump(file)
        return guardado
    
    
usuario = abrirArchivo()
ver = abrirArchivoServicio() 
regulares = abrirRegulares()
#usuario = []
#ver = []
#regulares = []




def crearUsuario(usuario):
    
    
    id = int(input("Ingrese id: "))
    nombre = input("Nombre: ")
    apellido = input("apellido: ")
    cedula = int(input("cedula: "))
    direccion = input("Direccion: ")




    usuario[0]["nuevos"].append({
                "id": id,
                "nombre": nombre,
                "apellido": apellido,
                "cedula": cedula,
                "direccion": direccion,
                "tipoCliente": "Nuevo",
                "servicio": "post pago"}
        )
    usuario = guardarArchivo(usuario)
    print("guardado")
   


def verUsuarios(usuario):
    for i in usuario[0]["nuevos"]:
        print(f"ID. {i["id"]}")
        print(f"Nombre: {i["nombre"]}")
        print(f"Apellido:{i["apellido"]}")
        print(f"Cedula: {i["cedula"]}")
        print(f"Direccion: {i["direccion"]}")
        print(f"Cliente: {i["tipoCliente"]}")
        print(f"Plan: {i["servicio"]}")
    

def planes(ver):
    for i in ver[0]["servicios"]:
        print(f"Plan: {i["plan1"]} Precio: ${i["precios"][0]["precio1"]}")
        print(f"Plan. {i["plan2"]} Precio: ${i["precios"][0]["precio2"]}")
        print(f"Plan: {i["plan3"]} Precio: ${i["precios"][0]["precio3"]}")

def eliminar(usuario):
    usuario = abrirArchivo()
    a = int(input("ingrese ID: a eliminar"))
    for i in usuario[0]["nuevos"]:
        if a == i["id"]:
            del usuario[0]["nuevos"]
        
def archivoRegular(regulares):
    for i in regulares[0]["regulares"]:
        print(f"ID. {i["id"]}")
        print(f"Nombre: {i["nombre"]}")
        print(f"Apellido:{i["apellido"]}")
        print(f"Cedula: {i["cedula"]}")
        print(f"Direccion: {i["direccion"]}")
        print(f"Plan: {i["plan"]}")

        

opcion = int(input("Ingrese: 1. registrar\n2. ver: \n3. planes: \n4. Eliminar Usuario: \n5. clientes regulares: "))
def menu():

    if opcion == 1:
        crearUsuario(usuario)
        

    if opcion == 2:
        verUsuarios(usuario)
    elif opcion == 3:
        planes(ver)
    elif opcion ==4:
        eliminar(usuario)
    elif opcion == 5:
        archivoRegular(regulares)
        
    else:
        print("Opcion Invalida")

    
    

menu()
    