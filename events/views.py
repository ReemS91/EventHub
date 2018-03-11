from django.shortcuts import render
from .models import Events
# Create your views here.
def events_list(request):
	events= models.Events.all()
	context={
		'events':events
	}

	return render(request,'list.html', context)

def events_detail(request, event_id):
	event= models.Evwnts.get(id= event_id)
	context={
		'event':event
	}

	return render(request,'detail.html', context)