from django.shortcuts import render
from django.views.generic import CreateView
from .models import Files
from django.contrib import messages


class filesCreateView(CreateView):
    model = Files
    fields = '__all__'
    template_name = 'home.html'
    success_url = '/'


    def form_valid(self, form):
        messages.success(self.request, 'Poprawnie wgrano plik. Zaczekaj na wynik weryfikacji.')
        return super().form_valid(form)
# Create your views here.
