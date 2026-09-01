from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm

"""from studentorg .models import OrgMember
from studentorg.forms import OrgMemberForm

from studentorg.models import Student
from studentorg.forms import StudentForm

from studentorg.models import College
from studentorg.forms import CollegeForm

from studentorg.models import Program
from studentorg.forms import ProgramForm"""

from django.urls import reverse_lazy
paginate_by = 5

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy('organization-list')
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = "org_list.html"
    paginate_by = 5
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy('organization-list')
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy('organization-list')

#ORG_MEMBERS
class Org_MemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "org_member_form.html"
    success_url = reverse_lazy('org-member-list')
class Org_MemberList(ListView):
    model = OrgMember
    context_object_name = 'org_member'
    template_name = "org_member_list.html"
    paginate_by = 5
class Org_MemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "org_member_form.html"
    success_url = reverse_lazy('org-member-list')
class Org_MemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "org_member_del.html"
    success_url = reverse_lazy('org-member-list')

#STUDENT
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy('student-list')
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = "student_list.html"
    paginate_by = 5
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy('student-list')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_del.html"
    success_url = reverse_lazy('student-list')

#COLLEGE
class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy('college-list')
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = "college_list.html"
    paginate_by = 5
class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy('college-list')
class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy('college-list')

#PROGRAM
class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy('program-list')
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = "program_list.html"
    paginate_by = 5
class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy('program-list')
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "program_del.html"
    success_url = reverse_lazy('program-list')
