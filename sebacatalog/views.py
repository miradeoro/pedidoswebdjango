from multiprocessing import context
from traceback import print_tb
#from types import NoneType
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpRequest,HttpResponse, JsonResponse
from sebacatalog.models import DboCategoriasWeb,DboProductocatWeb
from sebacatalog.models import DboStpdaa,DboVeclaa,DboStlpaa,DboStliaa,DboVecvaa,DboVedfaa

#from django.template import loader

import mercadopago
import json

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
    lista_categorias=DboCategoriasWeb.objects.filter(nivel="1")
    context = {'categorias': lista_categorias}
    return render(request, 'sebacatalog/index.html', context)   

def categorias_nivel_2(request,idcategoria):
    lista_categorias=DboCategoriasWeb.objects.filter(nivel="2",idcategoriaagrupa=idcategoria)
    context = {'categorias': lista_categorias}
    return render(request, 'sebacatalog/categorias_level2.html', context)  


def categorias_nivel_3(request,idcategoria):
    lista_categorias=DboCategoriasWeb.objects.filter(nivel="3",idcategoriaagrupa=idcategoria)
    context = {'categorias': lista_categorias}
    return render(request, 'sebacatalog/categorias_level3.html', context)  

def lista_productos(request,idcategoria):
    #Solo considera Productos Excel
    #lista_producto=DboProductocatWeb.objects.filter(categoria=idcategoria)

    #Excel contra Gestion Productos
    #get logged customer later
    idcliente="W00015"
    #lista usuario
    user_info=DboVeclaa.objects.filter(cod_codigo=idcliente)
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
    WHERE dbo_ProductoCat_Web.Categoria="+str(idcategoria)+ \
    " AND dbo_stpdaa.dat_vercam=1 \
    AND dbo_stlpaa.cod_codigo=0  \
    AND dbo_stpdaa.dat_habilitado='S' \
    AND dbo_ProductoCat_Web.Activo='S' \
    ORDER BY dbo_stpdaa.cod_producto ASC")          

    #Descuento es 0 por default
    product_list.dat_dtoitem=0
    product_list.dat_dtoadic=0

    #Controlar foto,agregar descuento si lo tiene
    for producto in product_list:

        #redondeo de decimales
        producto.imp_precio=round(producto.imp_precio,2)

        print(producto.cod_producto)
        print(producto.dat_descipcion01)
        print(producto.dat_rela12)
        print(round(producto.imp_precio,2))
        #si no tiene foto cambiar a no imagen.png 
        if producto.Foto==None:
            print("None!")
        else:
            print (producto.Foto)
        #Hay descuentos?
        #
        producto_descuento=DboVedfaa.objects.raw("SELECT dbo_vedfaa.nro_serie,dbo_vedfaa.dat_dtoitem,\
        dbo_vedfaa.dat_dtoadic \
        FROM dbo_vedfaa \
        WHERE dbo_vedfaa.dat_vercam=1 \
        AND dbo_vedfaa.cod_cliente="+user_info+ \
        " AND dbo_vedfaa.cod_familia="+producto.cod_familia+" LIMIT 1")

        if producto_descuento!=None:
            for desc in producto_descuento:
                product_list.dat_dtoitem=desc.dat_dtoitem
                product_list.dat_dtoadic=desc.dat_dtoadic
            
            print("Descuento ",product_list.dat_dtoitem)
            print("Desc Adic ",product_list.dat_dtoadic)
        print()


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
            "name": "Alejandro",
            "surname": "Ajler",
            "email": "ceo@soft54.com.ar",
            "phone": {
                "area_code": "11",
                "number": "5444-4441"
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
            "success": "http://127.0.0.1:8000/sebacatalog/", #usar redirect, procesar status pedido
            "failure": "http://127.0.0.1:8000/sebacatalog/", #usar para eso otro endpoint
            "pending": "http://127.0.0.1:8000/sebacatalog/"
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
     return render(request, 'sebacatalog/qrscan.html')   


def cart_controller(request):
     return render(request, 'sebacatalog/cart.html')

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
            "name": "Alejandro",
            "surname": "Ajler",
            "email": "ceo@soft54.com.ar",
            "phone": {
                "area_code": "11",
                "number": "5444-4441"
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
            "success": "http://127.0.0.1:8000/sebacatalog/", #usar redirect, procesar status pedido
            "failure": "http://127.0.0.1:8000/sebacatalog/", #usar para eso otro endpoint
            "pending": "http://127.0.0.1:8000/sebacatalog/"
        },
    }
    
    #get logged customer later
    #lista usuario
    user_info=DboVeclaa.objects.filter(cod_codigo="W00015")
    user_info=user_info.values()[0]['cod_listapr']
    #print (user_info)

    #print(type(cart_data))
    #print(cart_data)   
    
    #Recorrer cart
    for producto_comprado in cart_data:
    #      print(producto_comprado['name'])
    #      print(producto_comprado['count'])
 
            
        product_list=DboStpdaa.objects.raw("SELECT dbo_stpdaa.idproducto,dbo_stpdaa.cod_producto, \
        dbo_ProductoCat_Web.Descripcion as dat_descipcion01,  dbo_stpdaa.dat_rela12,dbo_stpdaa.dat_estante, \
        dbo_stlpaa.imp_precio,dbo_stpdaa.cod_familia,dbo_ProductoCat_Web.Foto  \
        FROM dbo_stpdaa \
        JOIN dbo_stlpaa ON  dbo_stlpaa.cod_producto=dbo_stpdaa.cod_producto \
        JOIN dbo_ProductoCat_Web ON  dbo_ProductoCat_Web.Producto=dbo_stpdaa.cod_producto \
        JOIN dbo_Categorias_Web ON  dbo_ProductoCat_Web.Categoria=dbo_Categorias_Web.IdCategoria \
        WHERE dbo_stpdaa.idproducto= "+str(producto_comprado['name'])+ \
        " AND dbo_stpdaa.dat_vercam=1 \
        AND dbo_stlpaa.cod_codigo=0  \
        AND dbo_stpdaa.dat_habilitado='S' \
        AND dbo_ProductoCat_Web.Activo='S' \
        ORDER BY dbo_stpdaa.cod_producto ASC")      
    
        product_list.dat_dtoitem=0
        product_list.dat_dtoadic=0

        for producto in product_list:
    #     # print(producto.cod_producto)
    #     # print(producto.dat_descipcion01)
    #     # print(producto.dat_rela12)
    #     # print(round(producto.imp_precio,2))

    #       #redondeo de decimales
            producto.imp_precio=round(producto.imp_precio,2)

            #si no tiene foto cambiar a no imagen.png 
            if producto.Foto==None:
                print("None!")
            else:
                print (producto.Foto)

    #     #Hay descuentos?
            producto_descuento=DboVedfaa.objects.raw
            ("SELECT dbo_vedfaa.nro_serie,dbo_vedfaa.dat_dtoitem,\
            dbo_vedfaa.dat_dtoadic \
            FROM dbo_vedfaa \
            WHERE dbo_vedfaa.dat_vercam=1 \
            AND dbo_vedfaa.cod_cliente="+user_info+ \
            " AND dbo_vedfaa.cod_familia="+producto.cod_familia+" LIMIT 1")

            # if producto_descuento!=None:
            #     for desc in producto_descuento:
            #         product_list.dat_dtoitem=desc.dat_dtoitem
            #         product_list.dat_dtoadic=desc.dat_dtoadic
                
    #     #     print("Descuento ",product_list.dat_dtoitem)
    #     #     print("Desc Adic ",product_list.dat_dtoadic)
    #     # print()

            Producto_a_pagar={
                'title':producto.dat_descipcion01,
                'quantity': producto_comprado['count'],
                'unit_price': float(producto.imp_precio),##evita json cant serialize decimal error por la DB
                "picture_url":producto.Foto,
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
    return HttpResponse("This cart is making me thirsty!")

  ##save order   
# """   public function submit(Request $request)
#   {
     
#     //dd($request);
#     //$request->session()->forget('elpedido');
#     $obs1="";
#     $obs2="";
#     $obs3="";
#     $obs4="";
#     $obs5="";
#     $suc_clienterq="";
#     $transp_clienterq="";
#     $orden_compra="";
    
#     //get request from order details form

#     //Observations
#     $obs1 = $request->input('observacion1', '');
#     $obs2 = $request->input('observacion2', '');
#     $obs3 = $request->input('observacion3', '');
#     $obs4 = $request->input('observacion4', '');
#     $obs5 = $request->input('observacion5', '');

#     //VET no lleva sucursal,transporte, ni OC
#     //sucursal cliente desc
#     //$suc_clienterq=$request->input('suc_cliente', '');
#     //dd($suc_clienterq);

#     //transporte desc
#     //$transp_clienterq=$request->input('transp_cliente', '');

#     //orden de compra
#     //$orden_compra=$request->input('ordencompra', '');


#     //get session
#     //session should have customer id too
#     //branch id too
#     //price list too
#     //transporte too
#      //$customerid="120032";
  
#     $customerid=$request->session()->get('logged_user');
#     $customerid=$customerid['login_customerid'];
   
#      //simulate comments
#      $fake_datobserva01="";

#      //Vendedor asignado
#      //$pedido_vendedorasignado=999;//vendedor temporal
#      $pedido_vendedorasignado = DB::table('dbo_veclaa')
#      ->select('dbo_veclaa.cod_vendedor')
#      ->where([
#        ['dbo_veclaa.cod_codigo', '=', $customerid],
#        ])
#      ->get();

#      $pedido_vendedorasignado=json_decode($pedido_vendedorasignado,true);
#      $pedido_vendedorasignado=$pedido_vendedorasignado[0]['cod_vendedor'];
#      //dd($pedido_vendedorasignado);

#      $pedido_datetimenow=date('Y-m-d');
#      $pedido_timenow=date('H:i:s');
#      //dd($pedido_timenow);
     
#      $pedido_sucursalcli=""; //reemplazar con query

#      $cart_now = $request->session()->get('elpedido');
#      //dd($cart_now);
#      //$cart_now=$cart_now[0];
#      //flush session
#      $request->session()->forget('elpedido');
      
#      //echo("su pedido es el siguiente");
#      //echo(json_decode((string)$cart_now,true));
#     //dd($cart_now[0]);

#     //===CARGA PRE INICIAL - DATOS CLIENTE====
#     $customer_info = DB::table('dbo_veclaa')
#             ->select('dbo_veclaa.cod_codigo','dbo_veclaa.dat_razonsocial','dbo_veclaa.cod_listapr','dbo_stliaa.dat_descripcion as desc_listavta',
#             'dbo_veclaa.cod_convta','dbo_vecvaa.dat_descripcion as desc_condvta','dbo_veclaa.dat_domicilio',
#             'dbo_veclaa.dat_localidad')
#             ->leftjoin('dbo_stliaa', function ($join) {
#                 $join->on('dbo_veclaa.cod_listapr', '=', 'dbo_stliaa.cod_codigo');
#                       //->on('dbo_stliaa.dat_vercam', '=', 1);
#             })
#             ->leftjoin('dbo_vecvaa', function ($join) {
#                  $join->on('dbo_veclaa.cod_convta', '=', 'dbo_vecvaa.cod_codigo');
#             //      $join->on('dbo_vecvaa.dat_vercam', '=', 1);
#             })
        
#             ->where('dbo_veclaa.cod_codigo', '=', $customerid)
#             ->get();

      
     
#      $customer_info=json_decode($customer_info,true);
#      $customer_info=$customer_info[0];

#      //dd($customer_info);

#      $customer_pricelist=$customer_info['cod_listapr'];
#      $customer_pricelist_desc=$customer_info['desc_listavta'];
     
#      $customer_saleconditions=$customer_info['cod_convta'];
#      $customer_saleconditions_desc=$customer_info['desc_condvta'];
     

#      //sucursal no lleva VET

    
#     $user_suc_codigo="";

#     //$user_sucursal_desc=$user_sucursal[0]['dat_descripcion'];

#          //Vendedor asignado
    
#          $user_vendedorasignado = DB::table('dbo_veclaa')
#          ->select('dbo_veclaa.cod_vendedor')
#          ->where([
#            ['dbo_veclaa.cod_codigo', '=', $customerid],
#            ])
#          ->get();
    
#          $user_vendedorasignado=json_decode($user_vendedorasignado,true);
#          $user_vendedorasignado=$user_vendedorasignado[0]['cod_vendedor'];
#           //2 veces pido vendedor asignado?
#          //dd($user_vendedorasignado);
  

         
#        //transporte no llevaba VET
#        //cambio a que surge del VECLAA ahora
#         //Vendedor asignado
    
#         $user_transporte = DB::table('dbo_veclaa')
#         ->select('dbo_veclaa.cod_transporte')
#         ->where([
#           ['dbo_veclaa.cod_codigo', '=', $customerid],
#           ])
#         ->get();
   
#         $user_transporte=json_decode($user_transporte,true);
#         $user_transporte=$user_transporte[0]['cod_transporte'];
 
#       //$user_transporte="";
#       //dd($user_transporte);
      


#     ///====CARGA INICIAL=====
#     //trae_empresa();
#     //string queryString = "SELECT COD_CE_EMPRESA,DAT_CE_RAZONSOCIAL ";
#     //queryString += "FROM GZEMAA ";
#     //queryString += "WHERE DAT_VERCAM= 1 ";
#     //permite usar el mismo codigo para distintos clisntes de pedidosweb
#     $pedido_empresapedidosweb = DB::table('dbo_gzemaa')
#     ->select('dbo_gzemaa.cod_ce_empresa','dbo_gzemaa.dat_ce_razonsocial')
#     ->where([
#       ['dbo_gzemaa.dat_vercam', '=', 1],
#       ])
#     ->get();
#     //dd($pedido_empresapedidosweb);
#     $pedido_empresapedidosweb=json_decode($pedido_empresapedidosweb,true);
#     $pedido_empresapedidosweb=$pedido_empresapedidosweb[0]['cod_ce_empresa'];  
#     //dd($pedido_empresapedidosweb);

#     //carga_inicial();

#     ///vendedor ,esto se graba en VEPH
#     // SELECT us.vendedor,ve.dat_nombre ";
#     // FROM usuarios_web us ";
#     // inner join veveaa ve on ve.cod_codigo=us.vendedor and ve.dat_vercam=1 ";
#     // where us.usuario='" + HttpContext.Current.User.Identity.Name + "'";
    
#     //porque le agrega un 0 adelante a lo que trae de la base?
#     // if (Convert.ToString(reader[0]).Length == 1)
#     // {
#     //     vend.Text = "0" + Convert.ToString(reader[0]);
#     // }
#     // else
#     // {
#     //     vend.Text = Convert.ToString(reader[0]);
#     // } 
    
    
#     //comprobante,sucursal,codnro
#     $pedido_comprosucunumer = DB::table('dbo_vecoaa')
#     ->select('dbo_vecoaa.cod_codigo','dbo_vecoaa.dat_descripcion','dbo_vecoaa.cod_su_sucursal','dbo_vecoaa.cod_numeracion',
#     'dbo_gzsuaa.dat_empresa')
#     ->join('dbo_gzsuaa', function ($join) {
#       $join->on('dbo_vecoaa.cod_su_sucursal', '=', 'dbo_gzsuaa.nro_sucursal')
#            ->where([
#              ['dbo_gzsuaa.dat_vercam', '=', 1] 
#            ]);
#        })
#     ->where([
#       ['dbo_vecoaa.dat_vercam', '=', 1],
#       ])
#     ->get();

#     $pedido_comprosucunumer=json_decode($pedido_comprosucunumer,true);
#     //dd($pedido_empresapedidosweb);
#     //dd($pedido_empresapedidosweb[0]['cod_numeracion']);
#     //$pedido_compro=$pedido_comprosucunumer[0]['cod_codigo'];
    
#     $pedido_compro="PWR"; //hardcodeado para SEBASTIAN
    
#     $pedido_suc=$pedido_comprosucunumer[0]['cod_su_sucursal'];  
#     $pedido_codnro=$pedido_comprosucunumer[0]['cod_numeracion'];

#      //SELECT co.cod_codigo,co.dat_descripcion,co.cod_su_sucursal,cod_numeracion,su.dat_empresa 
#     //FROM vecoaa co 
#     //INNER JOIN GZSUAA SU ON CO.COD_SU_SUCURSAL=SU.NRO_SUCURSAL AND SU.DAT_VERCAM=1 
#     //WHERE CO.DAT_VERCAM= 1 

#         // LCOMPRO.Text = Convert.ToString(reader2[0]);
#         // LSUC.Text = Convert.ToString(reader2[2]);
#         // LCODNRO.Text = Convert.ToString(reader2[3]);

#     //proximo_numero();

#     //SELECT dat_proxnroa 
#     //FROM venuaa 
#     //WHERE DAT_VERCAM=1 and cod_codigo='" + LCODNRO.Text + "'"
#     $pedido_proxnro = DB::table('dbo_venuaa')
#     ->select('dbo_venuaa.dat_proxnroa')
#     ->where([
#       ['dbo_venuaa.dat_vercam', '=', 1],
#       ['dbo_venuaa.cod_codigo', '=', $pedido_codnro],
#       ])
#     ->get();
#     $pedido_proxnro=json_decode($pedido_proxnro,true);
#     $pedido_proxnro=$pedido_proxnro[0]['dat_proxnroa'];
    
#     $pedido_proxnro=(int)$pedido_proxnro+1;
#     //dd($pedido_proxnro);

#      //============VEPH==========
    
#     //sucursal drop down
#     //  SELECT [cod_codigo],[dat_descripcion] FROM [vesuaa] WHERE [dat_vercam] =1
#     //  order by [dat_descripcion] asc
#     //cuando elige esto?
#     //cliente con sucursal 160125 tambien tiene descuento
#     // prod con desc 054000718E0050
#     //054000718A0050
#     //05400071800050

#     //Empresa Domicilio de Entrega 
#     $veph_empresa_domentrega = DB::table('dbo_veclaa')
#     ->select('dbo_veclaa.cod_empresa','dbo_vesuaa.dat_domicilio')
#     ->join('dbo_vesuaa','dbo_veclaa.cod_codigo', '=', 'dbo_vesuaa.cod_cliente')
#     ->where([
#       ['dbo_veclaa.dat_vercam', '=', 1],
#       ['dbo_vesuaa.dat_vercam', '=', 1],
#       ['dbo_veclaa.cod_codigo', '=', $customerid],

#       //['dbo_vesuaa.cod_codigo', '=', $user_suc_codigo] //VET no usa sucursal cliente
#       ])
#     ->get();

#     //check if query return no values (empty)
#     if (!$veph_empresa_domentrega->isEmpty())
#     {
#       $veph_empresa_domentrega=json_decode($veph_empresa_domentrega,true);
#       $veph_empresa=$veph_empresa_domentrega[0]['cod_empresa'];
#       $veph_domicilio=$veph_empresa_domentrega[0]['dat_domicilio'];
#       //dd($veph_empresa_domentrega);
#     }
#     else
#     {
#       $veph_empresa="";
#       $veph_domicilio="";
#       //echo ("yeah");
#     }

       

#     //"trae productos y graba"
# // SELECT STPD.COD_PRODUCTO,STPD.DAT_DESCIPCION01,STPD.DAT_RELA12,
# //  STPD.DAT_ESTANTE,STLP.IMP_PRECIO,STPD.COD_FAMILIA ";
# //  FROM stpdaa STPD  

# //   INNER JOIN stlpaa STLP ON STPD.cod_producto = STLP.cod_producto 
# //    and STLP.COD_CODIGO='" + LISTAPRE + "' AND STLP.DAT_VERCAM=1";

# //   WHERE STPD.DAT_VERCAM= 1 
# //   and STLP.cod_codigo ='" + LISTAPRE + "'"
# //   and STPD.dat_actzcompos ='S' "
# // if (TextCODPRO.Text != "")
# // {   and STPD.COD_PRODUCTO like '%" + TextCODPRO.Text + "%'"; }
# // if (TextDESC.Text != "")
# // {   and STPD.dat_descipcion01 like '%" + TextDESC.Text + "%'"; }
# // if (TextCodBar.Text != "")
# // {   and STPD.DAT_ESTANTE like '%" + TextCodBar.Text + "%'"; }
# //   ORDER BY 1 ASC ";


# //Moneda del pedido
# $pedido_moneda = DB::table('dbo_stliaa')
# ->select('dbo_stliaa.cod_moneda')
# ->where([
#   ['dbo_stliaa.cod_codigo', '=', $customer_pricelist],

#   ])
# ->get();
# $pedido_moneda=json_decode($pedido_moneda,true);
# $pedido_moneda=$pedido_moneda[0]['cod_moneda'];

# if ($pedido_moneda==2)
# {
#   $pedido_moneda="DOLAR";
# }
# else
# {
#   $pedido_moneda="PESOS";
# }

# //dd($pedido_moneda);

# //Sucursal activa empresa
# //revisar si no es por tipo de comprobante
# $pedido_sucursalactiva = DB::table('dbo_vecoaa')
# ->select('dbo_vecoaa.cod_su_sucursal')
# ->where([

#   ['dbo_vecoaa.dat_vercam', '=', 1],
  
#   ])
# ->get();
# $pedido_sucursalactiva=json_decode($pedido_sucursalactiva,true);
# $pedido_sucursalactiva=$pedido_sucursalactiva[0]['cod_su_sucursal'];
# //dd($pedido_sucursalactiva);

# //NO hay sucursal en VET

# $pedido_sucursalcli="";
# //dd($pedido_sucursalcli);


# //insert into order table VEPHAA
# DB::table('dbo_vephaa')->insert(
#   ['cod_empresa' =>$pedido_empresapedidosweb,
#   'cod_sucursal' =>$pedido_sucursalactiva, 
#   'cod_cliente' =>$customerid,
#   'cod_succli' =>$pedido_sucursalcli,
#   'cod_comprobante' =>$pedido_compro,
#   'dat_numero' =>$pedido_proxnro,
#   'fec_feccompro' =>$pedido_datetimenow,   
#   'cod_transporte' =>$user_transporte,  
#   'cod_condvta' =>$customer_saleconditions,
#   'dat_observa01' =>$obs1,  //observaciones viene del form previo a esto
#   'dat_observa02' =>$obs2,
#   'dat_observa03' =>$obs3,
#   'dat_observa04' =>$obs4,
#   'dat_observa05' =>$obs5,
#   'dat_forma' =>"WE",  //que es esto?
#   'cod_lista' =>$customer_pricelist,
#   'cod_vendedor' =>$pedido_vendedorasignado, 
#   'fec_entrega' =>$pedido_datetimenow,  
#   'dat_domentrega' =>$veph_domicilio,
#   'cod_traentrega' =>$user_transporte,
#   'dat_ordendecompra' =>$orden_compra, 
#   'dat_moneda' =>$pedido_moneda,  
#   'cod_centrocostos' =>"", //si no esta zonas que ponemos aca?
#   'Sys_fecha' =>$pedido_datetimenow,
#   'Sys_time' =>$pedido_timenow,
#   'Sys_users' =>"PEDIDOSWEBTEST"]  //determinar que va a aca,cliente id?
 
# );
# //echo("\n");
# //echo ("VEPH grabado\n");
# //original query
#   // INSERT INTO VEPHAA 
#   // ([cod_empresa]
#   // ,[cod_sucursal]
#   // ,[cod_cliente]
#   // ,[cod_succli]
#   // ,[cod_comprobante]
#   // ,[dat_numero]
#   // ,[fec_feccompro]
#   // ,[cod_transporte]
#   // ,[cod_condvta]
#   // ,[dat_observa01]
#   // ,[dat_observa02]
#   // ,[dat_observa03]
#   // ,[dat_observa04]
#   // ,[dat_observa05]
#   // ,[dat_forma]
#   // ,[cod_lista]
#   // ,[cod_vendedor]
#   // ,[fec_entrega]
#   // ,[dat_domentrega]
#   // ,[cod_traentrega]
#   // ,[dat_ordendecompra]
#   // ,[dat_moneda]
#   // ,[cod_centrocostos]
#   // ,[Sys_fecha]
#   // ,[Sys_time]
#   // ,[Sys_users])
#     //  VALUES				
#     //  ('" + empresa + "'		
#     //  ,'" + LSUC.Text + "'		
#     //  ,'" + CLIENTE + "'		
 
#  //wtf? sucursal
#   //    if (DropCodCli.SelectedValue == "999")
#   // {
#   //        ,''";
#   // }
#   // else
#   // {
#   //        ,'" + DropCodCli.SelectedValue + "'		";
#   // }
#   //    ,'" + LCOMPRO.Text + "'		";
#   //    ,'" + LPROXNRO.Text + "'		";
#   //    ,'" + FECHA.Text + "'		";
#   //    ,'" + DropTransporte.SelectedValue + "'		";
#   //    ,'" + COND + "'		";
#   //    ,'" + TextObs1.Text + "'		";
#   //    ,'" + TextObs2.Text + "'		";
#   //    ,'" + TextObs3.Text + "'		";
#   //    ,'" + TextObs4.Text + "'		";
#   //    ,'" + TextObs5.Text + "'		";
#   //    ,'WE'		";
#   //    ,'" + LISTA + "'		";
#   //    ,'" + vend.Text + "'		";
#   //    ,'" + FECHA.Text + "'		";
#   //    ,'" + domentrega.Replace("'", "") + "'		";
#   //    ,'" + DropTransporte.SelectedValue + "'		";
#   //    ,'" + TOrdenCompra.Text + "'		";
#   // switch (MONEDA)
#   // {
#   //     case "Pesos Argentinos":
#   //         moneda_desc = "PESOS";
#   //         break;
#   //     case "Dolares Americanos":
#   //         moneda_desc = "DOLAR";
#   //         break;
#   //     case "Real Brasilero":
#   //         moneda_desc = "REAL";
#   //         break;
#   //     case "Euro Unico":
#   //         moneda_desc = "EURO";
#   //         break;
#   //     case "Mercosur Moneda":
#   //         moneda_desc = "MERCO";
#   //         break;

#   // }
#   //    ,'" + moneda_desc + "'		";
#   //    ,'" + DropZona.SelectedValue + "'		"; //que grabamos aca?
#   //    ,'" + FECHA.Text + "'		";
#   //    ,'" + DateTime.Now.ToShortTimeString() + "'		";
#   //    ,'" + HttpContext.Current.User.Identity.Name + "'	    )";


 
# //dd($user_info);



# //==================VEPIAA================================

#     //Empresa Domicilio de Entrega 
#     $empresa_domentrega = DB::table('dbo_veclaa')
#     ->select('dbo_veclaa.cod_empresa','dbo_veclaa.dat_domentrega')
#     ->where([
#       ['dbo_veclaa.dat_vercam', '=', 1],
#       ['dbo_veclaa.cod_codigo', '=', $customerid]

#       ])
#     ->get();

#     //string queryString = "SELECT COD_EMPRESA,DAT_DOMENTREGA ";
#     //queryString += "FROM VECLAA ";
#     //ueryString += "WHERE DAT_VERCAM= 1 ";
#     //queryString += "and cod_codigo='" + CLIENTE + "'";
    
#   $unavariable=json_decode($empresa_domentrega,true);
#   //echo($unavariable[0]['cod_empresa']);
#  //dd($empresa_domentrega);

#  $pedido_empresa=$unavariable[0]['cod_empresa'];
#  $pedido_domentrega=$unavariable[0]['dat_domentrega'];


#  //variables con el total de cada item del pedido

#  $total_cantidad=0;
#  $total_unidades=0;
#  $total_precio=0;
#  $total_desc1=0;
#  $total_desc2=0;
#  $total_importe=0;

#  //loop sobre cada item en el carro de compras
#  //dd($cart_now);

# foreach ($cart_now as $item_carrito) {
#   //echo ($item_carrito['codigo']);
#   //dd($customer_pricelist);

#   $trae_producto = DB::table('dbo_stpdaa')
#   ->select('dbo_stpdaa.cod_producto','dbo_ProductoCat_Web.Descripcion as dat_descipcion01','dbo_stpdaa.dat_rela12',
#   'dbo_stpdaa.dat_estante','dbo_stlpaa.imp_precio','dbo_stpdaa.cod_familia')
#   ->join('dbo_stlpaa', function ($join) use ($customer_pricelist){
#       $join->on('dbo_stpdaa.cod_producto', '=', 'dbo_stlpaa.cod_producto')
#            ->where([
#              ['dbo_stlpaa.cod_codigo','=',$customer_pricelist],
#              //['dbo_stlpaa.dat_vercam', '=', 1] 
#            ]);
#   })
#   ->join('dbo_ProductoCat_Web', 'dbo_ProductoCat_Web.Producto', '=', 'dbo_stpdaa.cod_producto')
#   ->where([
#     //['dbo_stpdaa.dat_vercam', '=', 1],
#     ['dbo_stlpaa.cod_codigo', '=', $customer_pricelist],//LISTAPRE (sale de otro lado)
#     //['dbo_stpdaa.dat_actzcompos', '=', 'S'],
#     //chequear que no llegue null a estas condiciones
#     ['dbo_stpdaa.cod_producto', '=', $item_carrito['codigo']]//EL PRODUCTO QUE ESTOY VIENDO DEL LOOP DEL PEDIDO
    
#     ])
  
#   ->orderBy('dbo_stpdaa.cod_producto', 'asc')
#   //->dd();
#   ->get();

# //familia producto actual  
# $producto_comprado=json_decode($trae_producto,true);
# //dd($producto_comprado);

# $cod_familia=$producto_comprado[0]['cod_familia'];
# $producto_precio=$producto_comprado[0]['imp_precio'];
# //echo($producto_comprado[0]['cod_producto']);
#  //echo($producto_comprado[0]['dat_descipcion01']); 
# //suma al total
# $total_precio=$total_precio+(float)$producto_precio;



#  $descuentos_cliente = DB::table('dbo_vedfaa')
#  ->select('dbo_vedfaa.dat_dtoitem','dbo_vedfaa.dat_dtoadic')
#  ->join('dbo_stpdaa','dbo_stpdaa.cod_familia', '=', 'dbo_vedfaa.cod_familia')
#  ->where([
#    ['dbo_vedfaa.dat_vercam', '=', 1],
#    ['dbo_vedfaa.cod_familia', '=', $cod_familia], //sale de otro query
#    ['dbo_vedfaa.cod_cliente', '=', $customerid]
 
   
#    ])
#  ->get();
#  //dd($descuentos_cliente); 

#  if (!$descuentos_cliente->isEmpty())
#  {
#    $descuento_item=json_decode($descuentos_cliente,true);

#    foreach ($descuento_item as $descuento)
#    {
#      $descuento_item=$descuento['dat_dtoitem'];
#      $descuento_adic=$descuento['dat_dtoadic'];
#      //echo ("hola");
#    }
#    //echo ($descuento_item);
#    //echo ($descuento_adic);
#    //dd();
   
#  }
#  else
#  {
#    //echo ("empty!");
#    $descuento_item=0;
#    $descuento_adic=0;

#  }

#  //suma al total
# $total_desc1=$total_desc1+(float)$descuento_item;
# $total_desc2=$total_desc2+(float)$descuento_adic;
# $total_unidades=$total_unidades+(int)$item_carrito['unidadestotal'];
# $total_cantidad=$total_cantidad+(int)$item_carrito['cantidad'];
# $total_importe=$total_importe+(float)$item_carrito['linea'];

#  //dd();


#  //check if query return no values (empty)

# //  if (!$descuentos_cliente->isEmpty())
# //  {
# //    $descuento_item=json_decode($descuentos_cliente,true);

# //    foreach ($descuento_item as $descuento)
# //    {
# //      $descuento_item=$descuento['dat_dtoitem'];
# //      $descuento_adic=$descuento['dat_dtoadic'];
# //      //echo ("hola");
# //    }
# //    //echo ($descuento_item);
# //    //echo ($descuento_adic);
# //    //dd();
   
# //  }
# //  else
# //  {
# //    //echo ("empty!");
# //    $descuento_item=0;
# //    $descuento_adic=0;

# //  }

#  //dd();

# //  if (!$descuentos_cliente->isEmpty())
# //  {
# //     $descuento_item=json_decode($descuentos_cliente,true);
# //     $descuento_item=$descuento_item[0]['dat_dtoitem'];
# //     $descuento_adic=$descuento_item[0]['dat_dtoadic'];
# //     //dd($descuento_item);
# //  }
# //  else
# //  {
# //     $descuento_item=0;
# //     $descuento_adic=0;

# //  }
#  //clientes c/descuento 
#  //vedfaa
# //0010005 
 
 
#  //descuento x cliente
#  // SELECT VEDF.dat_dtoitem,VEDF.dat_dtoadic 
#  //   FROM VEDFAA VEDF 
#  //    INNER JOIN STPDAA STPD ON STPD.cod_familia = VEDF.cod_familia
#  //    WHERE VEDF.DAT_VERCAM= 1 
#  //    and VEDF.cod_familia ='" + Convert.ToString(reader[5]) + "'
#  //    and VEDF.cod_cliente ='" + CLIENTE + "'"
 
 
#      //devolver json decode con array session a vista
#      //return view('products.cart')->with('elproductocomprado', $elproductocomprado);
 
#   ///trae del temporal 
#   //reemplazar con sesion o incorporar tambien?
#   // SELECT T.CODIGO,T.CANTIDAD,T.PRECIO,PD.COD_FAMILIA,
#   //T.FECHA_ENTREGA,T.CANTIDAD2,T.DESCUENTO1,T.DESCUENTO2,T.OBSERVACION "
#   //       FROM TEMP T ";
#   //        INNER JOIN STPDAA PD ON T.CODIGO=PD.COD_PRODUCTO AND PD.DAT_VERCAM=1 ";
#   //       where T.usuario='" + HttpContext.Current.User.Identity.Name + "'";
#   //      and T.cliente='" + CLIENTE + "'";
#   //     ORDER BY T.ITEM ASC";
 
#  DB::table('dbo_vepiaa')->insert(
#   ['cod_empresa' =>$pedido_empresa,
#   'cod_sucursal' =>$pedido_sucursalactiva,
#   'cod_cliente' =>$customerid,
#   'cod_succli' =>$pedido_sucursalcli,
#   'cod_comprobante' =>$pedido_compro,
#   'dat_numero' =>$pedido_proxnro,
#   'fec_feccompro' =>$pedido_datetimenow,
#   'cod_producto' =>$producto_comprado[0]['cod_producto'],
#   'cod_familia' =>$producto_comprado[0]['cod_familia'],//??
#   'fec_feclimite' =>$pedido_datetimenow, 
#   'dat_cantid01' =>$item_carrito['unidadestotal'],  //cantxbulto * bultos
#   'dat_cantid02' =>$item_carrito['cantidad'], //bultos
#   'dat_precio' =>$producto_precio, 
#   'dat_descto' =>$descuento_item,
#   'dat_desctoadi' =>$descuento_adic,
#   'dat_nivelurg' =>"A",  //Esto es el tipo dejo A o que va?
#   'cod_centrocostos' =>"",//si no esta zonas que ponemos aca?
#   'dat_obsart1' =>"",//va algo aca?
#   'imp_paripeso'=>"1",//   ,1		"; ??
#   'Sys_fecha' =>$pedido_datetimenow,
#   'Sys_time' =>$pedido_timenow,
#   'Sys_users' =>"PEDIDOSWEBTEST"]
 
# ); 

# //echo("\n");
# //echo ("VEPI grabado\n");
#   //  ,'" + LCOMPRO.Text + "'";
#   //                  ," + LPROXNRO.Text + "	";
#   //                  ,'" + FECHA.Text + "'	";
#   //                  ,'" + Convert.ToString(reader[0]) + "'		";
#   //                  ,'" + Convert.ToString(reader[3]) + "'		";
#   //                  ,'" + Convert.ToDateTime(reader[4]).ToShortDateString() + "'	";
#   //                  ," + Convert.ToString(reader[1]).Replace(",", ".") + "		";
#   //                  ," + Convert.ToString(reader[5]).Replace(",", ".") + "		";
#   //                  ," + Convert.ToString(reader[2]).Replace(",", ".") + "		";
#   //                  ," + Convert.ToString(reader[6]).Replace(",", ".") + "		";
#   //                  ," + Convert.ToString(reader[7]).Replace(",", ".") + "		";
#   //                  ,'" + TIPO.Text + "'		";
#   //                  ,'" + LZONA.Text + "'		";
#   //                  ,'" + Convert.ToString(reader[8]) + "'		";
#   //                  ,1		";
#   //                  ,'" + FECHA.Text + "'		";
#   //                  ,'" + DateTime.Now.ToShortTimeString() + "'		";
#   //                  ,'" + HttpContext.Current.User.Identity.Name + "'	    )";
 

# }
# //dd($cod_familia);



# // INSERT INTO VEPIAA";
# //                 ([cod_empresa]";
# //                 ,[cod_sucursal]";
# //                 ,[cod_cliente]";
# //                 ,[cod_succli]";
# //                 ,[cod_comprobante]";
# //                 ,[dat_numero]";
# //                 ,[fec_feccompro]";
# //                 ,[cod_producto]";
# //                 ,[cod_familia]";
# //                 ,[fec_feclimite]";
# //                 ,[dat_cantid01]";
# //                 ,[dat_cantid02]";
# //                 ,[dat_precio]";
# //                 ,[dat_descto]";
# //                 ,[dat_desctoadi]";
# //                 ,[dat_nivelurg]";
# //                 ,[cod_centrocostos]";
# //                 ,[dat_obsart1]";
# //                 ,[imp_paripeso]";
# //                 ,[Sys_fecha]";
# //                 ,[Sys_time]";
# //                 ,[Sys_users])";
# //                    VALUES				";
# //                    ('" + empresa + "'		";
# //                  LSUC.Text + "'		";
# //                  CLIENTE + "'		";
# //                 if (DropCodCli.SelectedValue == "999")
# //                 {
# //                        ,''";
# //                 }
# //                 else
# //                 {
# //                      DropCodCli.SelectedValue + "'		";
# //                 }
# //                  LCOMPRO.Text + "'";
# //                  LPROXNRO.Text + "	";
# //                  FECHA.Text + "'	";
# //                  Convert.ToString(reader[0]) + "'		";
# //                  Convert.ToString(reader[3]) + "'		";
# //                  Convert.ToDateTime(reader[4]).ToShortDateString() + "'	";
# //                  Convert.ToString(reader[1]).Replace(",", ".") + "		";
# //                  Convert.ToString(reader[5]).Replace(",", ".") + "		";
# //                  Convert.ToString(reader[2]).Replace(",", ".") + "		";
# //                  Convert.ToString(reader[6]).Replace(",", ".") + "		";
# //                  Convert.ToString(reader[7]).Replace(",", ".") + "		";
# //                  TIPO.Text + "'		";
# //                  LZONA.Text + "'		";
# //                  Convert.ToString(reader[8]) + "'		";
# //                    ,1		";
# //                  FECHA.Text + "'		";
# //                  DateTime.Now.ToShortTimeString() + "'		";
# //                  HttpContext.Current.User.Identity.Name + "'	    )";

# //view

# //dd($customer_info);


# //update last order number
# $mover_proxnro = DB::table('dbo_venuaa')
# ->update(
#   ['dbo_venuaa.dat_proxnroa'=>$pedido_proxnro]);

# //create array of parameters to create PDF
# $pdf_vars= array('customer_info', 'pedido_compro','customer_pricelist',
# 'customer_pricelist_desc',
# 'customer_saleconditions',
# 'customer_saleconditions_desc',
# 'pedido_vendedorasignado',
# 'pedido_sucursalcli',
# 'pedido_sucursalactiva',
# 'customerid',
# 'pedido_proxnro',
# 'transp_clienterq',
# 'obs1',
# 'obs2',
# 'obs3',
# 'obs4',
# 'obs5',
# 'pedido_datetimenow',
# 'pedido_timenow',
# 'total_cantidad',
# 'total_unidades',
# 'total_precio',
# 'total_desc1',
# 'total_desc2',
# 'total_importe',
# 'cart_now');



# //aux variable
# $test="testpdf";
# //one variable has all the parameters
# $result = compact("test", $pdf_vars);

# //call blade view with parameters
# //$pdf = PDF::loadView('invoicepdf',$result);

# //download PDF
# //return $pdf->download('pedido.pdf');

# //$pdf = App::make('dompdf.wrapper');
# //$pdf->loadHTML('<h1>Testo!</h1>');
# //return $pdf->stream();
# //dd($pedido_proxnro);

# return view('invoice')->with('customer_info',$customer_info)
#                          ->with('pedido_compro',$pedido_compro)

#                         //desc_vendedor que tabla?
#                          //descuento por condicion? //de donde sale?
#                         ->with('customer_pricelist',$customer_pricelist)
#                         ->with('customer_pricelist_desc',$customer_pricelist_desc)
#                         ->with('customer_saleconditions',$customer_saleconditions)
#                         ->with('customer_saleconditions_desc',$customer_saleconditions_desc)
#                         ->with('cart_now',$cart_now)
#                         ->with('pedido_vendedorasignado',$pedido_vendedorasignado)
#                         ->with('pedido_sucursalcli',$suc_clienterq)
#                         ->with('pedido_sucursalactiva',$pedido_sucursalactiva)
#                         ->with('customerid',$customerid)
#                         ->with('pedido_proxnro',$pedido_proxnro)
#                         ->with('transp_clienterq',$transp_clienterq)
#                         ->with('obs1',$obs1)
#                         ->with('obs2',$obs2)
#                         ->with('obs3',$obs3)
#                         ->with('obs4',$obs4)
#                         ->with('obs5',$obs5)
#                         ->with('pedido_datetimenow',$pedido_datetimenow)
#                         ->with('pedido_timenow',$pedido_timenow)
#                         //totales
#                         ->with('total_cantidad',$total_cantidad)
#                         ->with('total_unidades',$total_unidades)
#                         ->with('total_precio',$total_precio)
#                         ->with('total_desc1',$total_desc1)
#                         ->with('total_desc2',$total_desc2)
#                         ->with('total_importe',$total_importe);
                        






   
#   }
