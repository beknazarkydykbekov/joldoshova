from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import HttpResponseRedirect
from .models import User
from .forms import SendBackForm


class BaseView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'index.html', context)


# def sendus(request):
    # if request.method == 'POST':
    #     form = SendBackForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         return HttpResponseRedirect('/')

def sendus(request):
    user = SendBackForm
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        all_users = User(name=name, email=email, message=message)
        all_users.save()
        if all_users.save() == all_users.save():
            return HttpResponseRedirect('/')
        return render(request, 'index.html', {'user', user})


# def sendus(request):
#     form = SendBackForm
#
#     data = {
#         'form': form
#     }
#
#     return render(request, 'index.html', data)


# def sendus(request):
#     form = SendBackForm(request.POST or None)
#
#     if request.method == 'POST' and form.is_valid():
#         new_form = form.save()
#     return render(request, 'index.html', locals())