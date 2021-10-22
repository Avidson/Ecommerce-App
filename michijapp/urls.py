from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from michijapp import views
from .views import (
        HomeView,
        ProductView,
        add_to_cart,
        remove_from_cart,
        reduce_quantity_item,
        OrderSummaryView,
        CheckoutView,
        SearchResultView
)

app_name = 'michijapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('michproduct/<pk>/', ProductView.as_view(), name="michproduct"),
    path('add-to-cart/<pk>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', views.remove_from_cart, name='remove-from-cart'),
    path('search/', views.SearchResultView.as_view(), name='search_results'),
    path('cart', OrderSummaryView.as_view(), name='cart'),
    path('reduce-quantity-item/<pk>/', views.reduce_quantity_item, name="reduce-quantity-item"),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('contact', views.contact_page, name='contact'),
    path('search/', views.SearchResultView.as_view(), name='search_results'),
    path('profile/<pk>', views.ProfileView.as_view(), name='profile')
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
