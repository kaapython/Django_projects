from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.decorators import login_required

from main.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required()
def search(request):
    '''Вывод информации для страницы поиска'''
    data_cert = State_security.objects.filter(certificate='да').count()
    data_count = State_security.objects.count()
    return render(request, 'search.html', {'data_count': data_count, 'data_cert': data_cert})

@login_required()
def info(request):
    '''Вывод информации о нормативных актах'''
    return render(request, 'info.html')


@login_required()
def answer_inn(request):
    '''Вывод информации о всех учреждениях'''
    try:
        info_inn = request.GET['search_inn']
        data = State_security.objects.get(inn__inn=info_inn)
        return render(request, 'answer_inn.html', {'data': data})
    except ObjectDoesNotExist:
        return render(request, 'error.html')
    except ValueError:
        return render(request, 'error.html')
    except MultipleObjectsReturned:
        return render(request, 'doublerror.html')

@login_required()
def answer_sogl(request):
    '''Вывод информации о всех учреждениях'''
    try:
        info_sogl = request.GET['search_sogl']
        data = State_security.objects.get(sogl__sogl=info_sogl)
        return render(request, 'answer_sogl.html', {'data': data})
    except ObjectDoesNotExist:
        return render(request, 'error.html')
    except ValueError:
        return render(request, 'error.html')
    except MultipleObjectsReturned:
        return render(request, 'doublerror.html')


def logout_view(request):
    """Завершает сеанс работы с приложением."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required()
def affiliation(request):
    '''Вывод подведомственных учреждений'''
    return render(request, 'affiliation.html')

@login_required()
def affiliation(request):
    '''Вывод информации о всех подведомственных учреждениях'''
    data_podved = State_security.objects.all()
    return render(request, 'affiliation.html', {'data': data_podved})
