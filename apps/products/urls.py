from django.urls import path

from .api_endpoints import category, brand, product, sold_products

application_urlpatterns = [
    path("category/", category.CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/brand/", brand.BrandListView.as_view(), name="brand-list"),
    path("brand/<int:pk>/", product.ProductListView.as_view(), name="product-list"),
    path("user/add/product/", sold_products.SoldProductCreatetView.as_view(), name="sold-product-create"),
]

urlpatterns = application_urlpatterns
