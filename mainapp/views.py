from django.shortcuts import render
from googletrans import Translator
from .models import Result

translater = Translator()


def translate(text, src, dest):

    if text == '':
        trans = Result()
        trans.src = src
        trans.dest = dest
        return trans

    if dest == '':
        trans = Result()
        trans.origin = text
        trans.src = src
        trans.dest = dest
        return trans

    if src == '':
        return translater.translate(text, dest=dest)
    return translater.translate(text, src=src, dest=dest)


def index(request):
    result = Result()
    src = result.src
    if request.method == "POST":
        text = request.POST['entering_text']
        src = request.POST['src']
        dest = request.POST['dest']

        if not (text == None and src == None and dest == None):
            result = translate(text, src, dest)

    context = {"result": result, 'src': src}
    return render(request, 'index.html', context)