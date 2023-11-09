from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Consulta, Paciente

class ConsultaForm(forms.ModelForm):

    dia = forms.DateField(
        label='Data',
        widget= forms.DateInput(
            format="%Y-%m-%d",
            attrs={'type':'date',}
        ),
        input_formats=('%Y-%m-%d',)
    )
    
    hora = forms.TimeField(
        label='Horário',
        widget= forms.TimeInput(
            format="%H:%M",
            attrs={'type':'time',}
        ),
        input_formats=("%H:%M",)
    )

    class Meta:
        model = Consulta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        for field_nome, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Paciente.objects.filter(email=email).exists():
            raise forms.ValidationError("Este endereço de e-mail já está em uso.")
        return email

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        for field_nome, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PacienteAttForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'telefone', 'email']

    def __init__(self, *args, **kwargs):
        super(PacienteAttForm, self).__init__(*args, **kwargs)
        for field_nome, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
  

class CriarUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Username {username} já está em uso")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este endereço de e-mail já está em uso.")
        return email


    def __init__(self, *args, **kwargs):
        super(CriarUsuario, self).__init__(*args, **kwargs)


        placeholders = {
            'username': 'Nome de usuário',
            'first_name': 'Primeiro nome',
            'last_name': 'Sobrenome',
            'email': 'Endereço de e-mail',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }

        for field_nome, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = placeholders.get(field_nome, '')