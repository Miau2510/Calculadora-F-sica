import funcoes as fc
import os
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
5. Conversao de Distancia''')

    escolha = input("> ")
    # Decisões
    if escolha in opcoes:
        opcoes[escolha]()