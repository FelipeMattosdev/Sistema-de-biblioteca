def cadastro_usuario():
    try:
        novo_nome = input("Digite o seu nome de usuário: ") 
        nova_senha = input("Digite a sua senha: ")
        Login_nome.append(novo_nome)
        login_senha.append(nova_senha)
        print("Cadastro realizado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o cadastro: {e}")

def novo_cadastro():
    try:
        cadastro_usuario()
        menu1()  # Após o cadastro, voltamos para a tela de login
    except Exception as e:
        print(f"Ocorreu um erro durante o novo cadastro: {e}")

def fazer_login(): ##nessa def faz processo de login onde verifica se usuario e senha consta na area de cadastro de usuario. caso conste ele vai para proxima etapa d  codigo.
    try:
        nome = input("Digite o seu nome de usuário: ")
        senha = input("Digite a sua senha: ")
        if nome in Login_nome:
            index = Login_nome.index(nome)
            if senha == login_senha[index]:
                print("Login bem sucedido!")
                menu2()  # Após o login, vai para o menu principal
            else:
                print("Senha incorreta.")
        else:
            print("Nome de usuário incorreto.")
    except Exception as e:
        print(f"Ocorreu um erro durante o login: {e}")

def buscaBinaria(lista, chave):
    try:
        inicio = 0
        fim = len(lista) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if lista[meio] == chave:
                return meio
            elif lista[meio] > chave:
                fim = meio - 1
            else:
                inicio = meio + 1

        return -1
    except Exception as e:
        print(f"Ocorreu um erro durante a busca binária: {e}")
        return -1  # Retorna -1 em caso de erro

def listar_livros():
    try:
        print("Lista de Livros Disponíveis:") #printa os livors disponives 
        for livro in livros: #pecorre a lista de livros
            print(f"- {livro}")
    except Exception as e:
        print(f"Ocorreu um erro ao listar os livros: {e}") #qualquer exeção que venha ocorrer no codigo ele informa que houve erro

def menu2(): # menu 2 onde apos o usuario se autenticado aparece novas opções.
    try:
        while True:
            print('''
                MENU:

                [1] - Buscar Livros
                [2] - Listar Usuários Cadastrados
                [3] - Cadastrar Livros
                [4] - Sair
            ''')
            escolha = input('Escolha uma opção: ')

            if escolha == "1":
                procurado = input("Digite o nome do livro completo que deseja buscar: ")
                resultado = buscaBinaria(livros, procurado)
                if resultado == -1:
                    print("Livro não encontrado.")
                else:
                    print(f"O livro '{procurado}' está na posição {resultado}.")
            elif escolha == "2":
                print("Usuários cadastrados:")
                for usuario in Login_nome:
                    print(f"- {usuario}")
            elif escolha == "3":
                listar_livros()
            elif escolha == "4":
                print("Obrigado por utilizar a Biblioteca Virtual.")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")
    except Exception as e:#caso usuario digite algo fora do padrão printa msg de abaixo
        print(f"Ocorreu um erro no menu principal: {e}")

def menu1(): #menu inicial onde programa iniciar, dando a seguintes opções abaixo para usuario 
    try:
        while True:
            print('''
                MENU:

                [C] - Novo Cadastro 
                [L] - Fazer login
                [S] - Sair
            ''')
            escolha = input('Escolha uma opção: ')

            if escolha.lower() == "c":
                novo_cadastro()
            elif escolha.lower() == "l":
                fazer_login()
            elif escolha.lower() == "s":
                print("Obrigado por utilizar a Biblioteca Virtual!")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")
    except Exception as e:
        print(f"Ocorreu um erro no menu inicial: {e}")

# Listas para armazenamento de dados
Login_nome = []  # Lista dos nomes dos usuários cadastrados
login_senha = []  # Lista das senhas dos usuários cadastrados
livros = [
    "A Menina que Roubava Livros",
    "Dom Casmurro",
    "Harry Potter e a Pedra Filosofal",             #lista de livros cadastrados.
    "O Hobbit",
    "O Senhor dos Anéis",
    "O Pequeno Príncipe",
    "Orgulho e Preconceito",
    "Percy Jackson e o Ladrão de Raios",
    "As Crônicas de Nárnia",
    "As Aventuras de Sherlock Holmes"
]

# Início do programa
menu1()
