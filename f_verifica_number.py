
def verificar_number1(numero):
    numero.isnumeric()
    while(numero.isnumeric()) == False:
        print("Digite um valor válido ")
        numero = (input(" "))
    numero = int(numero)
    return numero