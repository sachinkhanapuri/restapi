from rest_framework import serializers
from qv1.models import student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=('id', 'first_name','gender','date_of_birth','total_marks')