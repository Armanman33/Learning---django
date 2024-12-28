from django.url import path

from. import views
urlpatterns = [

    path('', views.days_list, name='days_list'),
    path('<int:auto>', views.dynamic_days_by_number),
    path('<str:auto>', views.dynamic_days, name='days-of-week'),
] 