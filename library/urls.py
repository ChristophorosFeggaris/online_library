from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_student, name='login'),
    path('logout/', views.logout_student, name='logout'),
    path('signup/', views.register_student, name='signup'),
    path('addBook/', views.add_book, name='AddBook'),
    path('listBooks/', views.show_book, name='ListBook'),
    path('search_book/', views.search_book, name='searchedBook')
]
