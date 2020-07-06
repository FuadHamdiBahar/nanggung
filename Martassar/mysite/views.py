from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User


def Home(request):
    user = User.objects.get(username=request.user)
    print(user.email)
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'
