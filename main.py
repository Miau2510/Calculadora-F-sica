import funcoes as fc
import os
import time

# Funcao Sair
def sair():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Sair ---")
    print("Encerrando processo...")
    time.sleep(1)
    print("Programa finalizado")
    time.sleep(0.5)

# Lista de Opções
opcoes = {
    "1": fc.calcular_aceleracao_centripeta,
    "2": fc.calcular_transmissao,
    "3": fc.calcular_forca_gravitacional,
    "4": fc.calcular_velocidade_media,
    "5": fc.conversao_de_distancia
}

# Loop Principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''Selecione o cálculo
1. Calcular Aceleração Centrípeta
2. Calcular Transmissão
3. Calcular Forca Gravitacional
4. Calcular Velocidade Media
5. Conversao de Distancia

0. Sair''')

    escolha = input("> ")
    # Decisões
    if escolha in opcoes:
        opcoes[escolha]()
    if escolha == "0":
        sair()
        break