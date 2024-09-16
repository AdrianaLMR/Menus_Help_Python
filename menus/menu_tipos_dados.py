def mostrar_menu():
    menu = """
    ________________________________________
    |       MENU DE TIPOS DE DADOS         |
    |--------------------------------------|
    |   1. Inteiros (int)                  |
    |   2. Ponto flutuante (float)         |
    |   3. Strings (str)                   |
    |   4. Booleanos (bool)                |
    |   5. Listas (list)                   |
    |   6. Tuplas (tuple)                  |
    |   7. Dicionários (dict)              |
    |   8. Sair                            |
    |______________________________________|
    """
    print(menu)

def exemplo_inteiros():
    x = 10
    print(f"Tipo de x: {type(x)}, Valor: {x}")

def exemplo_float():
    x = 10.5
    print(f"Tipo de x: {type(x)}, Valor: {x}")

def exemplo_strings():
    x = "Olá, Mundo!"
    print(f"Tipo de x: {type(x)}, Valor: {x}")

def exemplo_booleanos():
    x = True
    print(f"Tipo de x: {type(x)}, Valor: {x}")

def exemplo_listas():
    x = [1, 2, 3, 4]
    print(f"Tipo de x: {type(x)}, Valor: {x}")

def exemplo_tuplas():
    x = (1, 2, 3, 4)
    print(f"Tipo de x: {type(x)}, Valor: {x}")

def exemplo_dicionarios():
    x = {"nome": "Alice", "idade": 25}
    print(f"Tipo de x: {type(x)}, Valor: {x}")

def executar_opcao(opcao):
    if opcao == "1":
        exemplo_inteiros()
    elif opcao == "2":
        exemplo_float()
    elif opcao == "3":
        exemplo_strings()
    elif opcao == "4":
        exemplo_booleanos()
    elif opcao == "5":
        exemplo_listas()
    elif opcao == "6":
        exemplo_tuplas()
    elif opcao == "7":
        exemplo_dicionarios()
    elif opcao == "8":
        print("Saindo do menu...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-8): ").strip()
        continuar = executar_opcao(opcao)
        print("\n")

if __name__ == "__main__":
    main()
