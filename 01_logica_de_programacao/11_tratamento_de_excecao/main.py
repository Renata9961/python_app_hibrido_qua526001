# tratamento de exceção
try:
    # entrada de dados
    nome = input("informe seu nome:").strip().title()
    idade = int(input("informe sua idade:").strip())
    altura = float(input("informe sua altura:"))

    # saída de dados
    print(f"nome:{nome}")
    print(f"idade:{idade}")
    print(f"altura:{altura}")
except:
    print("infelizmente o programa não pode ser execultado.")