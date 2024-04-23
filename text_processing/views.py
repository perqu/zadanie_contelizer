from django.shortcuts import render

from .forms import TextFileForm
from .utils import shuffle_sentence


def process_text(request):
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            text_file = request.FILES['text_file']
            modified_text = shuffle_sentence(text_file.read().decode('utf-8'))
            return render(request, 'text_processing/result.html', {'modified_text': modified_text})
    else:
        form = TextFileForm()
    return render(request, 'text_processing/home.html', {'form': form})