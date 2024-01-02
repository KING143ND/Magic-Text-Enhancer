from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def analyze(request):
    djtext = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc', 'off')
    removenum = request.POST.get('removenum', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    remove_duplicates = request.POST.get('remove_duplicates', 'off')
    sorttext = request.POST.get('sorttext', 'off')
    reverse_text = request.POST.get('reverse_text', 'off')
    params = {'purpose': 'Original Text', 'analyzed_text': djtext}

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~`=+'''
        analyzed = "".join(char for char in djtext if char not in punctuations)
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if removenum == "on":
        numbers = '''0123456789'''
        analyzed = "".join(char for char in djtext if char not in numbers)
        params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if lowercase == "on":
        analyzed = djtext.lower()
        params = {'purpose': 'Changed to Lowercase', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if capitalize == "on":
        analyzed = djtext.title()
        params = {'purpose': 'Changed to Capitalize', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = " ".join(djtext.split())
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = "".join(char for char in djtext if char != "\n" and char != "\r")
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if len(djtext)==0:
        messages.error(request, 'Enter Something to Analyze!')
        return redirect('/')
    
    if remove_duplicates == "on":
        words = djtext.split()
        unique_words = list(set(words))
        analyzed = ' '.join(unique_words)
        params = {'purpose': 'Removed Duplicate Words', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if sorttext == "on":
        words = djtext.split()
        words.sort()
        analyzed = " ".join(words)
        params = {'purpose': 'Sorted Text', 'analyzed_text': analyzed}
        djtext = analyzed
     
    if reverse_text == "on":
        analyzed = djtext[::-1]
        params = {'purpose': 'Text Reversed', 'analyzed_text': analyzed}
        djtext = analyzed
    else:
        params = {'purpose': 'Original Text', 'analyzed_text': djtext}
          
    return render(request, 'analyze.html', params)