from django.core.management.base import BaseCommand
from apps.news.models import News,NewsCategory,Banner,Comments
from apps.course.models import CourseOrder,Course,Teacher,CourseCategory
from django.contrib.auth.models import Group,Permission,ContentType


class Command(BaseCommand):
    def handle(self, *args, **options):
        #找到model对应的content_type_id
        #根据content_type_id  找到对应的权限
        #创建分组
        #把权限添加到分组中
        #编辑组
        edit_content_types = [
            ContentType.objects.get_for_model(News),
            ContentType.objects.get_for_model(NewsCategory),
            ContentType.objects.get_for_model(Banner),
            ContentType.objects.get_for_model(Comments),
            ContentType.objects.get_for_model(Course),
            ContentType.objects.get_for_model(CourseCategory),
            ContentType.objects.get_for_model(Teacher),
        ]
        edit_permissions = Permission.objects.filter(content_type__in=edit_content_types)
        edit_group = Group.objects.create(name='编辑')
        edit_group.permissions.set(edit_permissions)
        edit_group.save()
        self.stdout.write(self.style.SUCCESS('编辑组创建完毕'))


           #财务组
        finance_content_types = [
            ContentType.objects.get_for_model(CourseOrder),
        ]
        finance_permissions = Permission.objects.filter(content_type__in=finance_content_types)
        finance_group = Group.objects.create(name='财务')
        finance_group.permissions.set(finance_permissions)
        finance_group.save()
        self.stdout.write(self.style.SUCCESS('财务组创建完毕'))
           #管理员组  编辑+财务

        admin_permissions = edit_permissions.union(finance_permissions)
        admin_group = Group.objects.create(name='管理员')
        admin_group.permissions.set(admin_permissions)
        admin_group.save()
        self.stdout.write(self.style.SUCCESS('管理员组创建完毕'))