import os

def calcular_aceleracao_centripeta():

    os.system('cls' if os.name == 'nt' else 'clear')

    v = float(input("Velocidade linear (m/s): "))
    metros = 0

    medida_distancia = input("O raio será inserido em metros 'm' ou 'km'?\n1. m\n2. Km\n> ")

    if medida_distancia == "1":
        metros = float(input("Digite a distancia em metros: "))

    elif medida_distancia == "2":
        quilometros = float(input("Digite a distancia em quilometros: "))
        metros = quilometros * 1000
    
    acp = ((v ** 2) / metros)

    print(f"A Aceleração Centrípeta é {acp}m/s^2")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione o cálculo\n1. Calcular Aceleração Centrípeta")

    escolha = input("> ")

    if escolha == "1":
        calcular_aceleracao_centripeta()
        input()
    
    else:
        print("Digite uma opção válida!")
        input()