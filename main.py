from app.database import criar_tabelas  # importa a função para criar as tabelas do banco


def exibir_menu_principal():
    """Exibe as opções do menu inicial e retorna a escolha do usuário."""
    print("\n=== Caixa Bancário ===")
    print("1. Cadastrar cliente / abrir conta")
    print("2. Acessar conta")
    print("0. Sair")
    return input("Escolha uma opção: ").strip()


def main():
    """Ponto de entrada da aplicação."""
    criar_tabelas()  # garante que as tabelas existam antes de iniciar o menu

    while True:
        opcao = exibir_menu_principal()

        if opcao == "1":
            print("\n Fluxo de cadastro de cliente e abertura de conta.")
        elif opcao == "2":
            print("\n Fluxo de acesso à conta.")
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
