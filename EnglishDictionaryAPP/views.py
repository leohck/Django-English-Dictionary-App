from django.shortcuts import render
from .forms import MeaniningForm
from .main import translate


# Create your views here.
def home(request):
    meaningform = MeaniningForm(request.POST or None)
    context = {'meaningform': meaningform}
    if meaningform.is_valid():
        print(meaningform.cleaned_data)
        response = meaningform.cleaned_data['word']
        context['response'] = translate(response)
        return render(request, 'index.html', context=context)
    return render(request, 'index.html', context=context)
