
from django.contrib import admin
from django.urls import path
from products.views import AllProduct

urlpatterns = [
    path('product/admin/', admin.site.urls),
    path('product/products/', AllProduct.as_view()),

]
