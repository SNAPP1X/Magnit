from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', '12', 'go'],
        'obj':{
            'car': 'Audi',
            'age': 12,
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')