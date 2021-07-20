from django.shortcuts import render
from django.http import HttpResponse

# db 에 있는 모든 행 가져오기
from .models import Candidate

# Create your views here.
def index(request):
	#Candidates의 모든 후보가져오기
	candidates = Candidate.objects.all()
	context = {'candidates' : candidates}
	return render(request, 'elections/index.html', context)