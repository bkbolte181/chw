from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.forms.models import model_to_dict
from django.utils import formats
from models import *
import datetime
import json

def get_current_month():
	dates = []
	start_date = datetime.datetime.today()
	for n in range(-10, 11):
		item = {
			'date': start_date + datetime.timedelta(n),
		}
		if n == 0:
			item['today'] = True
		
		dates.append(item)
	return dates

def info(request):
	if request.is_ajax():
		year = int(request.POST.get('year'))
		month = int(request.POST.get('month'))
		day = int(request.POST.get('day'))
		obj, created = Day.objects.get_or_create(date=datetime.date(year,month,day))
		events = obj.events.all() # Need to filter for the current user's relevant events only
		response = {
			'date': str(obj.date),
			'events': [{'title': e.title, 'day': str(e.day)} for e in events],
		}
		return HttpResponse(json.dumps(response), content_type='application/json')
	else:
		raise Http404

def index(request):
	context = {}
	context['calendar'] = get_current_month()
	return render(request, 'index.html', context)
