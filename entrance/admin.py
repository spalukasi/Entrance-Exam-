from django.contrib import admin
from .models import Student, RightAns, Score, Helpsite,Physics_Question
from .models import Math_Question,Chemistry_Question,English_Question,Aptitude_Question

# Register your models here.

admin.site.register(Student)
admin.site.register(RightAns)
admin.site.register(Score)
admin.site.register(Helpsite)
admin.site.register(Physics_Question)
admin.site.register(Math_Question)
admin.site.register(Chemistry_Question)
admin.site.register(English_Question)
admin.site.register(Aptitude_Question)
