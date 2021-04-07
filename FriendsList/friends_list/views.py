from django.shortcuts import render, redirect
from .models import MyDB
from .forms import MyDBForm


def index(request):
    return render(request, 'friends_list/index.html')


def add_to_list(request):
    error = ''
    if request.method == 'POST':
        form = MyDBForm(request.POST)
        print(form)
        if form.is_valid():
            print('ooooook')
            form.save()
            return redirect('index')
        else:
            error = 'Форма заповнена не кректно'
            print('no ok')
    form = MyDBForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'friends_list/addition.html', context)


def show_all_list(request):
    all_data = MyDB.objects.all()
    return render(request, 'friends_list/show.html', {'res': all_data})


def contact(request):
    return render(request, 'friends_list/contact.html')