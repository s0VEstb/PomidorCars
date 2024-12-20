from django.contrib import admin
from django.urls import path, include, re_path
from cars.views import OauthAPIGithubView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('github-auth/', OauthAPIGithubView.as_view(), name='oauth_github'),
    path('main_page/', include('main_page.urls')),
]
