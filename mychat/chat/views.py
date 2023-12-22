from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


def chat_room(request):
    messages = Message.objects.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat_room')

    return render(request, 'chat/chat_room.html', {'messages': messages, 'form': form})

