# tratamento de exceção
try:
    # entrada de dados
    numero = int(input("informe um número inteiro:").strip())
    
    # laço de repetição
    while numero >= 0:
        print(numero)
        numero -= 1
except:
    print("não foi possível executar o contador.")
