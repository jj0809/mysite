from django.db import models

# Create your models here.

# 후보의 정보를 저장할 클래스
class Candidate(models.Model):
	name = models.CharField(max_length=10)
	#길이 제한 10인 문자
	introduction = models.TextField()
	#길이 제한 없이 문자열로 설정할 수 있음
	area = models.CharField(max_length=15)
	party_number = models.IntegerField(default=1)
	#숫자


	def __str__(self):
		return self.name