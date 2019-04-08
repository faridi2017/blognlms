from rest_framework import serializers
from .models import *




class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class BooksIssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('barcode', 'title', 'author')

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class CheckoutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkouts
        fields = '__all__'
#

class CheckoutsBookSerializer(serializers.ModelSerializer):
    # book_details = BooksIssuedSerializer(read_only=True)
    class Meta:
        model = Checkouts
        fields = ('barcode','issued_on','due_date')

class StudentWithBooks(serializers.ModelSerializer):
    book_issued = CheckoutsBookSerializer(read_only=True, many=True)
    class Meta:
        model = Students
        fields = ('student_name','enrollment_no','book_issued')

class CheckoutsTSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    def get_title(self, instance):
        data = Books.objects.filter(barcode=instance.barcode)
        return BooksSerializer(data, many=True).data
    class Meta:
        model = Checkouts
        fields = ('barcode', 'issued_on', 'due_date','student_eno','title')

