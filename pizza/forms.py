from django import forms
from .models import Pizza

#Let's comment out the actual PizzaForm class and lets's create a new one using models

class PizzaForm(forms.Form):

    ######widget implementations
    # topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.Textarea) # for textarea
    # topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.PasswordInput) # for password
    # toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olives', 'Olives')], widget=forms.CheckboxSelectMultiple) # for checkboxes

    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size',choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])

# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}
