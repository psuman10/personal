from django.contrib import admin

from .models import Product,Cart,OrderPlaced,Customer


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','brand','category','product_image']
admin.site.register(Product,ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
admin.site.register(Cart,CartAdmin)



class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','customer',product','quantity','ordered_date','status']
admin.site.register(OrderPlaced,OrderPlacedAdmin)


class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','state']
admin.site.register(Customer,CustomerModelAdmin)




