from django import forms
from news.models import Category, User


class CreateCategoryForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200, required=True)


class CreateNewsForm(forms.Form):
    title = forms.CharField(label="Título", max_length=200, required=True)
    content = forms.CharField(
        label="Conteúdo", widget=forms.Textarea, required=True
    )
    author = forms.ModelChoiceField(
        label="Autoria",
        required=True,
        queryset=User.objects.all(),
    )
    created_at = forms.DateField(
        label="Criado em",
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    image = forms.ImageField(
        label="URL da Imagem",
        required=False,
    )
    categories = forms.ModelMultipleChoiceField(
        label="Categorias",
        required=True,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
