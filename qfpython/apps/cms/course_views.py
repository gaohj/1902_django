#encoding:utf-8
from django.shortcuts import render
from .forms import PublicCourseForm
from apps.course.models import Course,CourseCategory,Teacher
from django.views.generic import View
from utils import restful

class PublicCourse(View):
    def get(self,request):
        context = {
            'categories':CourseCategory.objects.all(),
            'teachers':Teacher.objects.all()
        }
        return render(request,'cms/pub_course.html',context=context)
    def post(self,request):
        form = PublicCourseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category_id = form.cleaned_data.get('category_id')
            video_url = form.cleaned_data.get('video_url')
            cover_url = form.cleaned_data.get('cover_url')
            price = form.cleaned_data.get('price')
            duration = form.cleaned_data.get('duration')
            profile = form.cleaned_data.get('profile')
            teacher_id = form.cleaned_data.get('teacher_id')

            category = CourseCategory.objects.get(pk=category_id)
            teacher = Teacher.objects.get(pk=teacher_id)
            Course.objects.create(title=title,category=category,teacher=teacher,video_url=video_url,cover_url=cover_url,price=price,duration=duration,profile=profile)
            return restful.success()
        else:
            return restful.params_error(form.get_errors())

