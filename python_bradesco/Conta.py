class Conta:
    """
    Representa uma conta bancária.
    """
    def __init__(
        self,
        titular: str,
        numero: int,
        saldo: float,
        limite: float
    ):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self) -> float:
        """Retorna o saldo da conta."""
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float) -> None:
        """Define o saldo da conta, não permitindo valores negativos."""
        if saldo < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = saldo

    @property
    def limite(self) -> float:
        """Retorna o limite da conta."""
        return self._limite

    @limite.setter
    def limite(self, limite: float) -> None:
        """Define o limite da conta, não permitindo valores negativos."""
        if limite < 0:
            raise ValueError("Limite não pode ser negativo")
        self._limite = limite

    def saque(self, valor: float) -> tuple[bool, str]:
        """
        Realiza um saque na conta.

        Args:
            valor (float): O valor a ser sacado.

        Returns:
            tuple: (sucesso: bool, mensagem: str)
        """
        try:
            if valor <= 0:
                raise ValueError("Valor de saque deve ser positivo")
            if valor > self._saldo + self._limite:
                raise ValueError("Saldo insuficiente para realizar o saque")
            self._saldo -= valor
            return True, f"Saque de R${valor:.2f} realizado com sucesso."
        except Exception as e:
            return False, f"Erro ao realizar saque: {str(e)}"

    def deposita(self, valor: float) -> tuple[bool, str]:
        """
        Realiza um depósito na conta.

        Args:
            valor (float): O valor a ser depositado.

        Returns:
            tuple: (sucesso: bool, mensagem: str)
        """
        try:
            if valor <= 0:
                raise ValueError("Valor de depósito deve ser positivo")
            self._saldo += valor
            return True, f"Depósito de R${valor:.2f} realizado com sucesso."
        except Exception as e:
            return False, f"Erro ao realizar depósito: {str(e)}"

    def extrato(self) -> str:
        """
        Retorna um extrato simples da conta, com as principais informações.

        Returns:
            str: Extrato formatado da conta.
        """
        return (
            f"Extrato da Conta\n"
            f"Titular: {self._titular}\n"
            f"Número: {self._numero}\n"
            f"Saldo: R${self._saldo:.2f}\n"
            f"Limite: R${self._limite:.2f}"
        )


