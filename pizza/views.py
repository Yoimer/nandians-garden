from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            #filled_form data values belong to labels on forms.py

            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'Thanks for ordering! Your %s %s and %s pizza is on its way!' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'],)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Pizza order has failed. Try again'
        return render(request, 'pizza/order.html', {'created_pizza_pk':created_pizza_pk, 'pizzaform':filled_form, 'note':note, 'multiple_form':multiple_form, })
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'multiple_form':multiple_form, 'pizzaform':form})

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        # this line valids if number of pizzas are between 2 and 6
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == "POST":
        # section of code that saves field values in db
        post_form_values = {}
        post_form_values = request.POST
        number_of_forms = int(post_form_values['form-TOTAL_FORMS'])

        to_db = {}
        for i in range(0, number_of_forms):
            to_db['size'] = post_form_values['form-' + str(i) + '-' + 'size']
            to_db['topping1'] = post_form_values['form-' + str(i) + '-' + 'topping1']
            to_db['topping2'] = post_form_values['form-' + str(i) + '-' + 'topping2']
            filled_form = PizzaForm(to_db)
            if filled_form.is_valid():
                filled_form.save()
                created_pizza = filled_form.save()
                created_pizza_pk = created_pizza.id

        filled_formset = PizzaFormSet(request.POST)
        if(filled_formset.is_valid()):
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered!'
        else:
            note = 'Order was not created, please try again'
        return render(request, 'pizza/pizzas.html', {'created_pizza_pk':created_pizza_pk, 'note':note, 'formset':formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset':formset})

def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST,instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated.'
            return render(request, 'pizza/edit_order.html', {'pizzaform':form, 'note':note, 'pizza':pizza})
    return render(request, 'pizza/edit_order.html', {'pizzaform':form,'pizza':pizza})