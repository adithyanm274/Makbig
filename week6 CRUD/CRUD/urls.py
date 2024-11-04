from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
        #  User page
         path('',views.user_login,name='user_login'),
         path('register',views.register,name='register'),
         path('home',views.home,name='home'),
         path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
        #  Admin Page
         path('admin-home/', views.admin_home, name='admin_home'),
         path('add/',views.add,name="add"),
         path('addrecords/',views.addrecords,name="addrecords"),
         path('delete_record/<int:record_id>/',views.delete_record,name="delete_record"),
         path('update/<int:student_id>/',views.update,name="update"),
         path('students/update/<int:student_id>/submit/',views.update_student, name='update_student'),
         path('logout/', views.admin_logout, name='admin_logout'),






 

]
