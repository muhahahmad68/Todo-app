from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.


class Login(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) :
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        try:
            user = form.save()
            if user is not None:
                login(self.request, user)
        except ValueError as e:
            form.add_error(None, e.message)
            raise self.form_invalid(form)
        return super(RegisterPage, self).form_valid(form)

    '''def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)'''

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
