from django.urls import path
from .import views
urlpatterns = [
    path('', views.home,name="home"),
    path('login_def/', views.login_def,name="login"),
    path('res/', views.register,name="register"),
    path('org_details/', views.org_details,name="org_details"),
    path('logout/', views.logout_def, name="logout"),
    path('profile/', views.profile_def, name="profile"),
    path('feedback/', views.feed_back, name="feedback"),
    path('aboutus/', views.about_us, name="aboutus"),
    path('contect/', views.contect_us, name="contect"),
    path('domain_form_stack/', views.domain_form_stack, name="domain_form_stack"),
    path('domain/', views.domain_def, name="domain"),
    path('stack/', views.stack_def, name="stack"),
    path('forms/', views.forms_def, name="forms"),
    path('chart_bot/', views.chart_bot, name="chart_bot"),
    path('request-otp/', views.request_otp, name='request_otp'),
    path('opt_verify/', views.opt_verify, name='opt_verify'),

    path('chart_reponse/', views.chart_reponse, name='chart_reponse'),
]
