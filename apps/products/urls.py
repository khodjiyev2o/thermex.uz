from django.urls import path

from .api_endpoints import category, brand, product

application_urlpatterns = [
    path("category/", category.CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/brand/", brand.BrandListView.as_view(), name="brand-list"),
    path("brand/<int:pk>/", product.ProductListView.as_view(), name="product-list"),
]

urlpatterns = application_urlpatterns
