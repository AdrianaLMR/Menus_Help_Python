def mostrar_menu():
    menu = """
    ________________________________________
    |           MENU PRINCIPAL             |
    |--------------------------------------|
    |   1. Exemplo de 'split'              |
    |   2. Exemplo de 'rsplit'             |
    |   3. Exemplo de 'lstrip' e 'rstrip'  |
    |   4. Exemplo de 'join'               |
    |   5. Exemplo de 'center'             |
    |   6. Exemplo de 'title'              |
    |   7. Sair                            |
    |______________________________________|
    """
    print(menu)


def exemplo_split():
    frase = "Aprendendo Python com exemplos práticos"
    print("Frase original:", frase)
    print("Resultado do 'split()':", frase.split())


def exemplo_rsplit():
    frase = "Python é incrível para desenvolver, criar, aprender"
    print("Frase original:", frase)
    print("Resultado do 'rsplit()' (limitado a 2 separações):", frase.rsplit(", ", 2))


def exemplo_lstrip_rstrip():
    frase = "   Removendo espaços à esquerda e direita   "
    print("Frase original:", repr(frase))
    print("Sem espaços à esquerda:", repr(frase.lstrip()))
    print("Sem espaços à direita:", repr(frase.rstrip()))


def exemplo_join():
    palavras = ["Python", "é", "muito", "divertido"]
    print("Lista de palavras:", palavras)
    print("Resultado do 'join()':", " ".join(palavras))


def exemplo_center():
    texto = "Menu Principal"
    print("Texto original:", texto)
    print("Texto centralizado com '#':", texto.center(40, "#"))


def exemplo_title():
    frase = "python é uma linguagem de programação popular"
    print("Frase original:", frase)
    print("Resultado do 'title()':", frase.title())


def executar_opcao(opcao):
    if opcao == "1":
        exemplo_split()
    elif opcao == "2":
        exemplo_rsplit()
    elif opcao == "3":
        exemplo_lstrip_rstrip()
    elif opcao == "4":
        exemplo_join()
    elif opcao == "5":
        exemplo_center()
    elif opcao == "6":
        exemplo_title()
    elif opcao == "7":
        print("Saindo do menu...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True


def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-7): ").strip()
        continuar = executar_opcao(opcao)
        print("\n")


if __name__ == "__main__":
    main()
