from django.shortcuts import render, redirect
from .models import Chat

# Create your views here.
def index(request):
    chats = Chat.objects.all()
    context = {
        'chats': chats
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    user = request.POST.get('user')
    content = request.POST.get('content')
    chat = Chat(user=user, content=content)
    chat.save()
    return redirect("chatting:index")


def detail(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = {
        'chat': chat
    }
    return render(request, 'detail.html', context)


def edit(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = {
        'chat': chat
    }
    return render(request, 'edit.html', context)


def update(request, pk):
    chat = Chat.objects.get(pk=pk)
    chat.user = request.POST.get('user')
    chat.content = request.POST.get('content')
    chat.save()

    return redirect('chatting:detail', chat.pk)


def delete(request, pk):
    chat = Chat.objects.get(pk=pk)
    chat.delete()
    return redirect('chatting:index')

