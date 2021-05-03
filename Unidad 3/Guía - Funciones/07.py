print("******LOGIN*****")
usuario = str
contraseña = str
intentos = 0

def login(usuario,contraseña):
    if usuario == "usuario1" and contraseña == "asdasd":
        print("Ingreso correcto")
    
print("Solo tiene 3 intentos para ingresar.")
while intentos < 3:
    usuario = input("Ingrese ususario: ")
    contraseña = input("Ingrese contraseña: ")
    intentos = intentos + 1
    login(usuario,contraseña)
