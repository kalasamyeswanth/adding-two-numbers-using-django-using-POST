from django.shortcuts import render

# Create your views here.
def rana(request):
    return render(request,'hero.html')

def add(request):
    n1=int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    n3 = n1 + n2
    return render(request,'hero2.html',{'result':n3})


