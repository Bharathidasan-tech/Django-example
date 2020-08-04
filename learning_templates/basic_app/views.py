from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic = {"text":"Hello Python", "number": 500}
    return render(request, 'basic_app/index.html', context_dic)

def other(request):
    return render(request, 'basic_app/other.html')

def urltemplate(request):
    return render(request, 'basic_app/template_url.html')    
