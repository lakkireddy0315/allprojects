from django.shortcuts import render,get_object_or_404,redirect
#from testApp.models import Student
from reportlab.pdfgen import canvas
from django.http import HttpResponse, JsonResponse
from testApp import forms
#from testApp.forms import StudentForm
from testApp.forms import FeedbackForm,SignupForm
from testApp.models import Movie
from testApp.forms import MovieForm
from testApp.forms import ItemAddForm,SignUpForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View,ListView
from testApp.models import Book,Beer
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testApp.models import Employee1,ProxyEmployee,ProxyEmployee2
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from testApp.forms import EmailSendForm
from django.core.mail import send_mail
from testApp.forms import EmployeeForm
from testApp.models import Employee,Post

# Create your views here.

def show_view(request):
	employees=Employee.objects.all()
	return render(request,'testapp/index.html',{'employees':employees})

def insert_view(request):
	form=EmployeeForm()
	if request.method=='POST':
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	return render(request,'testapp/insert.html',{'form':form})

def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(employee)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request,'testapp/update.html',{'employee':employee})

def employee_data_view(request):
    employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
    resp='<h1>Employee No:{}<br>Employee Name:{}<br>Employee Salary:{}<br> Employee Address:{}</h1>'.format(employee_data['eno'],employee_data['ename'],employee_data['esal'],employee_data['eaddr'])
    return HttpResponse(resp)

def employee_data_jsonview(request):
    employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
    #json_data=json.dumps(employee_data)
    return JsonResponse(employee_data)


def moviesInfo(request):
    my_dict={'head_msg':'Movies Information',
    'sub_msg1':'Sonali slowly getting cured',
    'sub_msg2':'Bahubali-3 is just planning',
    'sub_msg3':'Salman Khan ready to marriage',
    'photo':'images/sunny.jpg'}
    return render(request,'testApp/news.html',context=my_dict)

def sportsInfo(request):
    my_dict={'head_msg':'Sports Information',
    'sub_msg1':'Anushka Sharma Firing Like anything',
    'sub_msg2':'Kohli updating in game anything can happend',
    'sub_msg3':'Worst Performance by India-Sehwag',
    }
    return render(request,'news.html',context=my_dict)

def politicsInfo(request):
    my_dict={'head_msg':'Politics Information',
    'sub_msg1':'Achhce Din Aaa gaya',
    'sub_msg2':'Rupee Value now 1$:70Rs',
    'sub_msg3':'In India Single Paisa Black money No more',
    }
    return render(request,'news.html',context=my_dict)

def index(request):
    return render(request,'testApp/index.html')

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{}({}) recommends you to read "{}"'.format(cd['name'],cd['email'],post.title)
            message='Read Post At: \n {}\n\n{}\' Comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'durga@blog.com',[cd['to']])
            sent=True
        else:
            form=EmailSendForm()
    return render(request,'testApp/blog/sharebymail.html',{'post':post,'form':form,'sent':sent})

def post_list_view(request):
    post_list=Post.objects.all()
    return render(request,'testApp/post_list.html',{'post_list':post_list})

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)

    return render(request,'testApp/post_detail.html',{'post':post})

"""def post_list_view1(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'testApp/post_list.html',{'post_list':post_list})"""

def home_page_view1(request):
    print(10/0)
    return HttpResponse('<h1>Hello This is from home page view</h1>')

def welcome_view(request):
    print('This line added by view function')
    return HttpResponse('<h1>Custom Middleware Demo</h1>')

def display_view(request):
# employees=Employee.objects.all()
# employees=ProxyEmployee.objects.all()
    #employees=ProxyEmployee.objects.all()
    employees=Employee.objects.get_queryset1()
    my_dict={'employees':employees}
    return render(request,'testapp/index.html',my_dict)

class BeerListView(ListView):
    model=Beer

class BeerDetailView(DetailView):
    model=Beer

class BeerCreateView(CreateView):
    model=Beer
 #fields=('name','taste','color','price')
    fields='__all__'
class BeerUpdateView(UpdateView):
    model=Beer
    fields=('taste','color','price')
class BeerDeleteView(DeleteView):
    model=Beer
    success_url=reverse_lazy('home')

class BookListView(ListView):
    model=Book

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
        #return HttpResponseRedirect('/movies/')
    return render(request,'testApp/signup.html',{'form':form})

def studentview(request):
    student_list=Student.objects.order_by('marks')
    my_dict={'student_list':student_list}
    return render(request,'testApp/students.html',context=my_dict)

'''def student_view(request):
    form=forms.StudentForm
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'testapp/students.html',{'form':form})'''

def index_view(request):
    return render(request,'testapp/index.html')

def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'testApp/addmovie.html',{'form':form})

def list_movie_view(request):
     movies_list=Movie.objects.all().order_by('-rating')
     return render(request,'testApp/listmovie.html',{'movies_list':movies_list})

def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100,700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response

def studentinputview1(request):
    form=forms.StudentForm()
    my_dict={'form':form}
    return render(request,'testapp/input1.html',context=my_dict)

def studentinputview(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing data')
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])
    return render(request,'testapp/input.html',{'form':form})

def student_input_view(request):
    sent=False
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printing data')
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])
            sent=True
    form=StudentForm()
    return render(request,'testApp/input.html',{'form':form,'sent':sent})

def feedback_form_view(request):
    form=FeedbackForm()
# feedback_submitted=False
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('Basic Validation Completed and Printing Data')
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback']) # feedback_submitted=True
    return render(request,'testapp/feedback.html',{'form':form})

def signup_form_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            print('Basic Validation Completed and Printing Data')
            print('Name:',form.cleaned_data['name'])
            print('Password:',form.cleaned_data['password'])
            print('Email:',form.cleaned_data['email'])
    return render(request,'testapp/signup.html',{'form':form})

"""def index(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>index page</h1>')"""

def check_view(request):
    if request.session.test_cookie_worked():
        print('cookies are working properly')
        request.session.delete_test_cookie()
        return HttpResponse('<h1>checking page</h1>')

# Create your views here.
def count_view(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'testApp/count.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response

def name_view(request):
    return render(request,'testApp/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request,'testApp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response

def gf_view(request):
     age=request.GET['age']
     name=request.COOKIES['name']
     response=render(request,'testApp/gf.html',{'name':name})
     response.set_cookie('age',age)
     return response

def results_view(request):
     name=request.COOKIES['name']
     age=request.COOKIES['age']
     gfname=request.GET['gfname']
     response=render(request,'testApp/results.html',{'name':name,'age':age,'gfname':gfname})
     response.set_cookie('gfname',gfname)
     return response

'''def index(request):
    return render(request,'testapp/home.html')'''
def additem(request):
    form=ItemAddForm()
    response=render(request,'testapp/additem.html',{'form':form})
    if request.method=='POST':
        form=ItemAddForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            quantity=form.cleaned_data['quantity']
            response.set_cookie(name,quantity,180)
 # return index(request)
    return response
def displayitem_view(request):
     return render(request,'testapp/showitems.html')


def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_exams_view(request):
    return render(request,'testApp/javaexams.html')
@login_required
def python_exams_view(request):
     return render(request,'testApp/pythonexams.html')
@login_required
def aptitude_exams_view(request):
     return render(request,'testApp/aptitudeexams.html')

def logout_view(request):
     return render(request,'testApp/logout.html')

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This is from ClassBasedView</h1>')
