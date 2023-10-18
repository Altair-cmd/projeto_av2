import getpass
from f_login import usuarios
from f_verifica_number import verificar_number1
from f_verifica_string import verificao_string
from f_valida_endereco import valida_endereco

def registrar():
    
    print("     Observações no cadastro :    ")
    print("No LOGIN é só aceito caracteres   ")
    novo_login = input("Crie seu nome de usuário: ")
    novo_login = verificao_string(novo_login)
    print("Na senha é só aceito números   ")
    nova_senha = input("Crie seu pin: ")
    verificar_number1(nova_senha)
    print("No endereço é não pode colocar caracteres especiais ")
    novo_endereco = input("Digite seu endereço: ")
    novo_endereco = valida_endereco(novo_endereco)
    print("No Telefone é só aceito números   ")
    novo_telefone = input("Digite seu telefone: ")
    novo_telefone = verificar_number1(novo_telefone)
    novo_usuario = {
        "login": novo_login,
        "senha": nova_senha,
        "endereco": novo_endereco,
        "telefone" :novo_telefone
        
    }
    usuarios.append(novo_usuario)
    print("Parabéns, sua conta foi criada com sucesso!")