
from django.urls import path 
from.import views 

urlpatterns = [
    path('',views.index,name='home'),
    path('arthtwe/<int:roll>',views.arthtwe,name='arthtwe'),
    path('arthele/<int:roll>',views.arthele,name='arthele'),
    path('commerceele/<int:roll>',views.commerceele,name='commerceele'),
    path('commercetwe/<int:roll>',views.commercetwe,name='commercetwe'),
    path('sciencetwe/<int:roll>',views.sciencetwe,name='sciencetwe'),
    path('scienceele/<int:roll>',views.scienceele,name='scienceele'),
    path('artele/',views.artele,name='artele'),
    path('arttwe/',views.arttwe,name='arttwe'),
    path('artele/',views.artele,name='artele'),
    path('commele/',views.commele,name='commele'),
    path('commtwe/',views.commtwe,name='commtwe'),
    path('sciele/',views.sciele,name='sciele'),
    path('scitwe/',views.scitwe,name='scitwe'),

]
