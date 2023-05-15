import requests
import os
from random import seed
from random import random
from datetime import datetime

#---------validar moneda
def esmoneda(cripto):
    return cripto in monedas

#---------llena Balance
def llenarBalance(usuario, balance):
    criptoMoneda = input("Ingrese Criptomoneda del usuario " + str(usuario) + ": ")
    if esmoneda(criptoMoneda):
        saldo = int(input("Ingrese saldo del usuario " + str(usuario) +" en " + criptoMoneda + ": "))
        balance[criptoMoneda]=saldo
    else:
        print("Criptomoneda no válida")
    otraCripto=input("Desea ingresar otra criptomoneda? (si, no): ")
    if otraCripto.upper() == "SI":
        llenarBalance(usuario,balance)

#---------Lista usuarios
def listaUsuarios():
    print("Lista de usuarios: ")
    for usuario in list(usuariosDict.keys()):
        print(str(usuario))

#---------Menu
def menu():
    opc = int(input("Menú Principal \n" +
                    "1. Recibir Monto \n" +
                    "2. Transferir Monto \n" +
                    "3. Balance de Moneda \n" +
                    "4. Balance General \n" +
                    "5. Histórico de Transacciones \n" +
                    "6. Salir \n" +
                    "Escoja una opción: \n"))
    return opc

#---------Recibir
def recibir():
    listaUsuarios()
    validarCodigo=int(input("Seleccionar de que usuario desea recibir: "))
    os.system("cls")
    if validarCodigo in list(usuariosDict.keys()) and validarCodigo != usuarioPropio:
        validarMoneda=input("¿Qué moneda desea recibir?: ")
        os.system("cls")
        if esmoneda(validarMoneda) and validarMoneda in list(usuariosDict[validarCodigo].keys()):
            cantidadMon=int(input("¿Cuánto desea recibir?: "))
            os.system("cls")
            if validarMoneda in list(usuariosDict[int(usuarioPropio)].keys()):
                if usuariosDict[int(usuarioPropio)][validarMoneda] >= cantidadMon:
                    usuariosDict[int(usuarioPropio)][validarMoneda]=usuariosDict[int(usuarioPropio)][validarMoneda] + cantidadMon
                    usuariosDict[int(validarCodigo)][validarMoneda]=usuariosDict[int(validarCodigo)][validarMoneda] - cantidadMon
                    valorDolar=(cantidadMon)*(monedasDict[validarMoneda])
                    transacciones(usuarioPropio,"Recepción", validarMoneda, cantidadMon, valorDolar)
                    transacciones(validarCodigo,"Transferencia", validarMoneda, cantidadMon, valorDolar)
                else:
                    print("El usuario " + str(validarCodigo) + " no tiene saldo suficiente de " + validarMoneda)
                    print(" ")
            else:
                usuariosDict[int(usuarioPropio)][validarMoneda]=cantidadMon
                usuariosDict[int(validarCodigo)][validarMoneda]=usuariosDict[int(validarCodigo)][validarMoneda] - cantidadMon
                valorDolar=(cantidadMon)*(monedasDict[validarMoneda])
                transacciones(usuarioPropio,"Recepción", validarMoneda, cantidadMon, valorDolar)
                transacciones(validarCodigo,"Transferencia", validarMoneda, cantidadMon, valorDolar)
        else:
            print("Moneda no válida o el usuario del que desea recibir no tiene dicha moneda")
            print(" ")
    else:
        print("El usuario ingresado no existe o es el mismo usuario propio")
        print(" ")

#---------Transferir
def transferir():
    listaUsuarios()
    validarCodigo=int(input("Seleccionar a que usuario desea transferir: "))
    os.system("cls")
    if validarCodigo in list(usuariosDict.keys()) and validarCodigo != usuarioPropio:
        validarMoneda=input("¿Qué moneda desea transferir?: ")
        os.system("cls")
        if esmoneda(validarMoneda) and validarMoneda in list(usuariosDict[validarCodigo].keys()):
            cantidadMon=int(input("¿Cuánto desea transferir?: "))
            os.system("cls")
            if validarMoneda in list(usuariosDict[int(usuarioPropio)].keys()):
                if usuariosDict[int(usuarioPropio)][validarMoneda] >= cantidadMon:
                    usuariosDict[int(usuarioPropio)][validarMoneda]=usuariosDict[int(usuarioPropio)][validarMoneda] - cantidadMon
                    usuariosDict[int(validarCodigo)][validarMoneda]=usuariosDict[int(validarCodigo)][validarMoneda] + cantidadMon
                    valorDolar=(cantidadMon)*(monedasDict[validarMoneda])
                    transacciones(usuarioPropio,"Transferencia", validarMoneda, cantidadMon, valorDolar) 
                    transacciones(validarCodigo,"Recepción", validarMoneda, cantidadMon, valorDolar)
                else:
                    print("El usuario " + str(usuarioPropio) + " no tiene saldo suficiente de " + validarMoneda)
                    print(" ")
            else:
                    usuariosDict[int(usuarioPropio)][validarMoneda]=cantidadMon
                    usuariosDict[int(validarCodigo)][validarMoneda]=usuariosDict[int(validarCodigo)][validarMoneda] + cantidadMon
                    valorDolar=(cantidadMon)*(monedasDict[validarMoneda])
                    transacciones(usuarioPropio,"Transferencia", validarMoneda, cantidadMon, valorDolar) 
                    transacciones(validarCodigo,"Recepción", validarMoneda, cantidadMon, valorDolar)    
        else:
            print("Moneda no válida o el usuario al que desea transferir no tiene dicha moneda")
            print(" ")
    else:
        print("El usuario ingresado no existe o es el mismo usuario propio")
        print(" ")

#---------Balance de Moneda
def balanceMoneda():
    validarCodigo=int(input("Seleccionar usuario: "))
    os.system("cls")
    if validarCodigo in list(usuariosDict.keys()):
        validarMoneda=input("¿De qué moneda desea verificar el balance?: ")
        os.system("cls")
        if esmoneda(validarMoneda) and validarMoneda in list(usuariosDict[validarCodigo].keys()):
            print("El usuario " + str(validarCodigo) + " tiene: ")
            print(" ")
            if validarMoneda in list(usuariosDict[validarCodigo].keys()):
                valorDolar=(usuariosDict[validarCodigo][validarMoneda])*(monedasDict[validarMoneda])
                print(validarMoneda + ": " + str(usuariosDict[validarCodigo][validarMoneda])  + " / " + " USD: "+ ('%.2f' % valorDolar))
                print(" ")
                transacciones(validarCodigo,"Consulta Moneda", validarMoneda, 0, 0)
        else:
            print("Moneda no válida o el usuario al que desea transferir no tiene dicha moneda")
            print(" ")
    else:
        print("El usuario ingresado no existe o es el mismo usuario propio")
        print(" ")

#---------Balance General
def balanceGeneral():
    validarCodigo=int(input("Seleccionar usuario: "))
    os.system("cls")
    if validarCodigo in list(usuariosDict.keys()):
        print("El usuario " + str(validarCodigo) + " tiene: ")
        print(" ")
        for criptoBalance in list(usuariosDict[validarCodigo].keys()):
            valorDolar=(usuariosDict[validarCodigo][criptoBalance])*(monedasDict[criptoBalance])
            print(criptoBalance + ": " + str(usuariosDict[validarCodigo][criptoBalance])  + " / " + " USD: "+ ('%.2f' % valorDolar))
        print(" ")
        transacciones(validarCodigo,"Consulta General", criptoBalance, 0, 0)
    else:
        print("El usuario no existe")
        print(" ")

#---------Crear Usuario
def crearUsuarios():
    cantidadUsuario = int(input("Ingrese cantidad de usuarios (max. 5): "))

    for contUsuarios in range(cantidadUsuario):
        if cantidadUsuario > 5:
            print("No se pueden más de 5")
            break
        balance={}
        seed()
        codigoUsuario = int(random()*1000)
        llenarBalance(contUsuarios+1,balance)
        usuariosDict[codigoUsuario]=balance
        contUsuarios=contUsuarios+1   
    if cantidadUsuario > 5:
        crearUsuarios()
    os.system("cls")

#---------Transacciones
def transacciones(usuario,transaccion,cripto,valor,valorusd):
    listaTrans=[]
    if int(usuario) in list(transaccionesDict.keys()):
        listaTrans = transaccionesDict[int(usuario)]

    nuevaTrans=""
    datos = datetime.now()
    hora = datos.strftime("%A %d/%m/%Y %I:%M:%S %p")
    
    if transaccion == "Transferencia":
        nuevaTrans="Realizó una transferencia por " +  str(valor) + " " + cripto + " / USD " + str('%.2f' % valorusd) + " , " + "Fecha y hora: " + str(hora)
    if transaccion == "Recepción":
        nuevaTrans="Recibió " +  str(valor) + " " + cripto + ", USD " + str('%.2f' % valorusd) + " / " + "Fecha y hora: " + str(hora)
    if transaccion == "Consulta Moneda":
        nuevaTrans="Realizó consulta de " +  cripto  + ", " "Fecha y hora: " + str(hora)
    if transaccion == "Consulta General":
        nuevaTrans="Realizó consulta general" + ", " "Fecha y hora: " + str(hora)
    listaTrans.append(nuevaTrans)
    transaccionesDict[int(usuario)] = listaTrans

#---------Historial Transacciones
def historialTransacciones():
    validarCodigo=int(input("Seleccionar usuario: "))
    os.system("cls")
    if validarCodigo in list(usuariosDict.keys()):
        listaTrans=[]
        if validarCodigo in list(transaccionesDict.keys()):
            print("Historial de transacciones del usuario " + str(validarCodigo) + ": ")
            print(" ") 
            listaTrans = transaccionesDict[validarCodigo] 
            for trans in listaTrans:
                print(trans)
        else:
            print("Este usuario no ha realizado transacciones")
            print(" ")
    else:
        print("Usuario no existente")
        print(" ")

#---------Declaracion variables
monedas=()
monedasDict={}
usuariosDict={}
transaccionesDict={}
saldo=0
criptoMoneda=""
contUsuarios=0
usuarioPropio=0
opcion=0

#---------Consulta HTTP
COINMARKET_API_KEY = "f632d18d-5bbb-4d9a-a19b-1c52d8d13e10"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
    monedasDict[cripto["name"]]=cripto["quote"]["USD"]["price"]
monedas = monedasDict.keys() 

#----------------------------------------------------------------------------------------------------
crearUsuarios()
listaUsuarios()
usuarioPropio=input("Mi usuario es: ")
os.system("cls")

while opcion != 6:
    opcion = menu()
    if opcion == 1:
        recibir()
    if opcion == 2:
        transferir()
    if opcion == 3:
        listaUsuarios()
        balanceMoneda()
    if opcion == 4:
        listaUsuarios()
        balanceGeneral()
    if opcion == 5:
        listaUsuarios()
        historialTransacciones()
        print(" ")