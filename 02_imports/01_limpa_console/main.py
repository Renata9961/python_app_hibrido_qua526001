# importação de bibliotecas
import os

# loop
while True:
    # limpeza de console
    os.system("cls")

    # tratamento de exceção
    try:
        # entrada de dados
        nome = input("informe o seu nome:").strip().title()
        email = input("informe o e-mail:").strip().lower()
        cpf = input("informe o cpf:").strip()

        # limpeza de console
        os.system("cls")

        # saída de dados
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")

        # menu
        print("1 - inserir novos dados.")
        print("2 - sair do programa.")
        opcao = input("opção desejada:").strip()

        # verifica a opção escolhida
        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break
    except:
                print("não foi possível receber informações.")

