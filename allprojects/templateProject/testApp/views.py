from django.shortcuts import render
import datetime
from .forms import GeeksForm


# creating a home view
def home_view(request):
	context = {}
	form = GeeksForm(request.POST or None)
	context['form'] = form
	return render(request, "testApp/home.html", context)

'''def newform(request):
    form = SampleForm(request.POST or None)
    return render(request, 'sampleform.html', {'form': form})'''

def wish(request):
    return render(request,'testApp/wish.html')

def wish1(request):
    date=datetime.datetime.now()
    my_dict={'insert_date':date}
    return render(request,'testApp/wish1.html',context=my_dict)

def wish2(request):
    date=datetime.datetime.now()
    msg=None
    h=int(date.strftime('%H'))
    print('h',h)
    if h<12:
        msg='Hello Guest !!!! Very Very Good Morning!!!'
    elif h<16:
        msg='Hello Guest !!!! Very Very Good AfterNoon!!!'
    elif h<21:
        msg='Hello Guest !!!! Very Very Good Evening!!!'
    else:
        msg='Hello Guest !!!! Very Very Good Night!!!'
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'testApp/wish2.html',context=my_dict)
