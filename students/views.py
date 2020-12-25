from django.shortcuts import render
from .models import Student, UploadFile
from django.forms import widgets
from .forms import StudentCreatationForm
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def students(request):
    context = {
        "students": Student.objects.all()
    }
    return render(request, 'students/student_list.html', context)


class StudentListView(ListView):
    model = Student
    template_name = "students/students_list.html"
    context_object_name = "students"


class StudentDetailView(DetailView):
    model = Student
    fields = '__all__'

    template_name = "students/students_detail.html"


class StudentCreateView(CreateView):
    model = Student
    fields = ['std_id', 'first_name', 'last_name',
              'father_name', 'email', 'phone', 'gender', 'province', 'national_id', 'current_address', 'hostel', 'budget', 'semester', 'image']

    def get_form(self):
        form = super(StudentCreateView, self).get_form()
        form.fields['current_address'].widget = widgets.Textarea(attrs={
                                                                 'rows': 2})

        return form
    template_name = "students/students_form.html"


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'

    def get_form(self):
        form = super(StudentUpdateView, self).get_form()
        form.fields['current_address'].widget = widgets.Textarea(attrs={
                                                                 'rows': 2})

        return form


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/students_confirm_delete.html"

    success_url = "student-list"


class StudentUploadView(CreateView):
    model = UploadFile
    template_name = "students/students_upload.html"
    fields = ['csv_file']
    success_url = '/'


def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_template.csv"'

    writer = csv.writer(response)
    writer.writerow(['std_id', 'first_name',
                     'last_name', 'father_name', 'gender', 'email', 'phone', 'province', 'current_address', 'national_id'])

    return response
