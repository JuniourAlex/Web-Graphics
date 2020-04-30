from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView





def login(request) :
    return render(request, 'Login.html')

def base(request):
    return render(request, 'Base.html')



def users(request):
    id =request.GET.get('id', 1)
    name = request.GET.get('name', 'Alex')
    output = '<h2> Id {0} Name {1} </h2>'.format(id, name)
    return HttpResponse(output)


class RegisterForm(FormView):
    form_class = UserCreationForm

    success_url = 'Base.html'

    template_name = 'Register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterForm, self).form_invalid(form)