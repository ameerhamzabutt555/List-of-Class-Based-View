from django.urls import path
from app import views


urlpatterns = [
    path('', views.RedirectView.as_view(pattern_name='students'), name='app'),
    path('students/<int:pk>/', views.Student.as_view(template_name = 'app/students.html'),name='students'),
    path('students/', views.ShowStudents.as_view(template_name='app/showstudents.html'), name='students'),
    path('message/', views.MessagePage.as_view(), name='message'),
    path('form/', views.StudentForm.as_view(), name='form'),
    path('update/<int:pk>/', views.StudentUpdate.as_view(), name='update'),
    path('delet/<int:pk>/', views.DeletPage.as_view(), name='delet'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks')

]

