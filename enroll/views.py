from django.shortcuts import render, HttpResponseRedirect, redirect
from enroll.forms import StudentRegistration
from enroll.models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


# Create your views here.
# this function will add new item and show to the front user
# By using TemplateView class
class UserAddAndShow(TemplateView):
    template_name = "enroll/addandshow.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {
            'stu': stud,
            'form': fm
        }
        return context

    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        return redirect('/')


# def add_show(request):
#     stud = User.objects.all()
#     if request.method == "POST":
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm = StudentRegistration()

#     else:
#         fm = StudentRegistration()

#     return render(request, "enroll/addandshow.html", {"form": fm, "stu": stud})


# this function will edit or update data
# By using View class
class UpdateStudent(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        return render(request,"enroll/updatestudent.html", {"form": fm})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request, instance=pi)
        print()
        if fm.is_valid():
            fm.save()
        return render(request, "enroll/updatestudent.html", {"form": fm, "stu": pi})


# def update_data(request, id):
#     if request.method == "POST":
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(instance=pi)
#     return render(request, "enroll/updatestudent.html", {"form": fm, "stu": pi})


# this function will delete data from table
# By using RedirectView class
class DeleteData(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        usr = User.objects.get(pk=kwargs['id'])
        usr.delete()
        return super().get_redirect_url(*args, **kwargs)

# def delete_data(request, id):
#     if request.method == "POST":
#         pi = User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect("/")

#     return HttpResponseRedirect("")
