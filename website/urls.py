from django.conf.urls import url
from website import views as website_views

urlpatterns = [
    url(r'^$', website_views.home, name='home'),
    url(r'^/policy/$', website_views.policy, name='policy'),

]
