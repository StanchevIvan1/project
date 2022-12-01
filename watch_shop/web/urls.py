from django.urls import path, include

from watch_shop.auth_app.views import UserDetailsView, UserEditView, UserDeleteView
from watch_shop.web.views import AboutView, IndexView, ContactView, ProductsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='user details'),
        path('edit/', UserEditView.as_view(), name='user edit'),
        path('delete/', UserDeleteView.as_view(), name='user delete'),
    ])),
)
