usuarios = list()
from f_verifica_number import verificar_number1
from f_verifica_string import verificao_string


def realizar_login():
    print("Em seu login digite somente letras")
    input_login = input("Digite seu nome de usuário: ")
    verificao_string(input_login)
    print("Em sua senha digite somente números")
    input_senha = input("Digite sua senha: ")
    verificar_number1(input_senha)
    
    for user in usuarios:
        if user['login'] == input_login and user['senha'] == input_senha:
            print("Login realizado com sucesso!")
            
        else:
            print("Usuário ou senha incorretos. Por favor, tente novamente.")