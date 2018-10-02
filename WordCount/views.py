from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request , 'home.html' , {'sentence' : 'hi am the home page of this web site ^^'})


def count(request):
    text = request.GET['text']
    words = text.split()
    worddictionary = {}
    for word in words :
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1) , reverse = True)

    return render(request, 'count.html' , {'text' : text , 'number': len(words), 'sortedwords': sortedwords})



def about(request):
    return render(request , 'about.html')
