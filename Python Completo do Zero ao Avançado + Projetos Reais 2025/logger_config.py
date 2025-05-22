import os
import sys
import time
import json
import uuid
import traceback
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path
from typing import Dict, Any, Optional, Callable
from functools import wraps
from loguru import logger
from collections import defaultdict
from threading import Lock

# Caminho para a pasta de logs
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True, parents=True)

# Dicionário para armazenar métricas de desempenho
_metrics = defaultdict(list)
_metrics_lock = Lock()

class LogLevel:
    DEBUG = "DEBUG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class RequestContext:
    _request_id = ""
    _user_id = ""
    _extra = {}
    
    @classmethod
    def set_request_context(cls, request_id: str = None, user_id: str = None, **extra):
        """Define o contexto da requisição atual."""
        cls._request_id = request_id or str(uuid.uuid4())
        cls._user_id = user_id or ""
        cls._extra = extra or {}
        return cls._request_id
        
    @classmethod
    def update_context(cls, **kwargs):
        """Atualiza o contexto da requisição atual."""
        cls._extra.update(kwargs)
        return cls.get_context()
        
    @classmethod
    def get_request_id(cls) -> str:
        """Obtém o ID da requisição atual."""
        return cls._request_id
        
    @classmethod
    def get_context(cls) -> dict:
        """Obtém todo o contexto da requisição."""
        return {
            "request_id": cls._request_id,
            "user_id": cls._user_id,
            **cls._extra
        }

def setup_logger(module_name: str):
    """
    Configura o logger para um módulo específico.
    
    Args:
        module_name (str): Nome do módulo para o qual o logger está sendo configurado
    """
    logger.remove()
    
    # Configurar handler para console
    logger.add(
        sys.stdout,
        format="{time:HH:mm:ss} | {level} | {message}",
        level="SUCCESS",
        colorize=True,
        enqueue=True,
        filter=lambda record: "wrapper" not in record["function"]
    )
    
    # Configurar handler para arquivo
    logger.add(
        LOG_DIR / f"{module_name}.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="DEBUG",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        enqueue=True
    )
    
    return logger

def log_function(logger_instance=None, level=LogLevel.INFO, log_args: bool = True, 
               log_result: bool = True, track_performance: bool = True):
    """Decorador avançado para registrar chamadas de função com métricas."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                log = logger_instance or get_logger(func.__module__)
                if log is None:
                    return func(*args, **kwargs)
                    
                func_name = func.__name__
                log_context = {
                    "function": func_name,
                    "module": func.__module__,
                    "timestamp": datetime.now(ZoneInfo('UTC')).isoformat(),
                }
                
                if log_args:
                    log_context["args"] = str(args)
                    log_context["kwargs"] = str(kwargs)
                
                start_time = time.monotonic() if track_performance else None
                
                log.log(level, f"Iniciando {func_name}", **{"extra": log_context})
                
                result = func(*args, **kwargs)
                
                if track_performance and start_time is not None:
                    duration = time.monotonic() - start_time
                    log_context["duration_seconds"] = f"{duration:.4f}"
                    with _metrics_lock:
                        _metrics[func_name].append(duration)
                
                if log_result:
                    log_context["result"] = str(result)[:200]
                
                log.log(level, f"{func_name} concluído", **{"extra": log_context})
                return result
                
            except Exception as e:
                error_context = {
                    **log_context,
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "traceback": traceback.format_exc()
                }
                
                if track_performance and start_time is not None:
                    error_context["duration_seconds"] = f"{time.monotonic() - start_time:.4f}"
                
                log.error(
                    f"Erro em {func_name}",
                    **{"extra": error_context}
                )
                raise
                
        return wrapper
    return decorator

def get_logger(module_name: str) -> logger:
    """Obtém uma instância do logger para o módulo especificado."""
    return setup_logger(module_name)

def get_metrics() -> Dict[str, list]:
    """Obtém as métricas de desempenho coletadas."""
    with _metrics_lock:
        return {
            func: {
                "count": len(times),
                "avg": sum(times) / len(times) if times else 0,
                "min": min(times) if times else 0,
                "max": max(times) if times else 0,
                "last_10": times[-10:]
            }
            for func, times in _metrics.items()
        }

def clear_metrics() -> None:
    """Limpa as métricas de desempenho."""
    with _metrics_lock:
        _metrics.clear()

def log_metrics(logger_instance: logger = None) -> None:
    """Registra as métricas de desempenho atuais."""
    log = logger_instance or logger
    metrics = get_metrics()
    
    if not metrics:
        log.info("Nenhuma métrica de desempenho disponível")
        return
    
    log.info("Métricas de desempenho:")
    for func, data in metrics.items():
        log.info(
            f"{func}: {data['count']} chamadas | "
            f"Média: {data['avg']:.4f}s | "
            f"Min: {data['min']:.4f}s | "
            f"Max: {data['max']:.4f}s"
        )

def cleanup_old_logs(days: int = 30, logger_instance: logger = None) -> None:
    """Remove arquivos de log mais antigos que o número especificado de dias."""
    log = logger_instance or get_logger("logger")
    cutoff = datetime.now() - timedelta(days=days)
    removed = 0
    errors = 0
    
    log.info(f"Iniciando limpeza de logs antigos (mais de {days} dias)")
    
    for log_file in LOG_DIR.glob("*.log"):
        try:
            file_time = datetime.fromtimestamp(log_file.stat().st_mtime)
            if file_time < cutoff:
                log_file.unlink()
                log.debug(f"Arquivo de log removido: {log_file.name} (modificado em {file_time})")
                removed += 1
        except Exception as e:
            errors += 1
            log.error(
                f"Erro ao remover {log_file.name}",
                error=str(e),
                error_type=type(e).__name__
            )
    
    log.info(
        "Limpeza de logs concluída",
        removed=removed,
        errors=errors,
        kept=len(list(LOG_DIR.glob("*.log"))) - removed
    )
