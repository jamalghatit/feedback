from django.db import models

class Base(models.Model):
    criado = models.DateTimeField('Data de criação', auto_now_add=True)

    # Classe abstrata não é criada no banco de dados.
    # Ela servirá como rascunho para outras classes.
    class Meta:
        abstract = True

class FeedbackModel(Base):
    nome = models.CharField("Nome", max_length=100)
    OM = models.CharField("OM", max_length=100)
    email = models.CharField('email', max_length=100)
    message = models.CharField('message',  max_length=100)

    def __str__(self):
        return self.nome
