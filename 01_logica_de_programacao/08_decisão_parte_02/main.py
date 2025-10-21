# declaração de variáveis
nome = input("informe o nome:").strip().title()
idade = int(input("informe a idade:").strip())
altura = float(input("informe a altura:").strip().replace(",","."))

# verificação das condições
if idade >= 12 and altura >= 1.15:
    print(f"entrada de {nome} autorizada.")
else:
    print(f"entrada de {nome} não autorizada.")