def mostrar_menu():
    menu = """
    _________________________________________
    |    MENU DE STRINGS MÚLTIPLAS LINHAS    |
    |----------------------------------------|
    |   1. Exemplo de aspas triplas simples  |
    |   2. Exemplo de aspas triplas duplas   |
    |   3. Usar strings múltiplas linhas     |
    |   4. Sair                              |
    |________________________________________|
    """
    print(menu)

def exemplo_aspas_triplas_simples():
    texto = '''Este é um exemplo de string
com aspas triplas simples.
Ela permite múltiplas linhas.'''
    print(texto)

def exemplo_aspas_triplas_duplas():
    texto = """Este é um exemplo de string
com aspas triplas duplas.
Ela também permite múltiplas linhas."""
    print(texto)

def exemplo_usar_strings_multiplas_linhas():
    texto = """Este é um texto de exemplo
utilizando strings múltiplas linhas com
a formatação mantida e quebras de linha
preservadas."""
    print(texto)

def executar_opcao(opcao):
    if opcao == "1":
        exemplo_aspas_triplas_simples()
    elif opcao == "2":
        exemplo_aspas_triplas_duplas()
    elif opcao == "3":
        exemplo_usar_strings_multiplas_linhas()
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
