from django.forms import ModelForm
from django import forms
from .models import Organization
from .models import Student
from .models import Orgmember
from .models import College
from .models import Program


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class OrgmemberForm(ModelForm):
    class Meta:
        model = Orgmember
        fields = "__all__"


class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"
