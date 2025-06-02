from django import forms # type: ignore
from .models import Student, Attendance, Mark, Behavior

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms # type: ignore
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    student_name = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Student'
    )

    class Meta:
        model = Attendance
        fields = ['student_name', 'date', 'present']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'present': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        # Populate the student dropdown with all students
        from .models import Student
        students = Student.objects.all()
        self.fields['student_name'].choices = [(student.name, student.name) for student in students]

class MarkForm(forms.ModelForm):
    student_name = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Student'
    )

    class Meta:
        model = Mark
        fields = ['student_name', 'subject', 'mark']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'mark': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MarkForm, self).__init__(*args, **kwargs)
        from .models import Student
        students = Student.objects.all()
        self.fields['student_name'].choices = [(student.name, student.name) for student in students]

class BehaviorForm(forms.ModelForm):
    student_name = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Student'
    )

    class Meta:
        model = Behavior
        fields = ['student_name', 'date', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(BehaviorForm, self).__init__(*args, **kwargs)
        from .models import Student
        students = Student.objects.all()
        self.fields['student_name'].choices = [(student.name, student.name) for student in students]


