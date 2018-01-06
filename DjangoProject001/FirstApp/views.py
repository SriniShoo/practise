from django.shortcuts import render
from .models import sumOfChars
from django.http.response import HttpResponse

def index(request):
    return render(request, 'index.html', locals(), content_type = None, status = None, using = None)

def search(request):
    if request.method == 'POST':
        searchString = request.POST.get("nameField", None)
        try:
            charSum = sumOfChars(searchString)
            html = ('<H1>Sum of the number for the alphabets in "{}": {}</H1>'
                    .format(searchString, charSum))
            return HttpResponse(html)
        except:
            return HttpResponse('Some Error')
    else:
        return render(request, 'form.html')
        

# Create your views here.
