from multiprocessing import context
from traceback import print_tb
#from types import NoneType
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpRequest,HttpResponse, JsonResponse,HttpResponseRedirect,HttpResponseServerError
from sebacatalog.models import DboCategoriasWeb,DboProductocatWeb
from sebacatalog.models import DboStpdaa,DboVeclaa,DboStlpaa,DboStliaa,DboVecvaa,DboVedfaa,DboGzemaa,DboVecoaa,DboVenuaa

#from django.template import loader

import mercadopago
import json
import datetime

# def index(request):
#     return HttpResponse("Seba Veterinaria")

#just text
# def index(request):
#     lista_categorias=DboCategoriasWeb.objects.all()
#     lista_categorias=lista_categorias.values()
#     output_categorias = ', '.join([categoria['descripcion'] for categoria in lista_categorias])
#     return HttpResponse(output_categorias)
#     #lista_categorias[0]['descripcion']


#with template
# def index(request):
#     lista_categorias=DboCategoriasWeb.objects.all()
#     #lista_categorias=lista_categorias.values()
#     template = loader.get_template('sebacatalog/index.html')
#     context = {
#         'categorias': lista_categorias,
#     }
#     return HttpResponse(template.render(context, request))

#Sin importar loader ni HttpResponse
def index(request):
    lista_categorias=DboCategoriasWeb.objects.filter(nivel="1",activo="S")
    context = {'categorias': lista_categorias}
    return render(request, 'sebacatalog/index.html', context)   

def categorias_nivel_2(request,idcategoria):
    lista_categorias=DboCategoriasWeb.objects.filter(nivel="2",idcategoriaagrupa=idcategoria,activo="S")
    context = {'categorias': lista_categorias}
    return render(request, 'sebacatalog/categorias_level2.html', context)  


def categorias_nivel_3(request,idcategoria):
    lista_categorias=DboCategoriasWeb.objects.filter(nivel="3",idcategoriaagrupa=idcategoria,activo="S")
    context = {'categorias': lista_categorias}
    return render(request, 'sebacatalog/categorias_level3.html', context)  

def lista_productos(request,idcategoria):
    #Solo considera Productos Excel
    #lista_producto=DboProductocatWeb.objects.filter(categoria=idcategoria)

    #Excel contra Gestion Productos
    #get logged customer later
    # idcliente="W00015"
    # #lista usuario
    # user_info=DboVeclaa.objects.filter(cod_codigo=idcliente)
    # user_info=user_info.values()[0]['cod_listapr']
    # #print (user_info)

    # #user_info=DboVeclaa.objects.raw("SELECT dbo_veclaa.cod_codigo,dbo_veclaa.dat_razonsocial,dbo_veclaa.cod_listapr,dbo_stliaa.dat_descripcion as desc_listavta,dbo_veclaa.cod_convta,dbo_vecvaa.dat_descripcion as desc_condvta, dbo_veclaa.dat_domicilio,dbo_veclaa.dat_localidad FROM dbo_veclaa LEFT JOIN dbo_stliaa ON dbo_veclaa.cod_listapr=dbo_stliaa.cod_codigo LEFT JOIN dbo_vecvaa ON dbo_vecvaa.cod_codigo=dbo_veclaa.cod_codigo WHERE dbo_veclaa.cod_codigo='W00015'")
    
    # product_list=DboStpdaa.objects.raw("SELECT dbo_stpdaa.idproducto,dbo_stpdaa.cod_producto, \
    # dbo_ProductoCat_Web.Descripcion as dat_descipcion01,  dbo_stpdaa.dat_rela12,dbo_stpdaa.dat_estante, \
    # dbo_stlpaa.imp_precio,dbo_stpdaa.cod_familia,dbo_ProductoCat_Web.Foto  \
    # FROM dbo_stpdaa \
    # JOIN dbo_stlpaa ON  dbo_stlpaa.cod_producto=dbo_stpdaa.cod_producto \
    # JOIN dbo_ProductoCat_Web ON  dbo_ProductoCat_Web.Producto=dbo_stpdaa.cod_producto \
    # JOIN dbo_Categorias_Web ON  dbo_ProductoCat_Web.Categoria=dbo_Categorias_Web.IdCategoria \
    # WHERE dbo_ProductoCat_Web.Categoria="+str(idcategoria)+ \
    # " AND dbo_stpdaa.dat_vercam=1 \
    # AND dbo_stlpaa.cod_codigo=0  \
    # AND dbo_stpdaa.dat_habilitado='S' \
    # AND dbo_ProductoCat_Web.Activo='S' \
    # ORDER BY dbo_stpdaa.cod_producto ASC")        

   
    #Descuento es 0 por default
    # product_list.dat_dtoitem=0
    # product_list.dat_dtoadic=0

    #Controlar foto,agregar descuento si lo tiene

    product_list=DboProductocatWeb.objects.raw("SELECT * FROM dbo_productocat_web \
                                               WHERE dbo_productocat_web.Categoria='"+str(idcategoria)+"' \
                                                AND dbo_productocat_web.Activo='S'"
                                               )
   
    print(product_list)
    for producto in product_list:
        print(producto.producto)
        print(producto.descripcion)
        print(producto.precio)
        print(producto.activo)
        print(producto.foto)
        #redondeo de decimales
        #producto.imp_precio=round(producto.imp_precio,2)

        #print(producto.cod_producto)
        #print(producto.dat_descipcion01)
        #print(producto.dat_rela12)
        #print(round(producto.imp_precio,2))
        #si no tiene foto cambiar a no imagen.png 
        # if producto.Foto==None:
        #     print("None!")
        # else:
        #     print (producto.Foto)
        #Hay descuentos?
        #
        # producto_descuento=DboVedfaa.objects.raw("SELECT dbo_vedfaa.nro_serie,dbo_vedfaa.dat_dtoitem,\
        # dbo_vedfaa.dat_dtoadic \
        # FROM dbo_vedfaa \
        # WHERE dbo_vedfaa.dat_vercam=1 \
        # AND dbo_vedfaa.cod_cliente="+user_info+ \
        # " AND dbo_vedfaa.cod_familia="+producto.cod_familia+" LIMIT 1")

        # if producto_descuento!=None:
        #     for desc in producto_descuento:
        #         product_list.dat_dtoitem=desc.dat_dtoitem
        #         product_list.dat_dtoadic=desc.dat_dtoadic
            
        #     print("Descuento ",product_list.dat_dtoitem)
        #     print("Desc Adic ",product_list.dat_dtoadic)
        # print()


    context={'productos':product_list}
    #return render(request,'sebacatalog/lista_productos.html', context)  
    
    #with JS cart
    return render(request,'sebacatalog/lista_productos_cart.html', context)  


#mercadopago    
def mercadopago_controller(request,idproducto):

    # Agrega credenciales
    sdk = mercadopago.SDK("TEST-7399728750816177-031617-e0e9a8555dcbf9676961169a9445324e-667108987")

    #Traer producto de la DB
    # Producto_a_pagar=DboProductocatWeb.objects.filter(pc_id=idproducto)
    # Producto_a_pagar=Producto_a_pagar.values()

    #get logged customer later
    #lista usuario
    user_info=DboVeclaa.objects.filter(cod_codigo="W00015")
    user_info=user_info.values()[0]['cod_listapr']
    #print (user_info)

    #user_info=DboVeclaa.objects.raw("SELECT dbo_veclaa.cod_codigo,dbo_veclaa.dat_razonsocial,dbo_veclaa.cod_listapr,dbo_stliaa.dat_descripcion as desc_listavta,dbo_veclaa.cod_convta,dbo_vecvaa.dat_descripcion as desc_condvta, dbo_veclaa.dat_domicilio,dbo_veclaa.dat_localidad FROM dbo_veclaa LEFT JOIN dbo_stliaa ON dbo_veclaa.cod_listapr=dbo_stliaa.cod_codigo LEFT JOIN dbo_vecvaa ON dbo_vecvaa.cod_codigo=dbo_veclaa.cod_codigo WHERE dbo_veclaa.cod_codigo='W00015'")
    
    product_list=DboStpdaa.objects.raw("SELECT dbo_stpdaa.idproducto,dbo_stpdaa.cod_producto, \
    dbo_ProductoCat_Web.Descripcion as dat_descipcion01,  dbo_stpdaa.dat_rela12,dbo_stpdaa.dat_estante, \
    dbo_stlpaa.imp_precio,dbo_stpdaa.cod_familia,dbo_ProductoCat_Web.Foto  \
    FROM dbo_stpdaa \
    JOIN dbo_stlpaa ON  dbo_stlpaa.cod_producto=dbo_stpdaa.cod_producto \
    JOIN dbo_ProductoCat_Web ON  dbo_ProductoCat_Web.Producto=dbo_stpdaa.cod_producto \
    JOIN dbo_Categorias_Web ON  dbo_ProductoCat_Web.Categoria=dbo_Categorias_Web.IdCategoria \
    WHERE dbo_stpdaa.idproducto= "+str(idproducto)+ \
    " AND dbo_stpdaa.dat_vercam=1 \
    AND dbo_stlpaa.cod_codigo=0  \
    AND dbo_stpdaa.dat_habilitado='S' \
    AND dbo_ProductoCat_Web.Activo='S' \
    ORDER BY dbo_stpdaa.cod_producto ASC")      
    
    product_list.dat_dtoitem=0
    product_list.dat_dtoadic=0

    for producto in product_list:
        # print(producto.cod_producto)
        # print(producto.dat_descipcion01)
        # print(producto.dat_rela12)
        # print(round(producto.imp_precio,2))

        #redondeo de decimales
        producto.imp_precio=round(producto.imp_precio,2)

        #si no tiene foto cambiar a no imagen.png 
        if producto.Foto==None:
            print("None!")
        else:
            print (producto.Foto)

        #Hay descuentos?
        producto_descuento=DboVedfaa.objects.raw
        ("SELECT dbo_vedfaa.nro_serie,dbo_vedfaa.dat_dtoitem,\
        dbo_vedfaa.dat_dtoadic \
        FROM dbo_vedfaa \
        WHERE dbo_vedfaa.dat_vercam=1 \
        AND dbo_vedfaa.cod_cliente="+user_info+ \
        " AND dbo_vedfaa.cod_familia="+producto.cod_familia+" LIMIT 1")

        if producto_descuento!=None:
            for desc in producto_descuento:
                product_list.dat_dtoitem=desc.dat_dtoitem
                product_list.dat_dtoadic=desc.dat_dtoadic
            
        #     print("Descuento ",product_list.dat_dtoitem)
        #     print("Desc Adic ",product_list.dat_dtoadic)
        # print()

        Producto_a_pagar={
            'title':producto.dat_descipcion01,
            'quantity': 1,
            'unit_price': float(producto.imp_precio),##evita json cant serialize decimal error por la DB
            "picture_url":producto.Foto,
        }

        #print(Producto_a_pagar)

    #crear preferencia de MercadoPago
    # preference_data = {
    #     "items": [
    #         {
    #             "title": Producto_a_pagar['title'],
    #             "quantity": 1,
    #             "unit_price": 75.76,
    #         }
    #     ]
    # }

    # print(preference_data)

    # print()

    # print("now the other one")

    preference_data = {
        "items": [
                Producto_a_pagar
        ],
        
        "payer": {
            "name": "Jorge ",
            "surname": "Garquetti",
            "email": "ceo@argentina.com.ar",
            "phone": {
                "area_code": "11",
                "number": "5776-4441"
            },
            "identification": {
                "type": "DNI",
                "number": "12345678"
            },
            "address": {
                "street_name": "UnaCalle",
                "street_number": 217,
                "zip_code": "1908"
            }
        },

        "back_urls": {
            "success": "http://127.0.0.1:8000/slicatalog/", #usar redirect, procesar status pedido
            "failure": "http://127.0.0.1:8000/slicatalog/", #usar para eso otro endpoint
            "pending": "http://127.0.0.1:8000/slicatalog/"
        },
    }

    #print(preference_data)

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    #preference = preference_response['response']['id']
    print("This preference:")
    print(preference)
    #sandbox_init_point=preference['sandbox_init_point']
    context = {'preference': preference}


    return render(request, 'sebacatalog/checkout.html', context)

def qr_controller(request):
     return render(request, 'slicatalog/qrscan.html')   


def cart_controller(request):
     return render(request, 'slicatalog/cart.html')

@csrf_exempt
def checkout_controller(request):
    #cart_data = json.loads(request.body)
    cart_data=json.loads(request.POST['shopping_cart'])
    print("Request!:")
   
    print(cart_data)
    #print(data['shopping_cart'])
    #cart_data=cart_data['shopping_cart']

    #cart format
    # [
    #     {"name":"OLD PRINCE CORDERO ADULT M&L X 15+3KG",
    #     "price":8800,
    #     "count":1},
    #     {"name":"OLD PRINCE CORDERO ADULT M&L X 3KG",
    #     "price":2030,
    #     "count":1}
    # ]
    
    # Agrega credenciales
    sdk = mercadopago.SDK("TEST-7399728750816177-031617-e0e9a8555dcbf9676961169a9445324e-667108987")
    #Cart de MercadoPago
    #preference_data=dict()
    #preference_data['']
    preference_data = {
        "items": [],  
        
        "payer": {
            "name": "Jorge",
            "surname": "Test",
            "email": "ceo@argentina.com.ar",
            "phone": {
                "area_code": "11",
                "number": "7844-4441"
            },
            "identification": {
                "type": "DNI",
                "number": "12345678"
            },
            "address": {
                "street_name": "UnaCalle",
                "street_number": 217,
                "zip_code": "1908"
            }
        },

        "back_urls": {
            "success": "http://127.0.0.1:8000/slicatalog/postpayment", #usar redirect, procesar status pedido
            "failure": "http://127.0.0.1:8000/slicatalog/", #usar para eso otro endpoint
            "pending": "http://127.0.0.1:8000/slicatalog/"
        },
    }
    
    #Recorrer cart
    for producto_comprado in cart_data:
    #      print(producto_comprado['name'])
    #      print(producto_comprado['count'])
 
            
        product_list=DboProductocatWeb.objects.raw("SELECT * FROM dbo_productocat_web \
                                               WHERE dbo_productocat_web.Descripcion='"+str(producto_comprado['description'])+"' \
                                                AND dbo_productocat_web.Activo='S'"
                                               )
       
    
        print(product_list)
        for producto in product_list:
            print(producto.producto)
            print(producto.descripcion)
            print(producto.precio)
            print(producto.activo)
            print(producto.foto)

    #       #redondeo de decimales
            producto.precio=round(producto.precio,2)

            #si no tiene foto cambiar a no imagen.png 
            if producto.foto==None:
                print("None!")
            else:
                print (producto.foto)


            Producto_a_pagar={
                'title':producto.descripcion,
                'quantity': producto_comprado['count'],
                'unit_price': float(producto.precio),##evita json cant serialize decimal error por la DB
                "picture_url":producto.foto,
            }

            print(Producto_a_pagar)
            print()

            #Agregar a preferencia MercadoPago
            preference_data['items'].append(Producto_a_pagar)

    
  

    print(preference_data)

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    # #preference = preference_response['response']['id']
    print("This preference:")
    print(preference)
    # sandbox_init_point=preference['sandbox_init_point']
    context = {'preference': preference}


    return render(request, 'sebacatalog/checkout.html', context)


    #return HttpResponse("This cart is making me thirsty!")
    #return JsonResponse(preference,safe=False)

@csrf_exempt
def payment_controller(request):
    compra = json.loads(request.COOKIES['compra'])
    print(compra)

    #return render(request, 'sebacatalog/checkout.html', context)
    return HttpResponse("Carro de compras")

#Luego de realizado el pago
def postpayment_controller(request):
    mercadopago_response=request.GET
    #MercadoPago devuelve:
    #<QueryDict: 
    # {
    # 'collection_id': ['1310604884'],
    # 'collection_status': ['approved'], 
    # 'payment_id': ['1310604884'], 
    # 'status': ['approved'],
    # 'external_reference': ['null'], 
    # 'payment_type': ['credit_card'], 
    # 'merchant_order_id': ['6665312634'],
    # 'preference_id': ['667108987-359923ca-eae0-4f3a-aaf2-037307d0068b'], 
    # 'site_id': ['MLA'], 
    # 'processing_mode': ['aggregator'], 
    # 'merchant_account_id': ['null']
    # }
    # >
    mercadopago_transaccionid=mercadopago_response['collection_id']

    print(mercadopago_response['collection_status'])
    if (mercadopago_response['collection_status']=="approved"):
        print("Aprobada!")
    else:
        print("Transaccion Rechazada!")

    #de donde saco cliente y vendedor sino hay login!
    #forzar temporales
    customer_id="W00015"
    ##vendedor_asignado=999;
    vendedor_asignado=DboVeclaa.objects.filter(cod_codigo=customer_id)
    vendedor_asignado=vendedor_asignado.values()[0]['cod_vendedor']

    print(f"Vendedor Asignado es:{vendedor_asignado}")

    pedido_fecha=datetime.datetime.now().date()
    pedido_hora=datetime.datetime.now().time()
    print(f"Fecha: {pedido_fecha}")
    print(f"Hora: {pedido_hora}")

    select=""
    select+="SELECT dbo_veclaa.nro_serie,dbo_veclaa.cod_codigo,"
    select+="dbo_veclaa.dat_razonsocial,"
    select+="dbo_veclaa.cod_listapr,"
    select+="dbo_stliaa.dat_descripcion as desc_listavta,"
    select+="dbo_veclaa.cod_convta,"
    select+="dbo_vecvaa.dat_descripcion as desc_condvta,"
    select+="dbo_veclaa.dat_domicilio,"
    select+="dbo_veclaa.dat_localidad"
    select+=" FROM dbo_veclaa"
    select+=" LEFT JOIN dbo_stliaa ON dbo_stliaa.cod_codigo=dbo_veclaa.cod_listapr"
    select+=" LEFT JOIN dbo_vecvaa ON dbo_veclaa.cod_convta=dbo_vecvaa.cod_codigo"
    select+=" WHERE dbo_veclaa.cod_codigo='"+customer_id+"'"
  
    customer_info=DboVeclaa.objects.raw(select)

    if customer_info!=None:
        for info in customer_info:
            #print("====")
            #print(info.dat_razonsocial)

            customer_pricelist=info.cod_listapr
            customer_pricelist_desc=info.desc_listavta
            
            customer_saleconditions=info.cod_convta
            customer_saleconditions_desc=info.desc_condvta

            #No hay sucursales en Veterinaria
            user_suc_codigo=""

            #Transporte
            customer_transporte=DboVeclaa.objects.filter(cod_codigo=customer_id)
            customer_transporte=customer_transporte.values()[0]['cod_transporte']
            #print(f"Transporte: {customer_transporte}")
            pedido_empresapedidosweb=DboGzemaa.objects.filter(dat_vercam=1)
            pedido_empresapedidosweb=pedido_empresapedidosweb.values()[0]['cod_ce_empresa']
            #print(f"Empresa:{pedido_empresapedidosweb}")

            #Comprobante,sucursal,codnro
            select=""
            select+="SELECT dbo_vecoaa.nro_serie,dbo_vecoaa.cod_codigo,dbo_vecoaa.dat_descripcion"
            select+=",dbo_vecoaa.cod_su_sucursal,dbo_vecoaa.cod_numeracion,"
            select+="dbo_gzsuaa.dat_empresa"
      
            select+=" FROM dbo_vecoaa"
            select+=" JOIN dbo_gzsuaa ON dbo_vecoaa.cod_su_sucursal=dbo_gzsuaa.nro_sucursal AND dbo_gzsuaa.dat_vercam=1"
            select+=" WHERE dbo_vecoaa.dat_vercam=1"
        
            #solo el primer row necesitamos,por eso el 0
            pedido_comprosucunumer=DboVecoaa.objects.raw(select)[0]
            pedido_suc=pedido_comprosucunumer.cod_su_sucursal
            #print(f"Pedido Sucursal :{pedido_suc}")
            pedido_codnro=pedido_comprosucunumer.cod_numeracion
            #print(f"Pedido Cod Nro :{pedido_codnro}")

            #TODO:Harcodeado para Sebastian
            pedido_compro="PWR"

            pedido_proxnro=DboVenuaa.objects.filter(dat_vercam=1,cod_codigo=pedido_codnro)[0]
            pedido_proxnro=pedido_proxnro.dat_proxnroa
            #print(f"Proximo Nro :{pedido_proxnro}")

            #============VEPH==========


        
            
            




    else:
        return HttpResponseServerError     

    return redirect('/slicatalog/')

  