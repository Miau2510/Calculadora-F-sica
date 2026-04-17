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
    input("")

# Calcular Transmissão
def calcular_transmissao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Calculo de Transmissao (Coroa e Pinhao) ---\n")

    r1 = float(input("Raio do pinhao: "))
    f1 = float(input("Frequencia do pinhao: "))

    r2 = float(input("Raio da coroa: "))
    
    f2 = (f1 * r1) / r2
    
    print(f"A frequencia da coroa e: {f2} rps")
    input("")

# Calcular Força Gravitacional
def calcular_forca_gravitacional():

    os.system('cls' if os.name == 'nt' else 'clear')

    G = float(6.674e-11)
    print("--- Calculo de Forca Gravitacional ---\n")
    m1 = float(input("Massa do primeiro corpo (Kg): "))
    m2 = float(input("Massa do segundo corpo (Kg): "))
    r = float(input("Distância entre os centros dos corpos (m): "))
    F = (G * (m1 * m2) / r**2)
    print(f"Forca = {F} N")
    input("")

# Lista de Opções
opcoes = {
    "1": calcular_aceleracao_centripeta,
    "2": calcular_transmissao,
    "3": calcular_forca_gravitacional
}

# Loop Principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''Selecione o cálculo
1. Calcular Aceleração Centrípeta
2. Calcular Transmissão
3. Calcular Forca Gravitacional''')

    escolha = input("> ")
    # Decisões
    if escolha in opcoes:
        opcoes[escolha]()
    else:
        print("Opcao inválida")
        