def mostrar_menu():
    menu = """
    ________________________________________
    |          MENU DE INTERPOLAÇÃO        |
    |--------------------------------------|
    |   1. Método '%'                      |
    |   2. Método '.format()'              |
    |   3. F-strings (Python 3.6+)         |
    |   4. Concatenação simples '+'        |
    |   5. Sair                            |
    |______________________________________|
    """
    print(menu)

def exemplo_percent():
    carro = "UNO"
    cor = "Preto"
    descricao_carro = "Meu carro é um %s da cor %s." % (carro, cor)
    print(descricao_carro)

def exemplo_format():
    nome = "Adriana"
    idade = 30
    apresentacao = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
    print(apresentacao)

def exemplo_fstrings():
    produto = "Tomate"
    preco = 1.0
    nota_fiscal = f"O preço do {produto} é R${preco}"
    print(nota_fiscal)

def exemplo_concat():
    usuario = "Fulano"
    senha = 12345
    notificacao = "Nome de usuário: " + usuario + " e senha: " + str(senha)
    print(notificacao)

def executar_opcao(opcao):
    if opcao == "1":
        exemplo_percent()
    elif opcao == "2":
        exemplo_format()
    elif opcao == "3":
        exemplo_fstrings()
    elif opcao == "4":
        exemplo_concat()
    elif opcao == "5":
        print("Saindo do menu...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        continuar = executar_opcao(opcao)
        print("\n")

if __name__ == "__main__":
    main()
