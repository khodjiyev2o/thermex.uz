from django.urls import path

from .api_endpoints import brand, category, product, sold_products


application_urlpatterns = [
    path("category/", category.CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/brand/", brand.BrandListView.as_view(), name="brand-list"),
    path("brand/<int:pk>/", product.ProductListView.as_view(), name="product-list"),
    path("user/add/product/", sold_products.SoldProductCreatetView.as_view(), name="sold-product-create"),
    path("user/points/", sold_products.UserPointsView.as_view(), name="sold-product-user-points"),
    path("user/history/", sold_products.UserSoldProductListView.as_view(), name="sold-product-user-list"),
]

urlpatterns = application_urlpatterns
