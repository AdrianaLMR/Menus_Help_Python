def mostrar_menu():
    menu = """
    ________________________________________
    |     MENU DE CONSTANTES E VARIÁVEIS   |
    |--------------------------------------|
    |   1. Definir uma constante           |
    |   2. Definir uma variável            |
    |   3. Usar constantes e variáveis     |
    |   4. Sair                            |
    |______________________________________|
    """
    print(menu)

def exemplo_constantes():
    PI = 3.14159  # Constante
    print(f"Constante PI: {PI}")

def exemplo_variaveis():
    idade = 25  # Variável
    print(f"Idade: {idade}")

def exemplo_constantes_variaveis():
    PI = 3.14159
    idade = 25
    print(f"Constante PI: {PI}")
    print(f"Idade: {idade}")

def executar_opcao(opcao):
    if opcao == "1":
        exemplo_constantes()
    elif opcao == "2":
        exemplo_variaveis()
    elif opcao == "3":
        exemplo_constantes_variaveis()
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
