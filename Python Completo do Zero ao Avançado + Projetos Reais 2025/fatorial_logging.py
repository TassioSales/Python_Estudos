from logger_config import log_function, get_logger, LogLevel, log_metrics

# Configuração do logger
logger = get_logger("fatorial")

# Decorador para rastrear métricas de desempenho
def track_performance(func):
    """Decorador para rastrear métricas de desempenho da função fatorial."""
    @log_function(
        logger_instance=logger,
        level=LogLevel.INFO,
        log_args=True,
        log_result=True,
        track_performance=True
    )
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@track_performance
def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão
    
    Args:
        n (int): Número para calcular o fatorial
        
    Returns:
        int: O fatorial do número
        
    Raises:
        ValueError: Se o número for negativo
    """
    if n < 0:
        raise ValueError("Não é possível calcular fatorial de número negativo")
    
    if n == 0 or n == 1:
        return 1
    
    return n * fatorial(n - 1)

@track_performance
def testar_fatorial():
    """
    Função que testa a função fatorial com diferentes casos
    """
    # Teste com número 0
    assert fatorial(0) == 1, "Fatorial de 0 deve ser 1"
    
    # Teste com número 1
    assert fatorial(1) == 1, "Fatorial de 1 deve ser 1"
    
    # Teste com número 5
    assert fatorial(5) == 120, "Fatorial de 5 deve ser 120"
    
    # Teste com número 10
    assert fatorial(10) == 3628800, "Fatorial de 10 deve ser 3628800"
    
    # Teste com número negativo
    try:
        fatorial(-1)
        assert False, "Deve ter lançado ValueError para número negativo"
    except ValueError:
        pass
    
    print("\n=== Resultados dos Testes ===")
    print(f"Fatorial de 0: {fatorial(0)}")
    print(f"Fatorial de 1: {fatorial(1)}")
    print(f"Fatorial de 5: {fatorial(5)}")
    print(f"Fatorial de 10: {fatorial(10)}")
    logger.success("Todos os testes da função fatorial PASSARAM!")

@track_performance
def testar_performance():
    """
    Função que testa a performance do fatorial com números grandes
    """
    print("\n=== Teste de Performance ===")
    print(f"Fatorial de 20: {fatorial(20)}")
    print(f"Fatorial de 30: {fatorial(30)}")
    logger.success("Teste de performance concluído!")

@track_performance
def testar_recursao():
    """
    Função que testa a recursão da função fatorial
    """
    # Teste com recursão profunda
    resultado = fatorial(15)
    
    # Teste com recursão mais profunda
    resultado = fatorial(25)

@track_performance
def main():
    """
    Função principal que executa os testes e solicita entrada do usuário
    """
    try:
        # Executar os testes
        testar_fatorial()
        testar_performance()
        testar_recursao()
        
        while True:
            print("\n=== Calculadora de Fatorial ===")
            print("1. Calcular fatorial")
            print("2. Sair")
            escolha = input("\nEscolha uma opção (1-2): ")
            
            if escolha == "2":
                print("\nObrigado por usar a calculadora de fatorial!")
                break
            
            try:
                numero = int(input("\nDigite um número para calcular o fatorial: "))
                resultado = fatorial(numero)
                print(f"O fatorial de {numero} é {resultado}")
                
            except ValueError as ve:
                logger.error(f"Erro de valor: {str(ve)}")
                logger.warning("Por favor, tente novamente com um número não negativo")
                print(f"Erro: {str(ve)}")
                continue
            except Exception as e:
                logger.error(f"Erro inesperado: {str(e)}")
                logger.warning("Ocorreu um erro inesperado. Por favor, tente novamente")
                print(f"Ocorreu um erro: {str(e)}")
                continue
        
        # Mostrar métricas de desempenho
        logger.info("\nMétricas de desempenho:")
        log_metrics(logger)
        
    except Exception as e:
        logger.error(f"Erro inesperado na execução principal: {str(e)}")
        logger.warning("O programa será encerrado")
        print(f"Ocorreu um erro crítico: {str(e)}")

if __name__ == "__main__":
    main()
