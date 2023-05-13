from django.urls import path

from .api_endpoints import category, brand

application_urlpatterns = [
    path("category/", category.CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/brand/", brand.BrandListView.as_view(), name="brand-list"),
]

urlpatterns = application_urlpatterns
