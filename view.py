# Ihave createrd this file Ashish
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    perms= {'name':'Jallawe','place':'Moon'}
    return render(request,'index.html',perms)
    HttpResponse('<h1>Ashish Hello</h1>')
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    newlineremover = request.POST.get('newlineremover', 'off')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analiyze.html', params)
    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to upper', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analiyze.html', params)
    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed=analyzed+char
        params = {'purpose': 'Change to upper', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analiyze.html', params)
    if (spaceremove== 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'space removel', 'analyzed_text': analyzed}
        djtext=analyzed
    if (removepunc!='on' and fullcaps!='on' and newlineremover!='on' and spaceremove!='on'):
        return HttpResponse('Error')
    return render(request, 'analiyze.html', params)
