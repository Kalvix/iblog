from django.conf.urls.static import static
from django.urls import path

from iblog import settings
from projects import views

urlpatterns = [
                 # path("",views.project_index,name="project_index"),
    path("", views.ProductListView.as_view(), name="project_index"),
    path("", views.product_detail, name="product_details"),
    path("", views.project_categories, name="category"),
    path("<int:pk>",views.project_detail,name="project_detail")
              ]