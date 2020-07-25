from django.urls import path

from portfolio import views


urlpatterns = [
                # path('/',views.show_index,name="index"),
    path('', views.project_list, name="itemget"),
    # path("", views.ProductListView.as_view(), name="item2"),

    # path('', views.images_list, name='image_data'),

]
