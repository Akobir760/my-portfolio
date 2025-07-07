from django.shortcuts import render

# Create your views here.



def my_portfolio(request):
    return render(request, 'index.html', context={
        "name": "Akobir"
    })




def teacher_view(request):
    return render(request, 'teacher.html')
