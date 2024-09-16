def mostrar_menu():
    menu = """
    __________________________________________
    |           CONVERSÃO DE TIPOS           |
    |----------------------------------------|
    |   1. Exemplo de conversão para 'int'   |
    |   2. Exemplo de conversão para 'float' |
    |   3. Exemplo de conversão para 'str'   |
    |   4. Exemplo de conversão para 'bool'  |
    |   5. Conversão de tipos complexos      |
    |   6. Sair                              |
    |________________________________________|
    """
    print(menu)


def exemplo_int():
    valor = "123"
    print("Valor original:", valor)
    print("Conversão para int:", int(valor))


def exemplo_float():
    valor = "123.45"
    print("Valor original:", valor)
    print("Conversão para float:", float(valor))


def exemplo_str():
    valor = 123
    print("Valor original:", valor)
    print("Conversão para str:", str(valor))


def exemplo_bool():
    valores = [0, 1, "", "Python"]
    for valor in valores:
        print(f"Valor original: {valor} -> Conversão para bool: {bool(valor)}")


def exemplo_conversao_complexa():
    valor = 3.14
    print("Valor original:", valor)
    print("Conversão para int (arredondado):", int(round(valor)))


def executar_opcao(opcao):
    if opcao == "1":
        exemplo_int()
    elif opcao == "2":
        exemplo_float()
    elif opcao == "3":
        exemplo_str()
    elif opcao == "4":
        exemplo_bool()
    elif opcao == "5":
        exemplo_conversao_complexa()
    elif opcao == "6":
        print("Saindo do menu...")
        return False
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 6.")
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
