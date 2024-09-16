def mostrar_menu():
    menu = """
    ___________________________________________________
    |             ESTRUTURA CONDICIONAIS              |
    |-------------------------------------------------|
    |   1. Exemplo de 'if'                            |
    |   2. Exemplo de 'if-else'                       |
    |   3. Exemplo de 'if-elif-else'                  |
    |   4. Exemplo de condição aninhada               |
    |   5. Exemplo de condição com operadores lógicos |
    |   6. Sair                                       |
    |_________________________________________________|
    """
    print(menu)


def exemplo_if():
    numero = 10
    print("Número:", numero)
    if numero > 5:
        print("O número é maior que 5.")


def exemplo_if_else():
    numero = 4
    print("Número:", numero)
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")


def exemplo_if_elif_else():
    nota = 85
    print("Nota:", nota)
    if nota >= 90:
        print("Nota A")
    elif nota >= 80:
        print("Nota B")
    elif nota >= 70:
        print("Nota C")
    else:
        print("Nota D")


def exemplo_condicao_aninhada():
    idade = 20
    estudante = True
    print("Idade:", idade)
    print("Estudante:", estudante)
    if idade < 30:
        if estudante:
            print("Você é um jovem estudante.")
        else:
            print("Você é um jovem não estudante.")
    else:
        print("Você não é um jovem.")


def exemplo_condicao_logica():
    idade = 25
    salario = 3500
    print("Idade:", idade)
    print("Salário:", salario)
    if idade > 18 and salario > 3000:
        print("Você é um adulto com um bom salário.")
    elif idade <= 18 or salario <= 3000:
        print("Você é jovem ou tem um salário baixo.")
    else:
        print("Condição não atendida.")


def executar_opcao(opcao):
    if opcao == "1":
        exemplo_if()
    elif opcao == "2":
        exemplo_if_else()
    elif opcao == "3":
        exemplo_if_elif_else()
    elif opcao == "4":
        exemplo_condicao_aninhada()
    elif opcao == "5":
        exemplo_condicao_logica()
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
