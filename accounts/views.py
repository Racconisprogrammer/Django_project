from .forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.
class SignupView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
