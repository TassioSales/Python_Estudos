class Cliente:
    """
    Representa um cliente do sistema bancário.
    """
    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: str,
        sexo: str,
        estado_civil: str,
        profissao: str,
        nacionalidade: str,
        naturalidade: str,
        endereco: str,
        telefone: str,
        email: str
    ):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._sexo = sexo
        self._estado_civil = estado_civil
        self._profissao = profissao
        self._nacionalidade = nacionalidade
        self._naturalidade = naturalidade
        self._endereco = endereco
        self._telefone = telefone
        self._email = email

    @property
    def nome(self) -> str:
        """Retorna o nome do cliente."""
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """Define o nome do cliente."""
        self._nome = nome


