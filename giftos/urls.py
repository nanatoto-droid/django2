from django.urls import path
from giftos import views

urlpatterns = [
    path('',views.index,name='index'),
    path('',views.shop,name='shop'),
    path('',views.testimonial,name='testimonial'),
    path('',views.contact, name='contact'),
    path('',views.why,name='why'),
]