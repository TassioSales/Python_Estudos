import time
import random

def pesquisa_simples(lista, item):
    """Pesquisa linear que retorna o índice e o número de iterações."""
    for i in range(len(lista)):
        if lista[i] == item:
            return i, i + 1  # Índice encontrado e número de iterações
    return None, len(lista)  # Se não encontrar, percorreu toda a lista

def pesquisa_binaria(lista, item):
    """Pesquisa binária que retorna o índice e o número de iterações."""
    baixo, alto = 0, len(lista) - 1
    iteracoes = 0

    while baixo <= alto:
        iteracoes += 1
        meio = (baixo + alto) // 2
        if lista[meio] == item:
            return meio, iteracoes  # Índice encontrado e número de iterações
        elif lista[meio] > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None, iteracoes  # Se não encontrar, retorna o total de iterações feitas

# Criando uma lista grande com números ímpares
minha_lista = list(range(1, 1000000, 2))

# Escolhendo um item aleatório da lista
item_procurado = random.choice(minha_lista)

# Número de repetições para cálculo do tempo médio
repeticoes = 1000

# Medindo tempo e contando iterações da pesquisa simples
tempos_simples = []
iteracoes_simples = []
indice_encontrado = None

for _ in range(repeticoes):
    inicio = time.time()
    indice, iteracoes = pesquisa_simples(minha_lista, item_procurado)
    tempos_simples.append((time.time() - inicio) * 1000)  # Convertendo para milissegundos
    iteracoes_simples.append(iteracoes)
    if indice is not None:
        indice_encontrado = indice  # Guarda o índice do item encontrado

tempo_simples_medio = sum(tempos_simples) / repeticoes
iteracoes_simples_medio = sum(iteracoes_simples) / repeticoes

# Medindo tempo e contando iterações da pesquisa binária
tempos_binarios = []
iteracoes_binarias = []

for _ in range(repeticoes):
    inicio = time.time()
    _, iteracoes = pesquisa_binaria(minha_lista, item_procurado)
    tempos_binarios.append((time.time() - inicio) * 1000)
    iteracoes_binarias.append(iteracoes)

tempo_binaria_medio = sum(tempos_binarios) / repeticoes
iteracoes_binaria_medio = sum(iteracoes_binarias) / repeticoes

# Função para formatar o tempo e evitar "0.00000 ms"
def formatar_tempo(tempo):
    return "< 0.00001" if tempo < 0.00001 else f"{tempo:.5f}"

# Exibindo os resultados
print(f"🔍 Item aleatório escolhido: {item_procurado}")
print(f"📍 Posição do item na lista: {indice_encontrado}")

print(f"\n📌 Pesquisa Simples:")
print(f"- Tempo médio de execução ({repeticoes} execuções): {formatar_tempo(tempo_simples_medio)} ms")
print(f"- Iterações médias para encontrar o número: {iteracoes_simples_medio:.2f}")

print(f"\n⚡ Pesquisa Binária:")
print(f"- Tempo médio de execução ({repeticoes} execuções): {formatar_tempo(tempo_binaria_medio)} ms")
print(f"- Iterações médias para encontrar o número: {iteracoes_binaria_medio:.2f}")
