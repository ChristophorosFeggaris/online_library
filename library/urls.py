from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_student, name='login'),
    path('logout/', views.logout_student, name='logout'),
    path('signup/', views.register_student, name='signup'),
    path('addBook/', views.add_book, name='AddBook'),
    path('listBooks/', views.show_books, name='ListBook'),
    path('bookdetails/<str:pk>/', views.book_details, name='detailBook'),
    path('search_book/', views.search_book, name='searchedBook'),
    path('update_book/<str:pk>', views.update_book, name='updateBook'),
    path('delete_book/<str:pk>/', views.delete_book, name='delete_book'),
]
