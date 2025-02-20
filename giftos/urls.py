from django.urls import path
from giftos import views

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('contact/',views.contact, name='contact'),
    path('why/',views.why,name='why'),
]