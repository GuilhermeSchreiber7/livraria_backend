from django.db import models

from asttokens.util import NodeMethods


class Autor(models.Model):
    nome = models.CharField(max_length=100, default="Unknown", blank=False, null=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)       
    def __str__(self):
        return f"({self.id}){self.nome}"

