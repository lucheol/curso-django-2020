from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from tickets.utils import MongoHandler


class Categoria(models.Model):

    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ('descricao', )

    def __str__(self):
        return self.descricao


class Solicitacao(models.Model):

    STATUS_NEW = 'new'
    STATUS_ONGOING = 'ongoing'
    STATUS_CLOSED = 'closed'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Novo'),
        (STATUS_ONGOING, 'Em andamento'),
        (STATUS_CLOSED, 'Encerrado'),
        (STATUS_CANCELED, 'Cancelado'),
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nome = models.CharField(max_length=120)
    email = models.EmailField(verbose_name='E-mail')
    assunto = models.CharField(max_length=80)
    descricao = models.TextField(verbose_name='Descrição')
    arquivo = models.FileField(upload_to='solicitacoes', null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_NEW)
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='Data da Solicitação')
    ultima_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    class Meta:
        ordering = ('-ultima_atualizacao', )
        verbose_name = 'Solicitação'
        verbose_name_plural ='Solicitações'

    def __str__(self):
        return f'TICKET{self.pk:04d}'

    # def save(self, *args, **kwargs):
    #
    #     if self.pk:
    #         pass
    #
    #     super().save(*args, **kwargs)

    def registrar_atendente(self, user):

        self.status = self.STATUS_ONGOING
        self.atendente = user
        self.save()

        interacao_obj = Interacao.objects.create(
            solicitacao=self,
            tipo=Interacao.TIPO_ASSIGNED,
            descricao=f'Solicitação assinada para o atendente {user.get_full_name()}',
            atendente=user,
        )

        interacao_obj.send_mail_message()

        return True

    def registrar_resposta(self, user, mensagem):

        self.atendente = user
        self.save()

        interacao_obj = Interacao.objects.create(
            solicitacao=self,
            tipo=Interacao.TIPO_TEAM_RESPONSE,
            descricao=f'Nova resposta: {mensagem}',
            atendente=user,
        )

        interacao_obj.send_mail_message()

        return True

    def cancelar(self, user, motivo):

        self.atendente = user
        self.status = self.STATUS_CANCELED
        self.save()

        interacao_obj = Interacao.objects.create(
            solicitacao=self,
            tipo=Interacao.TIPO_STATUS_CHANGE,
            descricao=f'Ticket cancelado. Motivo: {motivo}',
            atendente=user,
        )

        interacao_obj.send_mail_message()

        return True

    def finalizar(self, user, motivo):

        self.atendente = user
        self.status = self.STATUS_CLOSED
        self.save()

        interacao_obj = Interacao.objects.create(
            solicitacao=self,
            tipo=Interacao.TIPO_STATUS_CHANGE,
            descricao=f'Ticket fechado. Motivo: {motivo}',
            atendente=user,
        )

        interacao_obj.send_mail_message()

        return True


class Interacao(models.Model):

    TIPO_ASSIGNED = 0
    TIPO_TEAM_RESPONSE = 1
    TIPO_REQUESTER_RESPONSE = 2
    TIPO_STATUS_CHANGE = 3

    TIPO_CHOICES = (
        (TIPO_ASSIGNED, 'Assinado para o atendente'),
        (TIPO_TEAM_RESPONSE, 'Resposta do time'),
        (TIPO_REQUESTER_RESPONSE, 'Resposta do solicitante'),
        (TIPO_STATUS_CHANGE, 'Mudança de status')
    )

    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, related_name='interacoes')
    tipo = models.PositiveSmallIntegerField(choices=TIPO_CHOICES)
    descricao = models.TextField()
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    data_interacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_interacao',)
        verbose_name = 'Interação'
        verbose_name_plural = 'Interações'

    def __str__(self):

        return f'{self.pk}'

    def send_mail_message(self):

        subject = f'{self.solicitacao} - Nova interação - {self.get_tipo_display()}'

        send_mail(
            subject=subject,
            message=self.descricao,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.solicitacao.email]
        )

        email_data = {
            'subject': subject,
            'recipient': self.solicitacao.email,
            'message': self.descricao,
            'date': timezone.now()
        }

        mg = MongoHandler('tickets')
        mg.insert('emails', email_data)
