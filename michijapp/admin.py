from django.contrib import admin
from .models import Item, OrderItem, Order, PostImage, EmailSubscription, Message, Profile
# Register your models here.



class PostImageAdmin(admin.StackedInline):
    model = PostImage
#admin.site.register(PostImage)

class ItemAdmin(admin.ModelAdmin):
    list_display=('item_name', 'price', 'discount_price', 'category', 'label')
    #inlines = [PostImageAdmin]
admin.site.register(Item,ItemAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display=('user', 'ordered', 'item', 'quantity')
admin.site.register(OrderItem, OrderItemAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=('user', 'start_date', 'ordered')
admin.site.register(Order, OrderAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_contact', 'your_address', 'leave_a_message')

admin.site.register(Message, MessageAdmin)

class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display=('email', 'name')
admin.site.register(EmailSubscription, EmailSubscriptionAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'Biography', 'profile_pic')
admin.site.register(Profile, ProfileAdmin)
