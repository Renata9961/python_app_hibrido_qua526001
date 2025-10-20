# declaração de variáveis
nome = input("informe seu nome:").strip().title()
idade = int(input("informe sua idade:"))
altura = float(input("informe sua altura:").replace(",","."))

# saída de dados
print(f"nome do usuário: {nome}. Tipo: {type(nome)}")
print(f"idade: {idade}. Tipo {type(idade)}")
print(f"altura: {altura} metro. Tipo: {type(altura)}")