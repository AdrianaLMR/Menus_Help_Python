def mostrar_menu():
    menu = """
    ________________________________________
    |     MENU DE MÉTODOS INPUT E PRINT     |
    |---------------------------------------|
    |   1. Exemplo de 'input()'             |
    |   2. Exemplo de 'print()'             |
    |   3. Usar 'input()' e 'print()'       |
    |   4. Sair                             |
    |_______________________________________|
    """
    print(menu)

def exemplo_input():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}!")

def exemplo_print():
    mensagem = "Olá, Mundo!"
    print(mensagem)

def exemplo_input_print():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print(f"Olá, {nome}! Você tem {idade} anos.")

def executar_opcao(opcao):
    if opcao == "1":
        exemplo_input()
    elif opcao == "2":
        exemplo_print()
    elif opcao == "3":
        exemplo_input_print()
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
