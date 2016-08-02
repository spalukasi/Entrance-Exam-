from django.db  import models
from django import forms

# Create your models here.
class Student(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	username = models.CharField(max_length=20,default='username',unique=True)
	#password = models.forms.CharField(widget=.PasswordInput())
	email = models.EmailField
	college = models.CharField(max_length=30)
	address = models.CharField(max_length=20)
	favorite_subject = models.CharField(max_length=20,default='Maths')
	weak_subject = models.CharField(max_length=20,default='Physics')
	
	def __str__(self):
	 	return self.username + '  ' + self.address + ' ' + self.college
	 	#return self.college + '  ' + self.phone_no


class Helpsite(models.Model):
	weblink = models.URLField()
	pdflink = models.URLField()
	booklink = models.URLField()

class Score(models.Model):
	Student = models.ForeignKey(Student)
	s_physics = models.IntegerField()
	s_math = models.IntegerField()
	s_chemistry = models.IntegerField()
	s_english = models.IntegerField()
	s_aptitude = models.IntegerField()
    
  
class Physics_Question(models.Model):
	question = models.CharField(max_length=500,unique=True)
	option_a = models.CharField(max_length=50,default="")
	option_b = models.CharField(max_length=50,default="")
	option_c = models.CharField(max_length=50,default="")
	option_d = models.CharField(max_length=50,default="")
	correct_option = models.CharField(max_length=50,default="")

	def __str__(self):
		return self.question + ' ' + self.option_a + ' ' + self.option_b + ' ' + self.option_c + ' ' + self.option_d
	
class Math_Question(models.Model):
	question = models.CharField(max_length=500,unique=True)
	option_a = models.CharField(max_length=50,default="")
	option_b = models.CharField(max_length=50,default="")
	option_c = models.CharField(max_length=50,default="")
	option_d = models.CharField(max_length=50,default="")
	correct_option = models.CharField(max_length=50,default="")

	def __str__(self):
		return self.question + ' ' + self.option_a + ' ' + self.option_b + ' ' + self.option_c + ' ' + self.option_d
	

class Chemistry_Question(models.Model):
	question = models.CharField(max_length=500,unique=True)
	option_a = models.CharField(max_length=50,default="")
	option_b = models.CharField(max_length=50,default="")
	option_c = models.CharField(max_length=50,default="")
	option_d = models.CharField(max_length=50,default="")
	correct_option = models.CharField(max_length=50,default="")
	is_correct = models.BooleanField(default=False)
	
	def __str__(self):
		return self.question + ' ' + self.option_a + ' ' + self.option_b + ' ' + self.option_c + ' ' + self.option_d
	
	
class English_Question(models.Model):
	question = models.CharField(max_length=500,unique=True)
	option_a = models.CharField(max_length=50,default="")
	option_b = models.CharField(max_length=50,default="")
	option_c = models.CharField(max_length=50,default="")
	option_d = models.CharField(max_length=50,default="")
	correct_option = models.CharField(max_length=50,default="")
	is_correct = models.BooleanField(default=False)
	
	def __str__(self):
		return self.question + ' ' + self.option_a + ' ' + self.option_b + ' ' + self.option_c + ' ' + self.option_d
	


class Aptitude_Question(models.Model):
	question = models.CharField(max_length=500,unique=True)
	option_a = models.CharField(max_length=50,default="")
	option_b = models.CharField(max_length=50,default="")
	option_c = models.CharField(max_length=50,default="")
	option_d = models.CharField(max_length=50,default="")
	correct_option = models.CharField(max_length=50,default="")
	is_correct = models.BooleanField(default=False)
	 
	def __str__(self):
		return self.question + ' ' + self.option_a + ' ' + self.option_b + ' ' + self.option_c + ' ' +self.option_d
	

	
class RightAns(models.Model):
	question_id =models.IntegerField(default=0)
	correct_option = models.CharField(max_length=50)