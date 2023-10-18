# Criar listas vazias para armazenar informações de login e senha
from f_login import realizar_login
from f_registrar import registrar
from f_printar import mostrar_registro
from f_deletar import deletar_registro
from f_atualiza import atualizar_registro
from f_verifica_number import verificar_number1


# Menu principal


while True:
    print("------ Menu ------")
    print("1 - Login")
    print("2 - Registrar")
    print("3 - Mostrar registro")
    print("4 - Deletar registro")
    print("5- Atualizar registro ")
    print("6 - sair")
    
    escolha = input("Digite sua escolha: ")
    verificar_number1(escolha)
    
    if escolha == '1':
        realizar_login()
    elif escolha == '2':
        registrar()
    elif escolha == '3':
        mostrar_registro()
    elif escolha == '4':
        deletar_registro()
    elif escolha == '5':
        atualizar_registro()
    elif escolha == '6':
        print("Até logo!")
        break
    else:
        print("Escolha inválida. Por favor, digite uma das opções diponíveis.")