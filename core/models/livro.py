from .autor import Autor
from .categoria import Categoria
from .editora import Editora
import site
from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    autores = models.ManyToManyField('Autor', related_name='livros')
    editora = models.ForeignKey('Editora', on_delete=models.PROTECT, related_name='livros', null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, related_name='livros', null=True, blank=True)
    ano_publicacao = models.DateField()
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)