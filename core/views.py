from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import  CadastroModelForm
from .models import Palavras
from django.contrib import messages
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['palavras'] = Palavras.objects.all()
        return context
    
class CadastroView(FormView):
    template_name = 'cadastro.html'
    form_class = CadastroModelForm
    success_url = reverse_lazy('cadastro') 
    
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(self.request, *args, **kwargs)
        else:
            return render(self.request,('index.html'))
        
    def form_valid(self, form):
        cadastro = form.save(commit=False)
        cadastro.user = self.request.user
        form.save()
        messages.success(self.request,'Cadastro realizado!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,'Erro no cadastro')
        return super().form_invalid(form)
        
        
