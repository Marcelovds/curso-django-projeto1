from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError
from recipes.models import Recipe
from utils.django_forms import add_attr
from utils.strings import is_positive_number


class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

        add_attr(self.fields.get('observations'), 'class', 'span-2')

    class Meta:
        model = Recipe
        fields = 'title', 'description', 'contract', \
            'local_address', 'model_type', 'is_active', \
            'observations', 'foto'
        widgets = {
            'foto': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'is_active': forms.Select(
                choices=(
                    ('Ativo', 'Ativo'),
                    ('Desativado', 'Desativado'),
                    ('Em Reparo', 'Em Reparo'),
                    ('Outro', 'Outro'),
                ),
            ),
            'model_type': forms.Select(
                choices=(
                    ('Datalogger', 'Datalogger'),
                    ('VRP', 'VRP'),
                ),
            ),
        }

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cd = self.cleaned_data

        title = cd.get('title')
        description = cd.get('description')

        if title == description:
            self._my_errors['title'].append('Não pode ser igual a descrição')
            self._my_errors['description'].append('Não pode ser igual ao nome')

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            self._my_errors['title'].append('Dever ter ao menos 5 caracteres.')

        return title

    def clean_preparation_time(self):
        field_name = 'preparation_time'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('Deve ser um número positivo')

        return field_value

    def clean_servings(self):
        field_name = 'servings'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('Deve ser um número positivo')

        return field_value
