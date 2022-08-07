import requests

url = 'http://127.0.0.1:8000/hello/'
headers = {'Authorization': 'Token 30bec359d6dc47092b02226ef3487beb07802a61'}
r = requests.get(url, headers=headers)
'''import requests 
import json 
BASE_URL='http://127.0.0.1:8000/' 
ENDPOINT='api/' 
def get_resources(name): 
    data={"name":"Sunny"} 
    print('name ',name)
    if name is not None: 
        data={ 
        'name':name 
        } 
    print(json.dumps(data))
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data)) 
    print(resp.status_code) 
    print(resp.json()) 
get_resources(name) '''
'''import requests 
import json 
BASE_URL='http://127.0.0.1:8000/' 
ENDPOINT='api/' 
def get_resources(id): 
    data={} 
    print('id ',id)
    if id is not None: 
        data={ 
        'id':id 
        } 
    print(json.dumps(data))
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data)) 
    print(resp.status_code) 
    print(resp.json()) 
get_resources(2) '''
'''def create_resource(): 
    new_emp={ 
    'eno':300, 
    'ename':'Kareena', 
    'esal':3000, 
    'eaddr':'Hyderabad', 
    } 
    r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp)) 
    print(r.status_code) 
    # print(r.text) 
    print(r.json()) 
#create_resource() 
def update_resource(id): 
    new_data={ 
    'id':id, 
    'eno':700, 
    'ename':'Sunny123', 
    'esal':15000, 
    'eaddr':'Hyd' 

    } 
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data)) 
    print(r.status_code) 
    print(r.text) 
    print(r.json()) 
#update_resource(3) 
def delete_resource(id): 
    data={ 
    'id':id, 
    } 
    r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data)) 
    print(r.status_code) 
    # print(r.text) 
    print(r.json()) 
#delete_resource(5)

import requests 
import json 
BASE_URL='http://127.0.0.1:8000/' 
ENDPOINT='api/' 
def get_resources(id): 
    data={} 
    if id is not None: 
        data={ 
        'id':id 
        } 
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data)) 
    print(resp.status_code) 
    print(resp.json()) 
get_resources(3) 
def create_resource(): 
    new_std={ 
    'name':'Dhoni', 
    'rollno':105, 
    'marks':36, 
    'gf':'Deepika', 
    'bf':'Yuvraj' 
    } 
    r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_std)) 
    print(r.status_code) 
    # print(r.text) 
    print(r.json()) 
#create_resource() 
def update_resource(id): 
    new_data={ 
    'id':id, 
    'gf':'Sakshi', 

    } 
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data)) 
    print(r.status_code) 
    # print(r.text) 
    print(r.json()) 
#update_resource(1) 
def delete_resource(id): 
    data={ 
    'id':id, 
    } 
    r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data)) 
    print(r.status_code) 
    # print(r.text) 
    print(r.json()) 
#delete_resource(1) 

import requests 
BASE_URL='http://127.0.0.1:8000/' 
ENDPOINT='EmployeeCRUDCBV/' 
n=input('Enter required id:') 
r=requests.get(BASE_URL+ENDPOINT+n+'/') 
print(r.status_code)
data=r.json() 
print(data) 
import requests 
BASE_URL='http://127.0.0.1:8000/' 
ENDPOINT='api/' 
r=requests.get(BASE_URL+ENDPOINT) 
data=r.json() 
print(data)
print('Employee Number:',data['eno']) 
print('Employee Name:',data['ename']) 
print('Employee Salary:',data['esal']) 
print('Employee Address:',data['eaddr']) '''