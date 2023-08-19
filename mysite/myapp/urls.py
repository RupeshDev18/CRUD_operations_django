from . import views
from django.urls import path
urlpatterns = [
    #/food/1
    #path('<int:item_id>/',views.detail,name='detail'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    #/food/
    #path('',views.index,name="index"),
    path('',views.index,name="index"),
    path('item/',views.item),
    #add items
    path('add',views.CreateItem.as_view(),name='create_item'),
    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]