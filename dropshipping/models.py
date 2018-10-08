from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

class Pessoa(TimeStampedModel, SoftDeletableModel):
    """Model definition for Pessoa."""

    nome = models.CharField("Nome", max_length=255)
    dataNascimento = models.DateField("Data da Nascimento", auto_now=False, auto_now_add=False)
    telefone = models.CharField("Telefone", max_length=20)
    email = models.EmailField("Email", max_length=255)
    endereco = models.CharField("Endereço", max_length=255)
    numero = models.CharField("Número", max_length=10)
    complemento = models.CharField("Complemento", max_length=255)
    cep = models.CharField("CEP", max_length=20)
    cidade = models.CharField("Cidade", max_length=50)
    estado = models.CharField("Estado", max_length=50)
    Bairro = models.CharField("Bairro", max_length=50)

    class Meta:
        abstract = True



class PessoaFisica(Pessoa):

    rg = models.CharField("RG", max_length=25)
    cpf = models.CharField("CPF", max_length=25)

    class Meta:
        verbose_name = "Pessoa Fisica"
        verbose_name_plural = "Pessoas Fisicas"

    def __str__(self):
        return self.rg


class PessoaJuridica(Pessoa):
    """Model definition for PessoaJuridica."""

    empresa = models.CharField("Empresa", max_length=50)
    cnpj = models.CharField("CNPJ", max_length=50)

    class Meta:
        """Meta definition for PessoaJuridica."""

        verbose_name = 'Pessoa Juridica'
        verbose_name_plural = 'Pessoas Juridicas'

    def __str__(self):
        """Unicode representation of Pessoa Juridica."""
        return self.empresa


class Produtos(TimeStampedModel, SoftDeletableModel):
    """Model definition for Produtos."""

    nome = models.CharField("Nome", max_length=50)
    descricao =  models.TextField("Descrição", max_length=50)
    preco = models.DecimalField("Preço", max_digits=5, decimal_places=2)

    class Meta:
        """Meta definition for Produtos."""

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        """Unicode representation of Produtos."""
        self.nome
