from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from jackhun.views import(
    HomeView,
    ProductView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    reduce_quantity_item,
    CheckoutView,
    SearchResultView,
    ProfileView,
    dashboard,
    register_page,
    about_page,
    order_confirm,
    PaymentView,
    CategoryView,
    register_done
    #cart_add,
    #cart_remove,
    #cart_detail

 )
from jackhun import views

app_name = 'jackhun'

urlpatterns = [
    path('', views.HomeView, name="home"),
    path('<slug:category_slug>/', views.HomeView, name='product_list_by_category'),
    path('jackproduct/<pk>', views.ProductView.as_view(), name="jackproduct"),
    path('add-to-cart/<pk>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<pk>/', remove_from_cart, name="remove-from-cart"),
    path('cart', OrderSummaryView.as_view(), name='cart'),
    #path('add/<pk>/', views.cart_add, name='add'),
    #path('remove/<pk>/', views.cart_remove, name='remove'),
    #path('cart', views.cart_detail, name='cart'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name="reduce-quantity-item"),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('contact', views.contact_page, name='contact'),
    path('search/', views.SearchResultView.as_view(), name='search_results'),
    path('profile/<pk>', views.ProfileView.as_view(), name='profile'),
    path('dashboard', views.dashboard, name='dashboard' ),
    path('register', views.register_page, name='register'),
    path('about', views.about_page, name='about'),
    path('confirmation', views.order_confirm, name='confirmation'),
    path('navtest', views.navbar_item, name='navtest'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('category/<category>/', CategoryView.as_view(), name='category'),
    path('register-done', views.register_done, name='register-done')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
