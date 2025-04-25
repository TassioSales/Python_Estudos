# ENTRADA DE DADOS EM PYTHON - EXEMPLOS EXPLICATIVOS
# Use este arquivo para aprender e revisar como ler dados do usuário!

# 1. Entrada básica com input()
nome = input('Qual o seu nome? ')
print('Você digitou:', nome)

# 2. Todo dado lido com input() é do tipo string!
idade_str = input('Qual sua idade? ')
print('Tipo de idade_str:', type(idade_str))  # sempre será <class 'str'>

# 3. Convertendo a entrada para inteiro (int)
idade = int(input('Digite sua idade (número): '))
print('Idade como inteiro:', idade, '| Tipo:', type(idade))

# 4. Convertendo a entrada para float
altura = float(input('Digite sua altura (ex: 1.75): '))
print('Altura como float:', altura, '| Tipo:', type(altura))

# 5. Convertendo para booleano (True/False)
resposta = input('Você gosta de Python? (s/n): ')
gosta_python = resposta.lower() == 's'  # True se digitar 's', False caso contrário
print('Gosta de Python?', gosta_python, '| Tipo:', type(gosta_python))

# DICAS:
# - Sempre converta o dado lido se precisar de outro tipo (int, float, etc)
# - Se o usuário digitar algo inválido (ex: letra ao invés de número), o programa dará erro
# - Você pode tratar erros com try/except (avançado)

# FIM DOS EXEMPLOS
# Teste rodar este arquivo e digite diferentes valores para ver os resultados!
