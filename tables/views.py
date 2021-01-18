from django.shortcuts import render
from .models import BotUsers, BotScheduleUlSTU


def index(request):
    users = BotScheduleUlSTU.objects.all()
    content = {
        'users': users
    }
    return render(request, 'tables/index.html', content)
