# Project:
# create a bank app in which we can...
# Create an account create
# Make deposits
# Make withdrawals

class Persona: 
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre  # instance attributes 
        self.apellido = apellido
        
class Cliente (Persona):
    
    def __init__(self,nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta  # instance attributes 
        self.balance = balance
        
    def __str__(self):
        return f"EL cliente llamado {self.nombre} {self.apellido}\nTiene el numero de cuenta: {self.numero_cuenta}\ny su balacne de cuenta es: {self.balance}" 
    
    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")
        
    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficiente")
            

def crear_cliente():
    nombre_cl = input("Ingrese nombre: ")
    apellido_cl = input("Ingrese apellido: ")
    numero_cuenta = input("Ingrese el numero de cuenta: ")
    cliente = Cliente(nombre_cl,apellido_cl,numero_cuenta)
    
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    
    opcion = 0 
    
    while opcion != 'S':
        print("Elije: Depositar (D), Retirar (R), o Salir (S)") 
        opcion = input()
        
        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    
    print("Gracias por operar en Banco Python")
    
    
inicio()

