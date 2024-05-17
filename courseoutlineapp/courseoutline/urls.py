from django.urls import path, include
from rest_framework import routers
from courseoutline import views

r = routers.DefaultRouter()
r.register('categories', views.CategoryViewSet, 'categories')
r.register('courses', views.CourseViewSet, 'courses')
r.register('users', views.UserViewSet, 'users')
r.register('outlines',views.OutlineViewSet, 'outlines')
r.register('students', views.StudentViewSet,'students')
r.register('lessons', views.LessonViewSet,'lessons')
r.register('comments', views.CommentViewSet,'comments')

urlpatterns = [
    path('', include(r.urls)),
]