from django.contrib import admin
from django.urls import path
from content import views as contentviews
from users import views as authviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", contentviews.page, name="page"),
    path("create_task/", contentviews.create_task, name="create"),
    path("list/", contentviews.all_task, name="all_task"),
    path("list/<slug:date>/", contentviews.tasks_by_date, name="tasks_by_date"),
    path("list/<slug:date>/<int:slot>/", contentviews.tasks_by_date_and_slot, name="tasks_by_date_and_slot"),
    path('register/', authviews.RegisterView.as_view(), name='register'),
    path('login/', authviews.LoginView.as_view(), name="login"),
    path('logout/', authviews.logout_view, name="logout"),
    
]
