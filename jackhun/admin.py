from django.contrib import admin
from .models import Items, OrderItems, Orders, PostImage, Message, EmailSubscription, Profile, CheckoutAddress, Payment, Category
# Register your models here.



class PostImageAdmin(admin.StackedInline):
    model = PostImage


class ItemsAdmin(admin.ModelAdmin):
    list_display=('item_name', 'price', 'discount_price', 'category', 'slug', 'available')
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug' : ('item_name',)}
    #inlines = [PostImageAdmin]
admin.site.register(Items, ItemsAdmin)

class OrderItemsAdmin(admin.ModelAdmin):
    list_display=('owner', 'ordered', 'item', 'quantity', 'time')
admin.site.register(OrderItems, OrderItemsAdmin)

class OrdersAdmin(admin.ModelAdmin):
    model = Orders
    list_display=('owner', 'start_date', 'ordered', 'ordered_date')
admin.site.register(Orders, OrdersAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_contact', 'your_address', 'leave_a_message')

admin.site.register(Message, MessageAdmin)

class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display=('email', 'name')
admin.site.register(EmailSubscription, EmailSubscriptionAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'Biography', 'profile_pic')
admin.site.register(Profile, ProfileAdmin)

class CheckoutAddressAdmin(admin.ModelAdmin):
    list_display = ('owner', 'street_address', 'apartment_address', 'zip', 'tel', 'country', 'payment_option')
    inlinesModelAdmin = [OrderItems]
admin.site.register(CheckoutAddress, CheckoutAddressAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'paystack_id', 'amount', 'timestamp')
admin.site.register(Payment, PaymentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'slug')
    prepopulated_fields = {'slug' : ('item_name',)}
admin.site.register(Category, CategoryAdmin)
