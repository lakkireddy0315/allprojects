from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
from django.http import JsonResponse
from rest_framework import serializers
from testApp.mixins import SerializeMixin,HttpResponseMixin
from testApp.models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from testApp.utils import is_json
from testApp.forms import StudentForm,SignUpForm
from rest_framework.views import APIView
from rest_framework.response import Response
from testApp.serializers import NameSerializer,EmployeeSerializer,AuthorSerializer,BookSerializer
from rest_framework import viewsets,generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from testApp.permissions import SunnyPermission
from testApp.pagination import MyPagination
# Create your views here.
from testApp.pagination import MyPagination3
import requests
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from rest_framework import mixins

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

class EmployeeListModelMixin(mixins.CreateModelMixin,generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeDetailAPIViewMixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView,generics.CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #lookup_field='id'
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

def index(request):
    return render(request,'testApp/index1.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('-date')
    paginator=Paginator(jobs_list,25)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})

def blorejobs(request):
    return render(request,'testapp/blorejobs.html')

def punejobs(request):
    return render(request,'testapp/punejobs.html')

def chennaijobs(request):
    return render(request,'testapp/chennaijobs.html')

def get_geographic_info(request):
    ip = request.META.get ('REMOTE_ADDR') #request.META.get('HTTP_X_FORWARDED_FOR', "") #or request.META.get ('REMOTE_ADDR')
    print('ip ',ip)
    # url='http://api.ipstack.com/'+str(ip)+'? access_key= 3dc63ae05b2288d3bdb6ceaf97f18505'
    url='http://api.ipstack.com/183.82.219.127?access_key=3dc63ae05b2288d3bdb6ceaf97f18505'
    response=requests.get(url)
    data=response.json()
    return render(request,'testApp/info.html',data)

class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

'''class EmployeeAPIView(generics.ListAPIView):
    queryset =Employee.objects.all()
    serializer_class =EmployeeSerializer
    search_fields=('ename',)
    ordering_fields=('eno','esal')'''


'''class EmployeeAPIView(generics.ListAPIView):
    #queryset =Employee.objects.all()
    serializer_class =EmployeeSerializer
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs'''

class EmployeeAPIView(generics.ListAPIView):
    queryset =Employee.objects.all()
    serializer_class =EmployeeSerializer
    pagination_class =MyPagination3

'''class EmployeeAPIView(generics.ListAPIView):
    queryset =Employee.objects.all()
    serializer_class =EmployeeSerializer
    pagination_class =MyPagination'''

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[SunnyPermission,]

'''class EmployeeCRUDCBV(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()'''
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

#http GET http://127.0.0.1:8000/hello/ "Authorization: Token c40d7ef4245e626d3a6a5af4bcbf161a84e37d32"
#c40d7ef4245e626d3a6a5af4bcbf161a84e37d32
#python manage.py drf_create_token vitor

'''class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]'''

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'

class EmployeeListAPIView(APIView):
    def get(self,request,format=None):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)

'''class EmployeeAPIView(generics.ListAPIView):
# queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs'''

class TestViewSet(viewsets.ViewSet):
    def list(self,request):
        colors=['RED','GREEN','YELLOW','ORANGE']
        return Response({'msg':'Wish YOu Colorful Life in 2019','colors':colors})
    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} Your Life will be settled in 2019'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)
    def retrieve(self,request,pk=None):
        return Response({'msg':'Response from retrieve method'})
    def update(self,request,pk=None):
        return Response({'msg':'Response from update method'})
    def partial_update(self,request,pk=None):
        return Response({'msg':'Response from partial_update method'})
    def destroy(self,request,pk=None):
        return Response({'msg':'Response from destroy method'})

class TestApiView(APIView):
    def get(self,request,format=None):
        colors=['RED','BLUE','GREEN','YELLOW','INDIGO']
        return Response({'msg':'Welcome to Colorful Year','colors':colors})
    def post(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} Wish You Happy New Year !!!'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)
    def put(self,request,pk=None):
        return Response({'msg':'Response from put method'})
    def patch(self,request,pk=None):
        return Response({'msg':'Response from patch method'})
    def delete(self,request,pk=None):
        return Response({'msg':'Response from delete method'})

'''@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        id=data.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Created Succesfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        id=data.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(emp,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Updated Succesfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')'''

@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(SerializeMixin,HttpResponseMixin,View):
    def get_object_by_id(self,id):
        try:
            s=Student.objects.get(id=id)
        except Student.DoesNotExist:
            s=None
        return s

    def get(self,request,*args,**kwargs):
         data=request.body
         valid_json=is_json(data)
         if not valid_json:
             return self.render_to_http_response(json.dumps({'msg':'please send valid json only'}),status=400)
         pdata=json.loads(data)
         id=pdata.get('id',None)
         if id is not None:
             std=self.get_object_by_id(id)
             if std is None:
                 return self.render_to_http_response(json.dumps({'msg':'No Matched Resource Found for the given id'}),status=400)
             print(std)
             print(type(std))
             json_data=self.serialize([std,])
             print('json_data ',json_data)
             print(type(json_data))
             print('testing')
             return self.render_to_http_response(json_data)
         qs=Student.objects.all()
         json_data=self.serialize(qs)
         print('testing1')
         return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
         data=request.body
         valid_json=is_json(data)
         if not valid_json:
             return self.render_to_http_response(json.dumps({'msg':'please send valid json only'}),status=400)
         std_data=json.loads(data)
         form=StudentForm(std_data)
         if form.is_valid():
             form.save(commit=True)
             return self.render_to_http_response(json.dumps({'msg':'Resource Created Successfully'}))
         if form.errors:
             json_data=json.dumps(form.errors)
             return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
         data=request.body
         valid_json=is_json(data)
         if not valid_json:
             return self.render_to_http_response(json.dumps({'msg':'please send valid json only'}),status=400)
         provided_data=json.loads(data)
         id=provided_data.get('id',None)
         if id is None:
             return self.render_to_http_response(json.dumps({'msg':'To perform updation id is mandatory,plz provide id'}),status=400)
         std=self.get_object_by_id(id)
         original_data={
         'name':std.name,
         'rollno':std.rollno,
         'marks':std.marks,
         'gf':std.gf,
         'bf':std.bf
         }
         original_data.update(provided_data)
         form=StudentForm(original_data,instance=std)
         if form.is_valid():
             form.save(commit=True)
             return self.render_to_http_response(json.dumps({'msg':'Resource UpdatedSuccessfully'}))
         if form.errors:
             json_data=json.dumps(form.errors)
             return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data):
         return self.render_to_http_response(json.dumps({'msg':'plz send valid jsondata only'}),status=400)
        data=json.loads(request.body)
        id=data.get('id',None)
        if id is None:
         return self.render_to_http_response(json.dumps({'msg':'To perform delete,id is mandatory,you should provide'}),status=400)
        obj=self.get_object_by_id(id)
        if obj is None:
         json_data=json.dumps({'msg':'No matched record found, Not possible to perform delete operation'})
         return self.render_to_http_response(json_data,status=404)
        status,deleted_item=obj.delete()
        if status==1:
         json_data=json.dumps({'msg':'Resource Deleted successfully'})
         return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'unable to delete ...plz try again'})
        return self.render_to_http_response(json_data,status=500)


'''class EmployeeCRUDCBV(SerializeMixin,View):
	def get(self,request,id,*args,**kwargs):
		try:
			emp=Employee.objects.get(id=id)
		except Employee.DoesNotExist:
			json_data=json.dumps({'msg':'Specified Record Not Found'})
		else:
			json_data=self.serialize([emp,])
		return HttpResponse(json_data,content_type='application/json')'''

class EmployeeListCBV(SerializeMixin,View):
	def get(self,request,id,*args,**kwargs):
		qs=Employee.objects.get(id=id)
		json_data=self.serialize([qs,])
		return HttpResponse(json_data,content_type='application/json')

'''class EmployeeCRUDCBV(View):
    def get(self,request,id,*args,**kwargs):
        emp=Employee.objects.get(id=id)
        data={
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr,
        }
        print('emp ',emp)
        print('data ',data)
        json_data=json.dumps(data)
        return HttpResponse(json_data,content_type='application/json')'''

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
        return JsonResponse(employee_data)

def employee_data_view(request):
    employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
    resp='<h1>Employee No:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(employee_data['eno'],
    employee_data['ename'],employee_data['esal'],employee_data['eaddr'])
    return HttpResponse(resp)

def employee_data_jsonview(request):
    employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
    json_data=json.dumps(employee_data)
    return HttpResponse(json_data,content_type='application/json')

def employee_data_jsondirectview(request):
    employee_data={'eno':100,'ename':'Sunny Leone','esal':1000,'eaddr':'Hyderabad'}
    return JsonResponse(employee_data)
