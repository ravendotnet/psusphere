from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization
from studentorg.models import OrgMember
from studentorg.models import Student
from studentorg.forms import OrgMemberForm
from studentorg.forms import OrganizationForm 
from django.urls import reverse_lazy 


class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = "org_list.html"
    paginate_by = 5

class StudentList(ListView):
     model = Student
     context_object_name = 'student'
     template_name = 'student_list.html'
     paginate_by = 5

class OrganizationCreateView(CreateView): 
     model = Organization 
     form_class = OrganizationForm  
     template_name = 'org_form.html' 
     success_url = reverse_lazy('organization-list') 

class OrganizationUpdateView(UpdateView): 
     model = Organization 
     form_class = OrganizationForm  
     template_name = 'org_form.html' 
     success_url = reverse_lazy('organization-list') 

class OrganizationDeleteView(DeleteView): 
     model = Organization  
     template_name = 'org_del.html' 
     success_url = reverse_lazy('organization-list') 

# OrgMember
class OrgMemberList(ListView):
     model = OrgMember
     context_object_name = 'orgmember'
     template_name = 'orgmember_list.html'
     paginate_by = 5

class OrgMemberCreateView(CreateView):
     model = OrgMember
     form_class = OrgMemberForm
     template_name = 'orgmember_form.html'
     success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView): 
     model = OrgMember 
     form_class = OrgMemberForm  
     template_name = 'orgmember_form.html' 
     success_url = reverse_lazy('orgmember-list') 

class OrgMemberDeleteView(DeleteView): 
     model = OrgMember  
     template_name = 'orgmember_del.html' 
     success_url = reverse_lazy('orgmember-list') 

    

# Create your views here.
