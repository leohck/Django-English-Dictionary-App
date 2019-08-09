from django.shortcuts import render
from .forms import MeaniningForm
from .main import translate


# Create your views here.
def home(request):
    meaningform = MeaniningForm(request.POST or None)
    context = {'meaningform': meaningform}
    if meaningform.is_valid():
        response = meaningform.cleaned_data['word']
        meaning = translate(response)
        if type(meaning) == list:
            context['response_list'] = meaning
        else:
            context['response'] = meaning
        return render(request, 'index.html', context=context)
    return render(request, 'index.html', context=context)
