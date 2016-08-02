from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from entrance.models import Student, English_Question, Aptitude_Question
from entrance.forms import LoginForm
#from django.template import loader


def loginform(request):
    return render(request,"entrance/login.html",)


# Create your views here.
def HomePage(request):
	return render(request,"entrance/home_page.html",)

def signupform(request):
    return render(request,"entrance/signup.html",)

def test(request):
	all_question = English_Question.objects.all()
	#random = random.randEnglish_Question.id(1,5)
	context = {'all_question':all_question}
	return render(request, "entrance/test.html",context) 





def login(request):
	username = "not logged in"
	if request.method == "POST":
		#Get the posted form
		MyLoginForm = LoginForm(request.POST)
	if MyLoginForm.is_valid():
		username = MyLoginForm.cleaned_data['username']
	else:
		MyLoginForm = Loginform()
	return render(request, 'loggedin.html', {"username" : username})
















def search(request):
	if 'q' in request.GET:
		msg = "U search for: %r" % request.GET['q']
	else:
		msg = "U submitted an empty form."
	return HttpResponse(msg)


def hello(request):
	return HttpResponse("Hello World")

def Login(request):
    return render(request,"entrance/search_form.html",)

#Connecting database
#shortcut of template
def index(request):
	all_student = Student.objects.all()
	context ={'all_student':all_student}
	return render(request,"entrance/index.html", context)

def student_detail(request,student_id):
	try:
		st = Student.objects.get(pk=student_id)
	except Student.DoesNotExist:  #CASE sensitive
		raise Http404("Student doesn't exist")	
	return render(request, "entrance/detail.html",{'st':st})	


#using templates
def login_form(request):
	all_student = Student.objects.all()
	html =''
	for student in all_student:
		url = '/student/' + str(student.id) +student.firstname+ '/' 
		# student.firstname
		html += '<a href=" '+ url +' ">'+ student.firstname +  "</a><br>" 
	return HttpResponse (html)


def student_detail1(request,student_id):
	return HttpResponse("<h2> Detail of student:" + student_id +  "</h2>" )