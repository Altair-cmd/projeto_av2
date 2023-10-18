from f_login import usuarios
from f_valida_endereco import valida_endereco
from f_verifica_number import verificar_number1
from f_verifica_string import verificao_string

def atualizar_registro():
    consulta = input("Digite o nome de usuário que você deseja atualizar: ")
    encontrado = False

    for user in usuarios:
        if user['login'] == consulta:
            novo_login = input("Digite o novo nome de usuário: ")
            verificao_string(novo_login)
            nova_senha = input("Digite seu novo pin: ")
            verificar_number1(nova_senha)
            novo_endereco = input("Digite seu novo endereço: ")
            valida_endereco(novo_endereco)
            novo_telefone = input("Digite seu novo telefone: ")
            verificar_number1(novo_telefone)
            user['login'] = novo_login
            user['senha'] = nova_senha
            user['endereco']= novo_endereco
            user['senha']= nova_senha
            encontrado = True
            print("Registro atualizado com sucesso.")

    if not encontrado:
        print("Este usuário não existe na lista. Por favor, tente novamente.")