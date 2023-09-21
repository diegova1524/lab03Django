from django.shortcuts import render

# Create your views here.
from .models import Opcion,Pregunta

# Create your views here.
def index(request):
    latest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request,'encuesta/index.html',context)
