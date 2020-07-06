from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from . forms import AccountModelForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def RegisterView(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('account:login')

    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)


class AccountLoginView(LoginView):
    template_name = 'account/login.html'
    success_login = True

    def form_invalid(self, form):
        self.success_login = False
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AccountLoginView, self).get_context_data(**kwargs)
        context.update({
            'success_login': self.success_login
        })
        print(context)
        return context


class AccountLogoutView(LogoutView):
    template_name = 'account/logout.html'
