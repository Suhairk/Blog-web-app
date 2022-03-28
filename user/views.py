from django.shortcuts import redirect, render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import  UserCreationForm, UserRegistrationForm, UserUpdateForm,ProfileUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile



def register(request):
    print('printting')
    if request.method == 'POST':
        print('post method')
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print('successs')
            messages.success(request , 'your account has been registered')
            return redirect ('/login')
        print('errorr')
        messages.error(request , 'Please enter valid data')
    
    
    form = UserRegistrationForm()
    context = {'form':form}
    return render(request , 'user_tmp/register.html' ,context )

from django.contrib.auth.forms import AuthenticationForm
""" def usr_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request , data = resquest.POST)
 """
@login_required
def profile(request):
    print('somethinggg')
    if request.method == 'POST':
        print('method post')


        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        print(request.user)
        print(request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/')

    else:
        print('getttt')
        print(request.user)
        print(request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user_tmp/profile.html', context)


def success(request):
    return render(request , 'user_tmp/success.html')