from f_login import usuarios
from f_verifica_string import verificao_string
encontrado = bool

def deletar_registro():
    consulta = input("Digite o nome de usuário que você deseja excluir: ")
    encontrado = False
    for user in usuarios:
       
        if user['login'] == consulta:
            usuarios.remove(user) 
            encontrado = True
            print("Usuário deletado com sucesso.")

        if not encontrado:
           print("Este usuário não existe na lista. Por favor, tente novamente.")
