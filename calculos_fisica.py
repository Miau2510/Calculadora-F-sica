import os

def calcular_aceleracao_centripeta():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Calculo de Aceleração Centrípeta ---\n")

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

def calcular_transmissao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Calculo de Transmissao (Coroa e Pinhao) ---\n")

    r1 = float(input("Raio do pinhao: "))
    f1 = float(input("Frequencia do pinhao: "))

    r2 = float(input("Raio da coroa: "))
    
    f2 = (f1 * r1) / r2
    
    print(f"A frequencia da coroa e: {f2} rps")
    print("-" * 45)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione o cálculo\n1. Calcular Aceleração Centrípeta\n2. Calcular Transmissão")

    escolha = input("> ")

    if escolha == "1":
        calcular_aceleracao_centripeta()
        input()
    
    elif escolha == "2":
        calcular_transmissao()
        input()
    
    else:
        print("Digite uma opção válida!")
        input()