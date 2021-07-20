from django.contrib import admin

from .models import Candidate
#모델에서 candidate 만든걸 쓰겠다는 의미

# Register your models here.

admin.site.register(Candidate)