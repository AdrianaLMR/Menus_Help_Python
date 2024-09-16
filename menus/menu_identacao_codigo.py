def mostrar_menu():
    menu = """
    ________________________________________
    |            IDENTACAO  DE CÓDIGO       |
    |---------------------------------------|
    |   1. Exemplo de identação correta     |
    |   2. Exemplo de erro de identação     |
    |   3. Como corrigir erro de identação  |
    |   4. Sair                             |
    |_______________________________________|
    """
    print(menu)

def exemplo_indentacao_correta():
    def exemplo():
        print("Este é um exemplo de indentação correta.")
        if True:
            print("O código está corretamente indentado.")
    exemplo()

def exemplo_erro_indentacao():
    def exemplo():
    print("Este é um exemplo de erro de identação.")
        if True:
        print("A indentação está incorreta.")
    exemplo()

def corrigir_indentacao():
    def exemplo():
        print("Este é um exemplo corrigido.")
        if True:
            print("Agora a indentação está correta.")
    exemplo()

def executar_opcao(opcao):
    if opcao == "1":
        exemplo_indentacao_correta()
    elif opcao == "2":
        exemplo_erro_indentacao()
    elif opcao == "3":
        corrigir_indentacao()
    elif opcao == "4":
        print("Saindo do menu...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()
        continuar = executar_opcao(opcao)
        print("\n")

if __name__ == "__main__":
    main()
