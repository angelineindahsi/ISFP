from django.urls import path,include
from . import views

urlpatterns = [
    path('review/',views.review_list, name='review_list'),
    path('',views.movie_list, name='movie_list'),
    path('reviews/<int:pk>',views.review_detail, name='review_detail'),
    path('Movie/<int:pk>',views.movie_detail, name='movie_detail'),
    path('Movie/<int:pk>/add_review/',views.add_review, name='add_review'),
    path('accounts/logout/', views.logout_view,name='logout_view'),
    path('accounts/register/', views.SignUp.as_view(), name='signup'),
]


