from django.db import models
from cpf_field.models import CPFField


class Paciente(models.Model):
    nome = models.CharField(max_length=200, null=True)
    cpf = CPFField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=200, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
            return self.nome
    
    def cpf_formatado(self):
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[7:9]}-{self.cpf[9:]}"
    
    def telefone_formatado(self):
        return f"({self.telefone[:2]}) {self.telefone[2:7]}-{self.telefone[7:11]}"
    

class Medico(models.Model):
    ESPECIALIDADES = (('Cardiologia', 'Cardiologia'),
                     ('Psiquiatria', 'Psiquiatria'),
                     ('Endocrinologia', 'Endocrinologia'),
                     ('Dermatologia', 'Dermatologia'),
                     )
    
    nome = models.CharField(max_length=200, null=True)
    telefone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    crm = models.CharField(max_length=20, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    especialidade = models.CharField(max_length=200, null=True, choices=ESPECIALIDADES)

    def __str__(self):
        return f'{self.nome} - ({self.especialidade})'
    

class Consulta(models.Model):    
    STATUS = (
                ('Concluída', 'Conluída'),
                ('Aguardando Confirmação', 'Aguardando Confirmação'),
                ('Aguardando Exames', 'Aguardando Exames'),
                ('Confirmada', 'Confirmada'),
                ('Cancelada', 'Cancelada'),
    )

    paciente = models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    medico = models.ForeignKey(Medico, null=True, on_delete=models.SET_NULL)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    dia = models.DateField(null=True)
    hora = models.TimeField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.medico.nome