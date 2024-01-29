from django.urls import path

from . import views

urlpatterns = [
    #path,view.viewname,name=name
    path('', views.index, name='index'),
    path('nivel2/<int:idcategoria>/', views.categorias_nivel_2, name='categorias_nivel2'),
    path('nivel3/<int:idcategoria>/', views.categorias_nivel_3, name='categorias_nivel3'),
    path('productos/<int:idcategoria>/', views.lista_productos, name='lista_productos'),
    path('mercadopago/<int:idproducto>/', views.mercadopago_controller, name='mercadopago_controller'),
    path('checkout/<int:idproducto>/', views.mercadopago_controller, name='mercadopago_controller'),
    path('qr/', views.qr_controller, name='qr_controller'),
    path('cart/', views.cart_controller, name='cart_controller'),
    path('checkout_cart/', views.checkout_controller, name='checkout_controller'),
    path('payment/', views.payment_controller, name='payment_controller'),
    path('postpayment/', views.postpayment_controller, name='postpayment_controller'),
    
    
    path('ordersummary/', views.order_summary, name='order_summary'),
    path('addressbook/', views.address_book, name='address_book'),
    path('confirmed_order/', views.confirmed_order, name='confirmed_order'),
    

]

