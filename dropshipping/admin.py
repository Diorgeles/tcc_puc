from django.contrib import admin
from . import models

@admin.register(models.PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    """Pessoa Fisica admin."""

@admin.register(models.PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    """Pessoa Juridica admin."""

@admin.register(models.Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    """Produto admin."""