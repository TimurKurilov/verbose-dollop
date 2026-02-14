from django.contrib import admin
from django.urls import path
from content import views as contentviews
from users import views as authviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", contentviews.page, name="page"),
    path("create_task/", contentviews.create_task, name="create"),
    path("list/", contentviews.all_task, name="all_task"),
    path('register/', authviews.RegisterView.as_view(), name='register'),
    
]
