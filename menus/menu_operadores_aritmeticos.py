def mostrar_menu():
    menu = """
    ________________________________________
    |     MENU DE OPERADORES ARITMÉTICOS   |
    |--------------------------------------|
    |   1. Adição (+)                      |
    |   2. Subtração (-)                   |
    |   3. Multiplicação (*)               |
    |   4. Divisão (/)                     |
    |   5. Modulo (%)                      |
    |   6. Sair                            |
    |______________________________________|
    """
    print(menu)

def exemplo_adicao():
    a, b = 5, 3
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

def exemplo_subtracao():
    a, b = 5, 3
    resultado = a - b
    print(f"{a} - {b} = {resultado}")

def exemplo_multiplicacao():
    a, b = 5, 3
    resultado = a * b
    print(f"{a} * {b} = {resultado}")

def exemplo_divisao():
    a, b = 5, 3
    resultado = a / b
    print(f"{a} / {b} = {resultado}")

def exemplo_modulo():
    a, b = 5, 3
    resultado = a % b
    print(f"{a} % {b} = {resultado}")

def executar_opcao(opcao):
    if opcao == "1":
        exemplo_adicao()
    elif opcao == "2":
        exemplo_subtracao()
    elif opcao == "3":
        exemplo_multiplicacao()
    elif opcao == "4":
        exemplo_divisao()
    elif opcao == "5":
        exemplo_modulo()
    elif opcao == "6":
        print("Saindo do menu...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-6): ").strip()
        continuar = executar_opcao(opcao)
        print("\n")

if __name__ == "__main__":
    main()
