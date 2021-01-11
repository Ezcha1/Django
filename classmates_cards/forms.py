from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions
from classmates_cards.models import CardModel


class CardsForm(forms.Form):
    class Meta:
        model = CardModel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'

        self.helper.layout = Layout(
            Fieldset(
                'Введите номер карточки',
                AppendedText('number', '', placeholder="Номер карточки"),
            ),
            Fieldset(
                'Почта, для отправки данных на неё',
                'email',
            ),
            FormActions(
                Submit('submit', 'Отправить'),
            )
        )

    number = forms.IntegerField()
    email = forms.EmailField(min_length=9)
