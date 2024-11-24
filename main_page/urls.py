from . import views
from django.urls import path


urlpatterns = [
    path('abit_info_about_us/', views.ABitInfoAboutUsViewSet.as_view()),
    path('our_slogan/', views.OurSlogan.as_view()),
    path('our_proud/', views.OurProud.as_view()),
    path('company_authors_info/', views.CompanyAuthorsInfo.as_view()),
]
