def mostrar_menu_principal():
    menu = """
    ________________________________________
    |           MENU PRINCIPAL              |
    |---------------------------------------|
    |   1.   Constantes e Variáveis         |   
    |   2.   Conversão de Tipos             |
    |   3.   Estruturas Condicionais        |
    |   4.   Fatiamento de Strings          |
    |   5.   Identação de Código            |
    |   6.   Métodos 'input()' e 'print()'  |
    |   7.   Interpolação de Strings        |
    |   8.   Métodos de Strings             |
    |   9.   Operadores Aritméticos         |
    |   10.  Strings Múltiplas Linhas       |
    |   11.  Tipos de Dados                 |
    |   12.  Sair                           |
    |_______________________________________|
    """
    print(menu)

def executar_opcao_principal(opcao):
    if opcao == "1":
        from menus import menu_const_var
        menu_const_var.main()
    elif opcao == "2":
        from menus import menu_conversao_tipos
        menu_conversao_tipos.main()
    elif opcao == "3":
        from menus import menu_estruturas_condicionais
        menu_estruturas_condicionais.main()
    elif opcao == "4":
        from menus import menu_fatiamento_strings
        menu_fatiamento_strings.main()
    elif opcao == "5":
        from menus import menu_identacao_codigo
        menu_identacao_codigo.main()
    elif opcao == "6":
        from menus import menu_input_print
        menu_input_print.main()
    elif opcao == "7":
        from menus import menu_interpolacao_string
        menu_interpolacao_string.main()
    elif opcao == "8":
        from menus import menu_metodos_strings
        menu_metodos_strings.main()
    elif opcao == "9":
        from menus import menu_operadores_aritmeticos
        menu_operadores_aritmeticos.main()
    elif opcao == "10":
        from menus import menu_strings_multiplas_linhas
        menu_strings_multiplas_linhas.main()
    elif opcao == "11":
        from menus import menu_tipos_dados
        menu_tipos_dados.main()
    elif opcao == "12":
        print("Saindo do programa...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu_principal()
        opcao = input("Escolha uma opção (1-12): ").strip()
        continuar = executar_opcao_principal(opcao)
        print("\n")

if __name__ == "__main__":
    main()
