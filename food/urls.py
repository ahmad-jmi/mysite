from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    # Defaul food url
    path('', views.index,name='index'),
    #food/1
    path('items/', views.items, name='items'),
    path('<int:item_id>/', views.detail, name='detail'),
    # add item
    path('add/',views.create_item, name='create_item'),
    #edit
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    #delete
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]