   from django.shortcuts import render
from django.views import generic
from myapp.models import Company, CompanyForm
from django.http.response import HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

class LandingView(generic.TemplateView):
    template_name = 'landing.html'
    
    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST)
        if form.is_valid():
            instance = Company()
            instance.name = form.cleaned_data.get('name', None)
            instance.save()
            
            return HttpResponseRedirect('/')
        else:
            return HttpResponseNotFound("Validation Faild")
        
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')
        
