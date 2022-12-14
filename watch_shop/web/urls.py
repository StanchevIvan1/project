from django.urls import path, include

from watch_shop.auth_app.views import UserDetailsView, UserEditView, UserDeleteView
from watch_shop.web.views import AboutView, IndexView, ContactView, ProductsView, ShoppingCartView, ProductEditView, \
    ProductsApiView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
    path('api/products/', ProductsApiView.as_view(), name=' api     products'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(), name='product edit'),
    path('products/purchase/<int:pk>/<int:product_id>', ProductsView.purchase, name='purchase'),
    path('cart', ShoppingCartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/item/<int:product_id>', ShoppingCartView.add_item, name='add item'),
    path('cart/sub/<int:pk>/item/<int:product_id>', ShoppingCartView.subtract_item, name='sub item'),
    path('cart/<int:pk>/product/<int:product_id>/remove', ShoppingCartView.remove_item_from_cart, name='remove product'),
    path('cart/<int:pk>/product/remove/all', ShoppingCartView.clear_cart, name='clear cart'),
    path('cart/<int:pk>/checkout', ShoppingCartView.checkout, name='checkout'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='user details'),
        path('edit/', UserEditView.as_view(), name='user edit'),
        path('delete/', UserDeleteView.as_view(), name='user delete'),
    ])),
)
