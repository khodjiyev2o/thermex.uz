from django.urls import path

from .api_endpoints import child_category, parent_category, prize_product, purchase_prize


application_urlpatterns = [
    path("prize-category/", parent_category.PrizeParentCategoryListView.as_view(), name="prize-category-list"),
    path("child-category/<int:pk>/product/", prize_product.PrizeProductListView.as_view(), name="prize-product-list"),
    path("product/", purchase_prize.UserPurchasePrizeProductView.as_view(), name="prize-product-purchase"),
    path(
        "prize-category/<int:pk>/child-category/",
        child_category.PrizeChildCategoryListView.as_view(),
        name="prize-child-category-list",
    ),
]

urlpatterns = application_urlpatterns
