class CadastroDeUsuarios:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        email = input("Digite o email do usuário: ")
        
        usuario = {
            'nome': nome,
            'idade': idade,
            'email': email
        }
        
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!\n")

    def listar_usuarios(self):
        if self.usuarios:
            print("Lista de usuários cadastrados:")
            for i, usuario in enumerate(self.usuarios, 1):
                print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
        else:
            print("Nenhum usuário cadastrado.\n")

    def buscar_usuario(self):
        nome = input("Digite o nome do usuário que deseja buscar: ")
        encontrado = False
        for usuario in self.usuarios:
            if usuario['nome'].lower() == nome.lower():
                print(f"Usuário encontrado: Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
                encontrado = True
                break
        if not encontrado:
            print("Usuário não encontrado.\n")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Cadastrar Usuário")
            print("2. Listar Usuários")
            print("3. Buscar Usuário")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.cadastrar_usuario()
            elif opcao == '2':
                self.listar_usuarios()
            elif opcao == '3':
                self.buscar_usuario()
            elif opcao == '4':
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida! Tente novamente.\n")

# Executa o programa
if __name__ == "__main__":
    cadastro = CadastroDeUsuarios()
    cadastro.menu()
