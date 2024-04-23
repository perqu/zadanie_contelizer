from django.shortcuts import render
from .forms import PeselForm
from .utils import get_pesel_data

def pesel_validation(request):
    pesel_number = None
    birth_date = None
    gender = None
    if request.method == 'POST':
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel_number, birth_date, gender = get_pesel_data(form.cleaned_data['pesel_number'])
    else:
        form = PeselForm()
    return render(request, 'pesel_validator/home.html', {'form': form, 'pesel_number': pesel_number, 'birth_date': birth_date, 'gender': gender})
