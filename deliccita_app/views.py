from django.http import HttpResponse
from django.template import loader

def deliccita_app (request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

# Create your views here.