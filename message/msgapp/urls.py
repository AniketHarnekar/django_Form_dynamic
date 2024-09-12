from django.urls import path
from msgapp import views
from msgapp.views import ContactForm

urlpatterns = [
    #path('urlpattern',views.function_name)
    #path('urlpattern',ClassName.as_view())
    path('about',views.about),
    path('delete/<eid>',views.delete),
    path('classbase',ContactForm.as_view()),
    path('classbase/<eid>',ContactForm.as_view()),
    path('hello',views.hello),
    path('demo',views.demo),
    path('main',views.main),
    path('product',views.product),
    path('cart',views.cart),
    path('form',views.form),
    path('dashboard',views.dashboard),
    path('edit/<eid>',views.edit)
]
