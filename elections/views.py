from django.shortcuts import render
from django.http import HttpResponse

# db 에 있는 모든 행 가져오기
from .models import Candidate

# Create your views here.
def index(request):
	#Candidates의 모든 후보가져오기
	candidates = Candidate.objects.all()
	str = ''
	for candidate in candidates:
		str += "<p>{} 기호 {}번 ({})<br>".format(candidate.name,
			candidate.party_number,
			candidate.area)
		str += candidate.introduction + "</p>"
	return HttpResponse(str)