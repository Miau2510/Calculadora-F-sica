import os
# Aceleração Centrípeta
def calcular_aceleracao_centripeta():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Calculo de Aceleração Centrípeta ---\n")

    v = float(input("Velocidade linear (m/s): "))
    metros = 0

    medida_distancia = input("O raio será inserido em metros 'm' ou 'km'?\n1. m\n2. Km\n> ")

    if medida_distancia == "1" or medida_distancia == "m":
        metros = float(input("Digite a distancia em metros: "))
        print("Erro: Digite apenas numeros")
    elif medida_distancia == "2" or medida_distancia == "km":
        quilometros = float(input("Digite a distancia em quilometros: "))
        metros = quilometros * 1000
        print("Erro: Digite apenas numeros")
    
    acp = ((v ** 2) / metros)

    print(f"A Aceleração Centrípeta é {acp}m/s^2")

# Calcular Transmissão
def calcular_transmissao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Calculo de Transmissao (Coroa e Pinhao) ---\n")

    r1 = float(input("Raio do pinhao: "))
    f1 = float(input("Frequencia do pinhao: "))

    r2 = float(input("Raio da coroa: "))
    
    f2 = (f1 * r1) / r2
    
    print(f"A frequencia da coroa e: {f2} rps")
    print("-" * 45)



# Lista de Opções
opcoes = {
    "1": calcular_aceleracao_centripeta,
    "2": calcular_transmissao
}

# Loop Principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Selecione o cálculo\n1. Calcular Aceleração Centrípeta\n2. Calcular Transmissão")

    escolha = input("> ")
    # Decisões
    if "1" in opcoes:
        opcoes['1']()
    elif "2" in opcoes:
        opcoes['2']()
    else:
        print("Opcao inválida")
        