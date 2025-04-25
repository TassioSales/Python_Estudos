# CONVERSOR DE SEGUNDOS PARA HORAS:MINUTOS:SEGUNDOS
# Este programa pede ao usuário um número inteiro de segundos e converte para o formato h:m:s

def converter_segundos():
    # Entrada do usuário
    segundos_totais = int(input('Digite a quantidade de segundos: '))

    # Cálculo das horas, minutos e segundos
    horas = segundos_totais // 3600  # 1 hora = 3600 segundos
    resto = segundos_totais % 3600
    minutos = resto // 60  # 1 minuto = 60 segundos
    segundos = resto % 60

    # Exibe o resultado formatado
    print(f'{segundos_totais} segundos equivalem a: {horas:02d}:{minutos:02d}:{segundos:02d} (horas:minutos:segundos)')

# Execução somente se o arquivo for executado diretamente
if __name__ == '__main__':
    converter_segundos()

# DICA: Você pode digitar diferentes valores para testar!
