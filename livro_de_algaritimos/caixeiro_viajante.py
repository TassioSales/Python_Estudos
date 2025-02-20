import matplotlib.pyplot as plt
import numpy as np
import random

# 📌 Dicionário com cidades brasileiras e suas coordenadas aproximadas (latitude, longitude)
cidades = {
    "São Paulo": (-23.5505, -46.6333),
    "Rio de Janeiro": (-22.9068, -43.1729),
    "Belo Horizonte": (-19.9167, -43.9345),
    "Salvador": (-12.9714, -38.5014),
    "Brasília": (-15.8267, -47.9218),
    "Fortaleza": (-3.7172, -38.5433),
    "Curitiba": (-25.4284, -49.2733),
    "Recife": (-8.0476, -34.8770),
    "Porto Alegre": (-30.0346, -51.2177),
    "Manaus": (-3.1190, -60.0217),
    "Belém": (-1.4558, -48.5039),
    "Goiânia": (-16.6864, -49.2643),
    "São Luís": (-2.5387, -44.2823),
    "Maceió": (-9.6659, -35.7350),
    "Natal": (-5.7945, -35.2110),
    "Teresina": (-5.0892, -42.8013),
    "João Pessoa": (-7.1150, -34.8641),
    "Aracaju": (-10.9472, -37.0731),
    "Cuiabá": (-15.6010, -56.0978),
    "Campo Grande": (-20.4420, -54.6463)
}


def calcular_distancia(cidade1, cidade2):
    """Calcula a distância euclidiana entre duas cidades."""
    x1, y1 = cidade1
    x2, y2 = cidade2
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def caixeiro_viajante_vizinho_mais_proximo(cidades):
    """
    Resolve o problema do caixeiro viajante utilizando o algoritmo do vizinho mais próximo.

    Estratégia:
    1. Escolhe uma cidade inicial aleatória.
    2. Encontra a cidade mais próxima não visitada e a adiciona ao caminho.
    3. Repete até visitar todas as cidades.
    4. Retorna à cidade inicial para fechar o ciclo.
    """
    cidades_lista = list(cidades.keys())
    cidade_atual = random.choice(cidades_lista)  # Escolhe aleatoriamente uma cidade inicial
    caminho = [cidade_atual]  # Lista para armazenar a sequência de cidades visitadas
    nao_visitadas = set(cidades_lista)  # Conjunto com as cidades ainda não visitadas
    nao_visitadas.remove(cidade_atual)  # Remove a cidade inicial da lista de não visitadas
    distancia_total = 0  # Inicializa a distância total percorrida

    while nao_visitadas:
        # Escolhe a cidade mais próxima da cidade atual
        proxima_cidade = min(nao_visitadas,
                             key=lambda cidade: calcular_distancia(cidades[cidade_atual], cidades[cidade]))
        distancia_total += calcular_distancia(cidades[cidade_atual], cidades[proxima_cidade])
        caminho.append(proxima_cidade)  # Adiciona ao caminho
        nao_visitadas.remove(proxima_cidade)  # Marca como visitada
        cidade_atual = proxima_cidade  # Atualiza a cidade atual

    # Volta para a cidade inicial para completar o ciclo
    distancia_total += calcular_distancia(cidades[caminho[-1]], cidades[caminho[0]])
    return caminho, distancia_total


def desenhar_caminho(caminho, cidades):
    """
    Desenha o percurso do caixeiro viajante em um gráfico usando Matplotlib.

    Melhoria visual:
    - Cada cidade recebe um número indicando a ordem da visita.
    - O primeiro e o último ponto são destacados com cores diferentes.
    - As conexões entre as cidades são traçadas para mostrar o caminho percorrido.
    """
    plt.figure(figsize=(10, 8))
    plt.title("Caixeiro Viajante - Brasil", fontsize=16)

    # Adicionando cada cidade no gráfico e numerando a ordem
    for i, cidade in enumerate(caminho):
        x, y = cidades[cidade]
        plt.scatter(y, x, s=100, color='red')  # Marca a cidade no gráfico
        plt.text(y, x, f"{i + 1}. {cidade}", fontsize=9, ha='right',
                 color='black')  # Adiciona o nome e número da cidade

    # Desenha as conexões entre as cidades
    for i in range(len(caminho) - 1):
        cidade1 = cidades[caminho[i]]
        cidade2 = cidades[caminho[i + 1]]
        plt.plot([cidade1[1], cidade2[1]], [cidade1[0], cidade2[0]], color='blue', linewidth=2)

    # Conecta a última cidade de volta à cidade inicial (fechando o ciclo)
    cidade1 = cidades[caminho[-1]]
    cidade2 = cidades[caminho[0]]
    plt.plot([cidade1[1], cidade2[1]], [cidade1[0], cidade2[0]], color='blue', linewidth=2, linestyle="dashed")

    # Marcadores especiais para início e fim do percurso
    plt.plot([cidades[caminho[0]][1]], [cidades[caminho[0]][0]], 'go', markersize=10, label='Início')
    plt.plot([cidades[caminho[-1]][1]], [cidades[caminho[-1]][0]], 'mo', markersize=10, label='Fim')

    # Ajuste dos eixos para garantir que todas as cidades apareçam bem posicionadas
    plt.xlabel("Longitude", fontsize=12)
    plt.ylabel("Latitude", fontsize=12)
    plt.xlim(-75, -30)  # Garante que Manaus fique dentro do gráfico
    plt.ylim(-35, 5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Adiciona uma grade para melhor visualização
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Legendas", title_fontsize='13')

    plt.tight_layout()  # Ajusta automaticamente os espaçamentos para melhorar a visibilidade
    plt.show()


# 🏁 Pergunta ao usuário quantas cidades deseja visitar
quantidade = int(input(f"Quantas cidades você deseja visitar? (máximo de {len(cidades)}): "))

if quantidade > len(cidades):
    print(f"Quantidade inválida. O número máximo de cidades é {len(cidades)}.")
else:
    # Seleciona um número aleatório de cidades dentro do limite pedido pelo usuário
    cidades_selecionadas = dict(random.sample(list(cidades.items()), quantidade))

    # Resolve o problema do caixeiro viajante e exibe os resultados
    caminho, distancia_total = caixeiro_viajante_vizinho_mais_proximo(cidades_selecionadas)

    # Exibe os resultados no console
    print("\nMenor caminho encontrado:", " → ".join(caminho))
    print(f"Menor distância total: {distancia_total:.2f} unidades de distância\n")

    # Desenha o gráfico do caminho percorrido
    desenhar_caminho(caminho, cidades_selecionadas)
