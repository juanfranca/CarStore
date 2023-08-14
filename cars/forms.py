from django.forms import ModelForm
from cars.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor mínimo para cadastrar seu carro é R$20.000')
        return value
    
    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 1975:
            self.add_error('year', 'O modelo do carro precisa ser fabricado após a 1975')
        return year
