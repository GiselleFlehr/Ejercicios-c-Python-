texto = ""
def EscribirCentrado(texto):
    texto = (input("Ingrese un texto: "))
    print(" " * int(40 - (len(texto)/2)),texto)
    print(" " * int(40 - (len(texto)/2)),"=" * len(texto))

EscribirCentrado(texto)
