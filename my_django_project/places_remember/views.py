from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator

from .forms import MemoryForm
from .models import Memory, Userpic


def index(request):
    user = request.user
    if request.user.is_authenticated:
        full_name = user.get_full_name()
        username = user.username
        memories = Memory.objects.filter(author=username).order_by('-date')
        userpic = Userpic.objects.filter(username=username).first()
        pic = userpic.pic if userpic else None

        memory_list = Memory.objects.all()
        paginator = Paginator(memory_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            'memory-list.html',
            context={
                'memory_list': memories,
                'name': full_name,
                'pic': pic,
                'page_obj': page_obj
            }
        )
    else:
        return render(request, 'index.html', context={})


def add_memory(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = Memory()
            memory.author = request.user.username
            memory.title = form.cleaned_data['title']
            memory.comment = form.cleaned_data['comment']
            memory.date = form.cleaned_data['date']
            memory.save()
            return HttpResponseRedirect('/')
    else:
        form = MemoryForm()
        return render(request, 'form.html', {'form': form})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
