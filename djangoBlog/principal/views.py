from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from forms import AlumnosForm
from models import Alumnos

def alumnos(request):
	lista = Alumnos.objects.all()
	return render_to_response('alumnos.html',{'lista' : lista}, context_instance=RequestContext(request))

def addAlumnos(request):
	if request.method == "POST":
		form = AlumnosForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect("/alumnos")
	else:
		form = AlumnosForm()
	ctx = {'form': form}
	return render_to_response("add_Alumnos.html",ctx,context_instance=RequestContext(request))