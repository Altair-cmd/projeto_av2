from f_login import usuarios
from f_verifica_string import verificao_string
def mostrar_registro():
    consulta = input("Digite qual usuário você quer verificar: ")
    verificao_string(consulta)    
    for user in usuarios:
        if user['login'] == consulta:
            print(f"Seu úsuario é :",user['login'],'\n')
            print(f"Sua senha é :",user['senha'],'\n')
            print(f"Seu telefone é :  ",user['telefone'],'\n')
            print(f"Seu endereço é :  ",user['endereco'],'\n')

        else :
            print("Esse usuario não existe. Por favor tente novamente")