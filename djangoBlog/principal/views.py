from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from forms import AlumnosForm
from models import Alumnos


def alumnos(request):
	lista = Alumnos.objects.all()
	return render_to_response('alumnos.html',{'lista' : lista}, context_instance=RequestContext(request))