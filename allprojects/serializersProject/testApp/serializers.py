from rest_framework import serializers
from testApp.models import Employee,Book,Author
from rest_framework.serializers import ModelSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    #books_by_author=BookSerializer(read_only=True,many=True)
    class Meta:
        model=Author
        fields='__all__'

class NameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=7)
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

'''class NameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=7)'''

'''def multiples_of_1000(value):
    print('validations by using validator')
    if value%1000!=0:
        raise serializers.validationError('salary should be multiples of 1000s')'''

'''class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=64)
    esal=serializers.FloatField()
    eaddr=serializers.CharField(max_length=64)

    def validate_esal(self,value):
        print('validations for field level')
        if value<5000:
            raise serializers.ValidationError('emp should be min 5000')
        return value

    def validate(self,data):
        print('validations at object level')
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower()=='sunny':
            if esal<60000:
                raise serializers.ValidationError('Sunny Salary should be minimum 60K')
        return data

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance'''
