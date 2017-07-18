from django.conf.urls import url
from shop_order import views

urlpatterns = [
    url(r'^order/$', views.OrderView.as_view(), name='order'),
]
