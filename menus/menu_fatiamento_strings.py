def mostrar_menu():
    
    menu =  """
        ________________________________________________________________
        |     Escolha uma opção para ver exemplos de                    |             
        |              fatiamento de strings:                           |
        |---------------------------------------------------------------|
        |    1. Fatiamento Simples                                      |         
        |    2. Omissão de Índices                                      |         
        |    3. Uso do Passo                                            |     
        |    4. Fatiamento Reverso                                      |         
        |    5. Fatiamento Negativo                                     |         
        |    6. Sair                                                    |
        |_______________________________________________________________|         
        """
    print(menu)

def mostrar_exemplo(opcao):
    """
    Exibe um exemplo baseado na opção escolhida.
    """
    if opcao == "1":
        print(
            """
            Fatiamento Simples:
            Você pode extrair uma parte específica da string usando índices.

            Exemplo:
            texto = "Python é divertido"
            print(texto[0:6])  # 'Python'
            """
        )
    elif opcao == "2":
        print(
            """
            Omissão de Índices:
            Você pode omitir o índice inicial ou final para obter substrings a partir do início ou até o final da string.

            Exemplo:
            texto = "Python é divertido"
            print(texto[:6])  # 'Python'
            print(texto[7:])  # 'é divertido'
            """
        )
    elif opcao == "3":
        print(
            """
            Uso do Passo:
            O passo pode ser utilizado para obter substrings com intervalos específicos.

            Exemplo:
            texto = "Python é divertido"
            print(texto[::2])  # 'Pto  eivn'
            """
        )
    elif opcao == "4":
        print(
            """
            Fatiamento Reverso:
            Use um passo negativo para reverter a string.

            Exemplo:
            texto = "Python é divertido"
            print(texto[::-1])  # 'odivnuf é nohtyP'
            """
        )
    elif opcao == "5":
        print(
            """
            Fatiamento Negativo:
            Índices negativos permitem contar a partir do final da string.

            Exemplo:
            texto = "Python é divertido"
            print(texto[-11:-1])  # 'divertido'
            """
        )
    elif opcao == "6":
        print("Saindo do programa...")
        return False
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 6.")
    
    return True

def main():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção desejada: ").strip()
        
        if not mostrar_exemplo(opcao):
            break

        refazer = input("Deseja ver outra opção? (s/n): ").strip().lower()
        if refazer != "s":
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    main()
