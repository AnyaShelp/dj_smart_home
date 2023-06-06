from django.urls import path
from django.contrib import admin
from .views import DemoView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', DemoView.as_view()),
    path('sensors/<pk>/', DemoView.as_view())
