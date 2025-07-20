import re
from datetime import datetime

class Cliente:
    """
    Representa um cliente do sistema bancário, com validações para os principais campos.
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
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.profissao = profissao
        self.nacionalidade = nacionalidade
        self.naturalidade = naturalidade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    # Propriedade nome
    @property
    def nome(self) -> str:
        """Retorna o nome do cliente."""
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if not nome or not nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        self._nome = nome.strip()

    # Propriedade CPF
    @property
    def cpf(self) -> str:
        """Retorna o CPF do cliente."""
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        if not re.match(r"^\d{11}$", cpf):
            raise ValueError("CPF deve conter 11 dígitos numéricos.")
        self._cpf = cpf

    # Propriedade data_nascimento
    @property
    def data_nascimento(self) -> str:
        """Retorna a data de nascimento do cliente."""
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data: str) -> None:
        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data de nascimento deve estar no formato DD/MM/AAAA.")
        self._data_nascimento = data

    # Propriedade sexo
    @property
    def sexo(self) -> str:
        return self._sexo

    @sexo.setter
    def sexo(self, sexo: str) -> None:
        if sexo.upper() not in ("M", "F", "O"):
            raise ValueError("Sexo deve ser 'M', 'F' ou 'O'.")
        self._sexo = sexo.upper()

    # Propriedade estado_civil
    @property
    def estado_civil(self) -> str:
        return self._estado_civil

    @estado_civil.setter
    def estado_civil(self, estado: str) -> None:
        if not estado or not estado.strip():
            raise ValueError("Estado civil não pode ser vazio.")
        self._estado_civil = estado.strip()

    # Propriedade profissao
    @property
    def profissao(self) -> str:
        return self._profissao

    @profissao.setter
    def profissao(self, profissao: str) -> None:
        self._profissao = profissao.strip()

    # Propriedade nacionalidade
    @property
    def nacionalidade(self) -> str:
        return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str) -> None:
        self._nacionalidade = nacionalidade.strip()

    # Propriedade naturalidade
    @property
    def naturalidade(self) -> str:
        return self._naturalidade

    @naturalidade.setter
    def naturalidade(self, naturalidade: str) -> None:
        self._naturalidade = naturalidade.strip()

    # Propriedade endereco
    @property
    def endereco(self) -> str:
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        self._endereco = endereco.strip()

    # Propriedade telefone
    @property
    def telefone(self) -> str:
        return self._telefone

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        if not re.match(r"^\d{10,11}$", telefone):
            raise ValueError("Telefone deve conter 10 ou 11 dígitos numéricos.")
        self._telefone = telefone

    # Propriedade email
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            raise ValueError("Email inválido.")
        self._email = email

    def __str__(self) -> str:
        """
        Retorna uma representação legível do cliente.
        """
        return (
            f"Cliente: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Nascimento: {self.data_nascimento}\n"
            f"Sexo: {self.sexo}\n"
            f"Estado Civil: {self.estado_civil}\n"
            f"Profissão: {self.profissao}\n"
            f"Nacionalidade: {self.nacionalidade}\n"
            f"Naturalidade: {self.naturalidade}\n"
            f"Endereço: {self.endereco}\n"
            f"Telefone: {self.telefone}\n"
            f"Email: {self.email}"
        )
