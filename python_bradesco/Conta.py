from typing import Union
from Cliente import Cliente

class Conta:
    """
    Representa uma conta bancária robusta, com operações de saque, depósito, extrato e transferência.
    O titular pode ser um objeto Cliente ou uma string.
    """
    def __init__(
        self,
        titular: Union[Cliente, str],
        numero: int,
        saldo: float,
        limite: float
    ):
        # Permite titular como Cliente ou string
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    @property
    def titular(self) -> Union[Cliente, str]:
        """Retorna o titular da conta."""
        return self._titular

    @titular.setter
    def titular(self, titular: Union[Cliente, str]) -> None:
        if isinstance(titular, Cliente) or (isinstance(titular, str) and titular.strip()):
            self._titular = titular
        else:
            raise ValueError("Titular deve ser um Cliente ou string não vazia.")

    @property
    def numero(self) -> int:
        """Retorna o número da conta."""
        return self._numero

    @numero.setter
    def numero(self, numero: int) -> None:
        if numero <= 0:
            raise ValueError("Número da conta deve ser positivo.")
        self._numero = numero

    @property
    def saldo(self) -> float:
        """Retorna o saldo da conta."""
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float) -> None:
        if saldo < 0:
            raise ValueError("Saldo não pode ser negativo.")
        self._saldo = saldo

    @property
    def limite(self) -> float:
        """Retorna o limite da conta."""
        return self._limite

    @limite.setter
    def limite(self, limite: float) -> None:
        if limite < 0:
            raise ValueError("Limite não pode ser negativo.")
        self._limite = limite

    def saque(self, valor: float) -> tuple[bool, str]:
        """
        Realiza um saque na conta, validando saldo e limite.
        Retorna tupla (sucesso, mensagem).
        """
        try:
            if valor <= 0:
                raise ValueError("Valor de saque deve ser positivo.")
            if valor > self._saldo + self._limite:
                raise ValueError("Saldo insuficiente para realizar o saque.")
            self._saldo -= valor
            return True, f"Saque de R${valor:.2f} realizado com sucesso."
        except Exception as e:
            return False, f"Erro ao realizar saque: {str(e)}"

    def deposita(self, valor: float) -> tuple[bool, str]:
        """
        Realiza um depósito na conta. Retorna tupla (sucesso, mensagem).
        """
        try:
            if valor <= 0:
                raise ValueError("Valor de depósito deve ser positivo.")
            self._saldo += valor
            return True, f"Depósito de R${valor:.2f} realizado com sucesso."
        except Exception as e:
            return False, f"Erro ao realizar depósito: {str(e)}"

    def transferir(self, destino: 'Conta', valor: float) -> tuple[bool, str]:
        """
        Transfere valor para outra conta, validando saldo e tipo do destino.
        Retorna tupla (sucesso, mensagem).
        """
        if not isinstance(destino, Conta):
            return False, "Destino deve ser uma instância de Conta."
        saque_ok, msg_saque = self.saque(valor)
        if not saque_ok:
            return False, f"Transferência falhou: {msg_saque}"
        deposito_ok, msg_deposito = destino.deposita(valor)
        if not deposito_ok:
            # Estorna o valor sacado caso o depósito falhe
            self.deposita(valor)
            return False, f"Transferência falhou ao depositar no destino: {msg_deposito}"
        return True, f"Transferência de R${valor:.2f} realizada com sucesso para conta {destino.numero}."

    def extrato(self) -> str:
        """
        Retorna um extrato simples da conta, com as principais informações.
        """
        titular_str = str(self._titular) if isinstance(self._titular, Cliente) else self._titular
        return (
            f"Extrato da Conta\n"
            f"Titular: {titular_str}\n"
            f"Número: {self._numero}\n"
            f"Saldo: R${self._saldo:.2f}\n"
            f"Limite: R${self._limite:.2f}"
        )

    def __str__(self) -> str:
        """
        Retorna uma representação legível da conta.
        """
        titular_str = str(self._titular) if isinstance(self._titular, Cliente) else self._titular
        return (
            f"Conta(numero={self._numero}, titular='{titular_str}', saldo=R${self._saldo:.2f}, limite=R${self._limite:.2f})"
        )

    def __repr__(self) -> str:
        return self.__str__()
