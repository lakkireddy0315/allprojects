from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        #return HttpResponse('<h1>Currently Application under maintenance...plz try after 2 days!!!')
        #print('pre')
        response = self.get_response(request)
        #print('post')
        return response
    '''def process_exception(self,request,exception):
        print('except')
        return HttpResponse('<h1>Currently we are facing some technical problemsplz try after some time!!!</h1>')'''
