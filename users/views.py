from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from .forms import UserRegistrationForm

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    if request.method != 'POST':
        form = UserRegistrationForm()
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.refresh_from_db()
            new_user.profile.relation_to_denis = form.cleaned_data.get('relation_to_denis')
            new_user.profile.ready_to_register = form.cleaned_data.get('ready_to_register')
            new_user.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=form.cleaned_data.get('password1'))
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
