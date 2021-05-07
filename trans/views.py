from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator

translater = Translator()

def translate(text, src, dest):

    if text == '':
        return ''
    
    if dest == 'auto':
            dest = 'en'

    if src == 'auto':
        return translater.translate(text, dest=dest).text

    return translater.translate(text, src=src, dest=dest).text

# Create your views here.

def index(request):
    return render(request, 'index.html')


def trans(request):
    result = ''
    if request.method == 'POST':
        text = request.POST['text']
        src = request.POST['src1']
        dest = request.POST['dest1']

        result = translate(text=text, src=src, dest=dest)

        return HttpResponse(result)
    return HttpResponse(result)
        