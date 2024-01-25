# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DboCategoriasWeb(models.Model):
    idcategoria = models.TextField(db_column='IdCategoria', blank=True,primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    descripcioncorta = models.TextField(db_column='DescripcionCorta', blank=True, null=True)  # Field name made lowercase.
    nivel = models.TextField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    idcategoriaagrupa = models.TextField(db_column='IdCategoriaAgrupa', blank=True, null=True)  # Field name made lowercase.
    categoriaagrupa = models.TextField(db_column='CategoriaAgrupa', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    activo = models.TextField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dbo_categorias_web'


class DboCategoriasWebOldGood(models.Model):
    idcategoria = models.TextField(db_column='IdCategoria', blank=True,primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    descripcioncorta = models.TextField(db_column='DescripcionCorta', blank=True, null=True)  # Field name made lowercase.
    nivel = models.TextField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    idcategoriaagrupa = models.TextField(db_column='IdCategoriaAgrupa', blank=True, null=True)  # Field name made lowercase.
    categoriaagrupa = models.TextField(db_column='CategoriaAgrupa', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    activo = models.TextField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dbo_categorias_web_old_good'


class DboGrupoMenuWeb(models.Model):
    idgrupo = models.IntegerField(primary_key=True)
    idmenu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dbo_grupo_menu_web'


class DboGrupos(models.Model):
    idgrupo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    idmenu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_grupos'


class DboGruposWeb(models.Model):
    idgrupo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    idmenu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_grupos_web'


class DboGzemaa(models.Model):
    nro_interno = models.IntegerField(blank=True,primary_key=True)
    memo = models.TextField(blank=True, null=True)
    cod_ce_empresa = models.CharField(max_length=4, blank=True, null=True)
    dat_ce_razonsocial = models.CharField(max_length=40, blank=True, null=True)
    dat_ce_cuit = models.CharField(max_length=11, blank=True, null=True)
    dat_ce_domicilio = models.CharField(max_length=40, blank=True, null=True)
    dat_ce_localidad = models.CharField(max_length=40, blank=True, null=True)
    dat_ce_ingbru = models.CharField(max_length=20, blank=True, null=True)
    dat_ce_codiva = models.CharField(max_length=6, blank=True, null=True)
    dat_ce_telefonoi = models.CharField(max_length=40, blank=True, null=True)
    dat_ce_telefonoii = models.CharField(max_length=40, blank=True, null=True)
    dat_ce_telefonoiii = models.CharField(max_length=40, blank=True, null=True)
    dat_ce_fax = models.CharField(max_length=40, blank=True, null=True)
    dat_ce_email = models.CharField(max_length=50, blank=True, null=True)
    dat_ce_respon = models.CharField(max_length=50, blank=True, null=True)
    dat_ce_terespon = models.CharField(max_length=40, blank=True, null=True)
    dat_ce_actividad = models.CharField(max_length=50, blank=True, null=True)
    dat_ce_codpos = models.CharField(max_length=6, blank=True, null=True)
    dat_ce_pais = models.CharField(max_length=20, blank=True, null=True)
    dat_ce_observai = models.CharField(max_length=50, blank=True, null=True)
    dat_ce_observaii = models.CharField(max_length=50, blank=True, null=True)
    dat_ce_observaiii = models.CharField(max_length=50, blank=True, null=True)
    dat_ce_observaiv = models.CharField(max_length=50, blank=True, null=True)
    dat_ce_observav = models.CharField(max_length=50, blank=True, null=True)
    cod_comprofcc = models.CharField(max_length=7, blank=True, null=True)
    cod_comprofcd = models.CharField(max_length=7, blank=True, null=True)
    cod_comproopa = models.CharField(max_length=7, blank=True, null=True)
    dat_stlong01 = models.IntegerField(blank=True, null=True)
    dat_stcara01 = models.CharField(max_length=1, blank=True, null=True)
    dat_stlong02 = models.IntegerField(blank=True, null=True)
    dat_stcara02 = models.CharField(max_length=1, blank=True, null=True)
    dat_stlong03 = models.IntegerField(blank=True, null=True)
    dat_desele = models.CharField(max_length=20, blank=True, null=True)
    dat_despac = models.CharField(max_length=20, blank=True, null=True)
    dat_despes = models.CharField(max_length=20, blank=True, null=True)
    dat_desvol = models.CharField(max_length=20, blank=True, null=True)
    dat_decsto = models.IntegerField(blank=True, null=True)
    dat_impres = models.CharField(max_length=2, blank=True, null=True)
    dat_lineas = models.IntegerField(blank=True, null=True)
    dat_servweb = models.CharField(max_length=50, blank=True, null=True)
    dat_habweb = models.CharField(max_length=1, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_gzemaa'


class DboGzsuaa(models.Model):
    nro_interno = models.IntegerField(blank=True,primary_key=True)
    memo = models.TextField(blank=True, null=True)
    nro_sucursal = models.CharField(max_length=4, blank=True, null=True)
    dat_empresa = models.CharField(max_length=40, blank=True, null=True)
    dat_domicilio = models.CharField(max_length=45, blank=True, null=True)
    dat_localidad = models.CharField(max_length=30, blank=True, null=True)
    dat_codpostal = models.CharField(max_length=10, blank=True, null=True)
    dat_pais = models.CharField(max_length=20, blank=True, null=True)
    dat_telefono = models.CharField(max_length=30, blank=True, null=True)
    nro_ultnroint = models.IntegerField(blank=True, null=True)
    dat_npriva = models.IntegerField(blank=True, null=True)
    dat_nprgan = models.IntegerField(blank=True, null=True)
    dat_npribr = models.IntegerField(blank=True, null=True)
    dat_mribru = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cod_cnivag = models.CharField(max_length=7, blank=True, null=True)
    cod_cnivad = models.CharField(max_length=7, blank=True, null=True)
    cod_cnriva = models.CharField(max_length=7, blank=True, null=True)
    cod_cribru = models.CharField(max_length=7, blank=True, null=True)
    dat_su_observai = models.CharField(max_length=50, blank=True, null=True)
    dat_su_observaii = models.CharField(max_length=50, blank=True, null=True)
    dat_su_observaiii = models.CharField(max_length=50, blank=True, null=True)
    dat_su_observaiv = models.CharField(max_length=50, blank=True, null=True)
    dat_su_observav = models.CharField(max_length=50, blank=True, null=True)
    cod_su_moneda = models.CharField(max_length=4, blank=True, null=True)
    cod_ce_empresa = models.CharField(max_length=4, blank=True, null=True)
    fec_fechacierre = models.DateTimeField(blank=True, null=True)
    dat_stokneg = models.CharField(max_length=1, blank=True, null=True)
    dat_export = models.CharField(max_length=1, blank=True, null=True)
    dat_perciva = models.CharField(max_length=1, blank=True, null=True)
    dat_percib = models.CharField(max_length=1, blank=True, null=True)
    dat_retgan = models.CharField(max_length=1, blank=True, null=True)
    dat_retib = models.CharField(max_length=1, blank=True, null=True)
    dat_retiva = models.CharField(max_length=1, blank=True, null=True)
    dat_retsuss = models.CharField(max_length=1, blank=True, null=True)
    dat_nprsuss = models.IntegerField(blank=True, null=True)
    cod_provhab = models.CharField(max_length=6, blank=True, null=True)
    dat_autorizaoc = models.CharField(max_length=1, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_gzsuaa'


class DboMenuWeb(models.Model):
    idmenu = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    idhead = models.IntegerField(blank=True, null=True)
    posicion = models.IntegerField(blank=True, null=True)
    icono = models.CharField(max_length=50, blank=True, null=True)
    habilitado = models.PositiveIntegerField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_menu_web'


class DboPedidoroyalWeb(models.Model):
    pr_id = models.AutoField(db_column='PR_Id', primary_key=True)  # Field name made lowercase.
    codigo = models.TextField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    faltante = models.TextField(db_column='Faltante', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.TextField(db_column='Habilitado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dbo_pedidoroyal_web'


class DboProductocatWeb(models.Model):
    pc_id = models.BigIntegerField(db_column='PC_Id', blank=True,primary_key=True)  # Field name made lowercase.
    producto = models.TextField(db_column='Producto', blank=True, null=True)  # Field name made lowercase.
    categoria = models.FloatField(db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    descripcioncorta = models.TextField(db_column='DescripcionCorta', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    activo = models.TextField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dbo_productocat_web'


class DboProductocatWebOldGood(models.Model):
    pc_id = models.BigIntegerField(db_column='PC_Id', blank=True,primary_key=True)  # Field name made lowercase.
    producto = models.TextField(db_column='Producto', blank=True, null=True)  # Field name made lowercase.
    categoria = models.BigIntegerField(db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    descripcioncorta = models.TextField(db_column='DescripcionCorta', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    activo = models.TextField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dbo_productocat_web_old_good'


class DboRespuesta(models.Model):
    c01 = models.CharField(max_length=41, blank=True, null=True)
    c02 = models.CharField(max_length=41, blank=True, null=True)
    c03 = models.CharField(max_length=41, blank=True, null=True)
    c04 = models.CharField(max_length=41, blank=True, null=True)
    c05 = models.CharField(max_length=41, blank=True, null=True)
    c06 = models.CharField(max_length=41, blank=True, null=True)
    c07 = models.CharField(max_length=41, blank=True, null=True)
    c08 = models.CharField(max_length=41, blank=True, null=True)
    c09 = models.CharField(max_length=41, blank=True, null=True)
    c10 = models.CharField(max_length=41, blank=True, null=True)
    c11 = models.CharField(max_length=41, blank=True, null=True)
    c12 = models.CharField(max_length=41, blank=True, null=True)
    c13 = models.CharField(max_length=41, blank=True, null=True)
    c14 = models.CharField(max_length=41, blank=True, null=True)
    c15 = models.CharField(max_length=41, blank=True, null=True)
    c16 = models.CharField(max_length=41, blank=True, null=True)
    c17 = models.CharField(max_length=41, blank=True, null=True)
    c18 = models.CharField(max_length=41, blank=True, null=True)
    c19 = models.CharField(max_length=41, blank=True, null=True)
    c20 = models.CharField(max_length=41, blank=True, null=True)
    c21 = models.CharField(max_length=41, blank=True, null=True)
    c22 = models.CharField(max_length=41, blank=True, null=True)
    c23 = models.CharField(max_length=41, blank=True, null=True)
    c24 = models.CharField(max_length=41, blank=True, null=True)
    c25 = models.CharField(max_length=41, blank=True, null=True)
    c26 = models.CharField(max_length=41, blank=True, null=True)
    c27 = models.CharField(max_length=41, blank=True, null=True)
    c28 = models.CharField(max_length=41, blank=True, null=True)
    c29 = models.CharField(max_length=41, blank=True, null=True)
    c30 = models.CharField(max_length=41, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_respuesta'


class DboRespuesta2(models.Model):
    c01 = models.CharField(max_length=41, blank=True, null=True)
    c02 = models.CharField(max_length=41, blank=True, null=True)
    c03 = models.CharField(max_length=41, blank=True, null=True)
    c04 = models.CharField(max_length=41, blank=True, null=True)
    c05 = models.CharField(max_length=41, blank=True, null=True)
    c06 = models.CharField(max_length=41, blank=True, null=True)
    c07 = models.CharField(max_length=41, blank=True, null=True)
    c08 = models.CharField(max_length=41, blank=True, null=True)
    c09 = models.CharField(max_length=41, blank=True, null=True)
    c10 = models.CharField(max_length=41, blank=True, null=True)
    c11 = models.CharField(max_length=41, blank=True, null=True)
    c12 = models.CharField(max_length=41, blank=True, null=True)
    c13 = models.CharField(max_length=41, blank=True, null=True)
    c14 = models.CharField(max_length=41, blank=True, null=True)
    c15 = models.CharField(max_length=41, blank=True, null=True)
    c16 = models.CharField(max_length=41, blank=True, null=True)
    c17 = models.CharField(max_length=41, blank=True, null=True)
    c18 = models.CharField(max_length=41, blank=True, null=True)
    c19 = models.CharField(max_length=41, blank=True, null=True)
    c20 = models.CharField(max_length=41, blank=True, null=True)
    c21 = models.CharField(max_length=41, blank=True, null=True)
    c22 = models.CharField(max_length=41, blank=True, null=True)
    c23 = models.CharField(max_length=41, blank=True, null=True)
    c24 = models.CharField(max_length=41, blank=True, null=True)
    c25 = models.CharField(max_length=41, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_respuesta2'


class DboRespuestan(models.Model):
    c01 = models.CharField(max_length=41, blank=True, null=True)
    c02 = models.CharField(max_length=41, blank=True, null=True)
    c03 = models.CharField(max_length=41, blank=True, null=True)
    c04 = models.CharField(max_length=41, blank=True, null=True)
    c05 = models.CharField(max_length=41, blank=True, null=True)
    c06 = models.CharField(max_length=41, blank=True, null=True)
    c07 = models.CharField(max_length=41, blank=True, null=True)
    c08 = models.CharField(max_length=41, blank=True, null=True)
    c09 = models.CharField(max_length=41, blank=True, null=True)
    c10 = models.CharField(max_length=41, blank=True, null=True)
    c11 = models.CharField(max_length=41, blank=True, null=True)
    c12 = models.CharField(max_length=41, blank=True, null=True)
    c13 = models.CharField(max_length=41, blank=True, null=True)
    c14 = models.CharField(max_length=41, blank=True, null=True)
    c15 = models.CharField(max_length=41, blank=True, null=True)
    c16 = models.CharField(max_length=41, blank=True, null=True)
    c17 = models.CharField(max_length=41, blank=True, null=True)
    c18 = models.CharField(max_length=41, blank=True, null=True)
    c19 = models.CharField(max_length=41, blank=True, null=True)
    c20 = models.CharField(max_length=41, blank=True, null=True)
    c21 = models.CharField(max_length=41, blank=True, null=True)
    c22 = models.CharField(max_length=41, blank=True, null=True)
    c23 = models.CharField(max_length=41, blank=True, null=True)
    c24 = models.CharField(max_length=41, blank=True, null=True)
    c25 = models.CharField(max_length=41, blank=True, null=True)
    c26 = models.CharField(max_length=41, blank=True, null=True)
    c27 = models.CharField(max_length=41, blank=True, null=True)
    c28 = models.CharField(max_length=41, blank=True, null=True)
    c29 = models.CharField(max_length=41, blank=True, null=True)
    c30 = models.CharField(max_length=41, blank=True, null=True)
    c31 = models.CharField(max_length=41, blank=True, null=True)
    c32 = models.CharField(max_length=41, blank=True, null=True)
    c33 = models.CharField(max_length=41, blank=True, null=True)
    c34 = models.CharField(max_length=41, blank=True, null=True)
    c35 = models.CharField(max_length=41, blank=True, null=True)
    c36 = models.CharField(max_length=41, blank=True, null=True)
    c37 = models.CharField(max_length=41, blank=True, null=True)
    c38 = models.CharField(max_length=41, blank=True, null=True)
    c39 = models.CharField(max_length=41, blank=True, null=True)
    c40 = models.CharField(max_length=41, blank=True, null=True)
    c41 = models.CharField(max_length=41, blank=True, null=True)
    c42 = models.CharField(max_length=41, blank=True, null=True)
    c43 = models.CharField(max_length=41, blank=True, null=True)
    c44 = models.CharField(max_length=41, blank=True, null=True)
    c45 = models.CharField(max_length=41, blank=True, null=True)
    c46 = models.CharField(max_length=41, blank=True, null=True)
    c47 = models.CharField(max_length=41, blank=True, null=True)
    c48 = models.CharField(max_length=41, blank=True, null=True)
    c49 = models.CharField(max_length=41, blank=True, null=True)
    c50 = models.CharField(max_length=41, blank=True, null=True)
    c51 = models.CharField(max_length=41, blank=True, null=True)
    c52 = models.CharField(max_length=41, blank=True, null=True)
    c53 = models.CharField(max_length=41, blank=True, null=True)
    c54 = models.CharField(max_length=41, blank=True, null=True)
    c55 = models.CharField(max_length=41, blank=True, null=True)
    c56 = models.CharField(max_length=41, blank=True, null=True)
    c57 = models.CharField(max_length=41, blank=True, null=True)
    c58 = models.CharField(max_length=41, blank=True, null=True)
    c59 = models.CharField(max_length=41, blank=True, null=True)
    c60 = models.CharField(max_length=41, blank=True, null=True)
    c61 = models.CharField(max_length=41, blank=True, null=True)
    c62 = models.CharField(max_length=41, blank=True, null=True)
    c63 = models.CharField(max_length=41, blank=True, null=True)
    c64 = models.CharField(max_length=41, blank=True, null=True)
    c65 = models.CharField(max_length=41, blank=True, null=True)
    c66 = models.CharField(max_length=41, blank=True, null=True)
    c67 = models.CharField(max_length=41, blank=True, null=True)
    c68 = models.CharField(max_length=41, blank=True, null=True)
    c69 = models.CharField(max_length=41, blank=True, null=True)
    c70 = models.CharField(max_length=41, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_respuestan'


class DboStfaaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=8, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=40, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_stfaaa'


class DboStliaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(unique=True, blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=7, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=40, blank=True, null=True)
    cod_moneda = models.IntegerField(blank=True, null=True)
    dat_titulopr01 = models.CharField(max_length=15, blank=True, null=True)
    dat_titulose01 = models.CharField(max_length=15, blank=True, null=True)
    cod_lista01 = models.CharField(max_length=7, blank=True, null=True)
    dat_titulopr02 = models.CharField(max_length=15, blank=True, null=True)
    dat_titulose02 = models.CharField(max_length=15, blank=True, null=True)
    cod_lista02 = models.CharField(max_length=7, blank=True, null=True)
    dat_titulopr03 = models.CharField(max_length=15, blank=True, null=True)
    dat_titulose03 = models.CharField(max_length=15, blank=True, null=True)
    cod_lista03 = models.CharField(max_length=7, blank=True, null=True)
    dat_titulopr04 = models.CharField(max_length=15, blank=True, null=True)
    dat_titulose04 = models.CharField(max_length=15, blank=True, null=True)
    cod_lista04 = models.CharField(max_length=7, blank=True, null=True)
    dat_iva = models.CharField(max_length=1, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_stliaa'


class DboStlpaa(models.Model):
    idlista = models.AutoField(primary_key=True)
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(unique=True, blank=True, null=True)
    cod_codigo = models.CharField(max_length=7, blank=True, null=True)
    cod_producto = models.CharField(max_length=15, blank=True, null=True)
    dat_fechalista = models.DateTimeField(blank=True, null=True)
    imp_precio = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_stlpaa'


class DboStmaaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_productomad = models.CharField(max_length=15, blank=True, null=True)
    cod_productohij = models.CharField(max_length=15, blank=True, null=True)
    dat_cantid01 = models.DecimalField(max_digits=15, decimal_places=8, blank=True, null=True)
    dat_cantid02 = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_coefi = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    cod_codigo = models.CharField(max_length=3, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_stmaaa'


class DboStpdaa(models.Model):
    idproducto = models.AutoField(primary_key=True)
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(unique=True, blank=True, null=True)
    cod_producto = models.CharField(max_length=15, blank=True, null=True)
    dat_descipcion01 = models.CharField(max_length=40, blank=True, null=True)
    dat_descripcion02 = models.CharField(max_length=80, blank=True, null=True)
    cod_familia = models.CharField(max_length=8, blank=True, null=True)
    cod_tipopro = models.CharField(max_length=4, blank=True, null=True)
    cod_concepto = models.CharField(max_length=7, blank=True, null=True)
    cod_conceppr = models.CharField(max_length=7, blank=True, null=True)
    dat_llevast = models.CharField(max_length=1, blank=True, null=True)
    dat_nroserie = models.CharField(max_length=1, blank=True, null=True)
    dat_imagen = models.CharField(max_length=250, blank=True, null=True)
    dat_fecultcpa = models.DateTimeField(blank=True, null=True)
    dat_ultprov = models.CharField(max_length=6, blank=True, null=True)
    dat_ultcosto = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_costorep = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_costocompra = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_porutil = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    dat_porbonif = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    dat_stminimo = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_stmaximo = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    cod_unimedsto1 = models.CharField(max_length=4, blank=True, null=True)
    cod_unimedcom1 = models.CharField(max_length=4, blank=True, null=True)
    cod_unimedfac1 = models.CharField(max_length=4, blank=True, null=True)
    dat_faccomsto1 = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    dat_facstofac1 = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    cod_unimedsto2 = models.CharField(max_length=4, blank=True, null=True)
    cod_unimedcom2 = models.CharField(max_length=4, blank=True, null=True)
    cod_unimedfac2 = models.CharField(max_length=4, blank=True, null=True)
    dat_faccomsto2 = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    dat_facstofac2 = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    dat_actzcompos = models.CharField(max_length=1, blank=True, null=True)
    dat_ubicacion = models.CharField(max_length=20, blank=True, null=True)
    dat_pasillo = models.CharField(max_length=20, blank=True, null=True)
    dat_estante = models.CharField(max_length=20, blank=True, null=True)
    dat_habilitado = models.CharField(max_length=1, blank=True, null=True)
    dat_superfi = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    dat_rela12 = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    dat_ancho = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    dat_largo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    dat_peso = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    dat_costosim = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_monedacosto = models.CharField(max_length=2, blank=True, null=True)
    dat_monedaventa = models.CharField(max_length=2, blank=True, null=True)
    dat_sisven = models.CharField(max_length=1, blank=True, null=True)
    dat_siscom = models.CharField(max_length=1, blank=True, null=True)
    dat_sissto = models.CharField(max_length=1, blank=True, null=True)
    dat_sispro = models.CharField(max_length=1, blank=True, null=True)
    dat_sispto = models.CharField(max_length=1, blank=True, null=True)
    cod_tarea = models.CharField(max_length=15, blank=True, null=True)
    dat_concal = models.CharField(max_length=1, blank=True, null=True)
    dat_gramaje01 = models.IntegerField(blank=True, null=True)
    dat_gramaje02 = models.IntegerField(blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_stpdaa'


class DboStseaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=7, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=40, blank=True, null=True)
    cod_producto = models.CharField(max_length=15, blank=True, null=True)
    dat_fecha = models.DateTimeField(blank=True, null=True)
    dat_observa01 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa02 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa03 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa04 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa05 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa06 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa07 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa08 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa09 = models.CharField(max_length=40, blank=True, null=True)
    dat_observa10 = models.CharField(max_length=40, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_stseaa'


class DboSttpaa(models.Model):
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    memo = models.TextField(blank=True, null=True)
    cod_codigo = models.CharField(max_length=4, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=40, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_sttpaa'


class DboStumaa(models.Model):
    memo = models.TextField(blank=True,primary_key=True)
    nro_serie = models.IntegerField(blank=True, null=True)
    cod_codigo = models.CharField(max_length=4, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=40, blank=True, null=True)
    dat_elementos = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_peso = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_volumen = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_pack = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_stumaa'


class DboTemp(models.Model):
    item = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    observacion = models.CharField(max_length=40, blank=True, null=True)
    superficie = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    cantidad = models.CharField(max_length=15, blank=True, null=True)
    cantidad2 = models.CharField(max_length=15, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    descuento1 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    descuento2 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    cliente = models.CharField(max_length=6, blank=True, null=True)
    obs1 = models.CharField(max_length=250, blank=True, null=True)
    obs2 = models.CharField(max_length=50, blank=True, null=True)
    obs3 = models.CharField(max_length=50, blank=True, null=True)
    obs4 = models.CharField(max_length=50, blank=True, null=True)
    obs5 = models.CharField(max_length=50, blank=True, null=True)
    sys_fecha = models.DateField(blank=True, null=True)
    sys_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_temp'


class DboTempPedidos(models.Model):
    item = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    observacion = models.CharField(max_length=40, blank=True, null=True)
    superficie = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    cantidad = models.CharField(max_length=15, blank=True, null=True)
    cantidad2 = models.CharField(max_length=15, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    descuento1 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    descuento2 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    cliente = models.CharField(max_length=6, blank=True, null=True)
    sys_fecha = models.DateField(blank=True, null=True)
    sys_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_temp_pedidos'


class DboTmpGraficos(models.Model):
    sessionid = models.CharField(max_length=50, blank=True, null=True)
    tipografico = models.CharField(max_length=50, blank=True, null=True)
    jsonstring = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_tmp_graficos'


class DboUsuariosWeb(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    idgrupo = models.IntegerField(blank=True, null=True)
    habilitado = models.PositiveIntegerField(blank=True, null=True)
    mail = models.CharField(max_length=500, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    vendedor = models.IntegerField()
    cliente = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_usuarios_web'


class DboUsuariosWebPerfil(models.Model):
    idusuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    idgrupo = models.IntegerField(blank=True, null=True)
    habilitado = models.PositiveIntegerField(blank=True, null=True)
    mail = models.CharField(max_length=500, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    vendedor = models.IntegerField()
    cliente = models.CharField(max_length=6, blank=True, null=True)
    perfil = models.CharField(max_length=100, blank=True, null=True)
    lista_precio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'dbo_usuarios_web_perfil'


class DboVeccaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=7, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=40, blank=True, null=True)
    dat_tipcon = models.CharField(max_length=3, blank=True, null=True)
    cod_conigr = models.CharField(max_length=7, blank=True, null=True)
    cod_coniso = models.CharField(max_length=7, blank=True, null=True)
    cod_coniin = models.CharField(max_length=7, blank=True, null=True)
    dat_colsui = models.IntegerField(blank=True, null=True)
    dat_colsuc = models.IntegerField(blank=True, null=True)
    dat_tasa1 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    dat_minimponible = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    cod_conexp = models.CharField(max_length=7, blank=True, null=True)
    nro_imputacontable = models.CharField(max_length=15, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_veccaa'


class DboVeclaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(unique=True, blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=6, blank=True, null=True)
    dat_razonsocial = models.CharField(max_length=40, blank=True, null=True)
    dat_domicilio = models.CharField(max_length=40, blank=True, null=True)
    dat_localidad = models.CharField(max_length=35, blank=True, null=True)
    dat_codpostal = models.CharField(max_length=10, blank=True, null=True)
    cod_provincia = models.CharField(max_length=3, blank=True, null=True)
    cod_pais = models.CharField(max_length=3, blank=True, null=True)
    dat_fantasia = models.CharField(max_length=40, blank=True, null=True)
    dat_telefono01 = models.CharField(max_length=40, blank=True, null=True)
    dat_telefono02 = models.CharField(max_length=40, blank=True, null=True)
    dat_fax = models.CharField(max_length=40, blank=True, null=True)
    dat_email = models.CharField(max_length=60, blank=True, null=True)
    dat_domentrega = models.CharField(max_length=40, blank=True, null=True)
    dat_locentrega = models.CharField(max_length=35, blank=True, null=True)
    dat_codposent = models.CharField(max_length=10, blank=True, null=True)
    dat_horaentre = models.CharField(max_length=15, blank=True, null=True)
    dat_contacto = models.CharField(max_length=20, blank=True, null=True)
    dat_diaspago = models.CharField(max_length=20, blank=True, null=True)
    dat_habilitado = models.CharField(max_length=1, blank=True, null=True)
    dat_fecultcom = models.DateTimeField(blank=True, null=True)
    cod_cobrador = models.CharField(max_length=4, blank=True, null=True)
    cod_vendedor = models.CharField(max_length=4, blank=True, null=True)
    cod_zona = models.CharField(max_length=4, blank=True, null=True)
    cod_recorrido = models.CharField(max_length=4, blank=True, null=True)
    dat_credcom = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_credchp = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_credcht = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_credotr = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_cuit = models.CharField(max_length=11, blank=True, null=True)
    dat_ingbrutos = models.CharField(max_length=15, blank=True, null=True)
    cod_convta = models.CharField(max_length=4, blank=True, null=True)
    cod_listapr = models.CharField(max_length=7, blank=True, null=True)
    dat_categoriaiva = models.CharField(max_length=5, blank=True, null=True)
    cod_transporte = models.CharField(max_length=4, blank=True, null=True)
    dat_tiesuc = models.CharField(max_length=1, blank=True, null=True)
    dat_tiecor = models.CharField(max_length=1, blank=True, null=True)
    cod_consiba = models.CharField(max_length=7, blank=True, null=True)
    cod_conriva = models.CharField(max_length=7, blank=True, null=True)
    cod_conpibr = models.CharField(max_length=7, blank=True, null=True)
    cod_conhaber = models.CharField(max_length=7, blank=True, null=True)
    cod_provib = models.CharField(max_length=3, blank=True, null=True)
    fec_credito = models.DateTimeField(blank=True, null=True)
    fec_alta = models.DateTimeField(blank=True, null=True)
    memo1 = models.TextField(blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    dat_tipocli = models.CharField(max_length=4, blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_veclaa'


class DboVeclaaOld(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(unique=True, blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=6, blank=True, null=True)
    dat_razonsocial = models.CharField(max_length=40, blank=True, null=True)
    dat_domicilio = models.CharField(max_length=40, blank=True, null=True)
    dat_localidad = models.CharField(max_length=35, blank=True, null=True)
    dat_codpostal = models.CharField(max_length=10, blank=True, null=True)
    cod_provincia = models.CharField(max_length=3, blank=True, null=True)
    cod_pais = models.CharField(max_length=3, blank=True, null=True)
    dat_fantasia = models.CharField(max_length=40, blank=True, null=True)
    dat_telefono01 = models.CharField(max_length=40, blank=True, null=True)
    dat_telefono02 = models.CharField(max_length=40, blank=True, null=True)
    dat_fax = models.CharField(max_length=40, blank=True, null=True)
    dat_email = models.CharField(max_length=60, blank=True, null=True)
    dat_domentrega = models.CharField(max_length=40, blank=True, null=True)
    dat_locentrega = models.CharField(max_length=35, blank=True, null=True)
    dat_codposent = models.CharField(max_length=10, blank=True, null=True)
    dat_horaentre = models.CharField(max_length=15, blank=True, null=True)
    dat_contacto = models.CharField(max_length=20, blank=True, null=True)
    dat_diaspago = models.CharField(max_length=20, blank=True, null=True)
    dat_habilitado = models.CharField(max_length=1, blank=True, null=True)
    dat_fecultcom = models.DateTimeField(blank=True, null=True)
    cod_cobrador = models.CharField(max_length=4, blank=True, null=True)
    cod_vendedor = models.CharField(max_length=4, blank=True, null=True)
    cod_zona = models.CharField(max_length=4, blank=True, null=True)
    cod_recorrido = models.CharField(max_length=4, blank=True, null=True)
    dat_credcom = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_credchp = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_credcht = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_credotr = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_cuit = models.CharField(max_length=11, blank=True, null=True)
    dat_ingbrutos = models.CharField(max_length=15, blank=True, null=True)
    cod_convta = models.CharField(max_length=4, blank=True, null=True)
    cod_listapr = models.CharField(max_length=7, blank=True, null=True)
    dat_categoriaiva = models.CharField(max_length=5, blank=True, null=True)
    cod_transporte = models.CharField(max_length=4, blank=True, null=True)
    dat_tiesuc = models.CharField(max_length=1, blank=True, null=True)
    dat_tiecor = models.CharField(max_length=1, blank=True, null=True)
    cod_consiba = models.CharField(max_length=7, blank=True, null=True)
    cod_conriva = models.CharField(max_length=7, blank=True, null=True)
    cod_conpibr = models.CharField(max_length=7, blank=True, null=True)
    cod_conhaber = models.CharField(max_length=7, blank=True, null=True)
    cod_provib = models.CharField(max_length=3, blank=True, null=True)
    fec_credito = models.DateTimeField(blank=True, null=True)
    fec_alta = models.DateTimeField(blank=True, null=True)
    memo1 = models.TextField(blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    dat_tipocli = models.CharField(max_length=4, blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_veclaa_old'


class DboVecnaa(models.Model):
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=6, blank=True, null=True)
    dat_razonsocial = models.CharField(max_length=40, blank=True, null=True)
    dat_fantasia = models.CharField(max_length=40, blank=True, null=True)
    dat_domicilio = models.CharField(max_length=40, blank=True, null=True)
    dat_localidad = models.CharField(max_length=35, blank=True, null=True)
    dat_codpostal = models.CharField(max_length=10, blank=True, null=True)
    cod_provincia = models.CharField(max_length=3, blank=True, null=True)
    cod_pais = models.CharField(max_length=3, blank=True, null=True)
    dat_telefono01 = models.CharField(max_length=40, blank=True, null=True)
    dat_telefono02 = models.CharField(max_length=40, blank=True, null=True)
    dat_fax = models.CharField(max_length=40, blank=True, null=True)
    dat_email = models.CharField(max_length=60, blank=True, null=True)
    dat_contacto = models.CharField(max_length=20, blank=True, null=True)
    dat_memo = models.TextField(blank=True, null=True)
    dat_cuit = models.CharField(max_length=11, blank=True, null=True)
    dat_categoriaiva = models.CharField(max_length=5, blank=True, null=True)
    fec_alta = models.DateTimeField(blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vecnaa'


class DboVecoaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=7, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=35, blank=True, null=True)
    cod_numeracion = models.CharField(max_length=3, blank=True, null=True)
    dat_autman = models.CharField(max_length=1, blank=True, null=True)
    dat_actstock = models.CharField(max_length=1, blank=True, null=True)
    cod_comstock = models.CharField(max_length=5, blank=True, null=True)
    cod_comteso = models.CharField(max_length=7, blank=True, null=True)
    dat_tipodecuenta = models.CharField(max_length=2, blank=True, null=True)
    dat_tipcomprobante = models.CharField(max_length=2, blank=True, null=True)
    dat_signo = models.IntegerField(blank=True, null=True)
    dat_cancopias = models.IntegerField(blank=True, null=True)
    cod_comprob = models.CharField(max_length=5, blank=True, null=True)
    cod_comproe = models.CharField(max_length=5, blank=True, null=True)
    dat_comision = models.CharField(max_length=1, blank=True, null=True)
    cod_ce_empresa = models.CharField(max_length=4, blank=True, null=True)
    cod_su_sucursal = models.CharField(max_length=4, blank=True, null=True)
    dat_difepre = models.IntegerField(blank=True, null=True)
    dat_obsa = models.CharField(max_length=10, blank=True, null=True)
    dat_obsb = models.CharField(max_length=10, blank=True, null=True)
    dat_obse = models.CharField(max_length=10, blank=True, null=True)
    dat_caia = models.CharField(max_length=50, blank=True, null=True)
    dat_caib = models.CharField(max_length=50, blank=True, null=True)
    dat_caie = models.CharField(max_length=50, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vecoaa'


class DboVecvaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=4, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=35, blank=True, null=True)
    dat_cancuotas = models.IntegerField(blank=True, null=True)
    dat_desfin = models.CharField(max_length=1, blank=True, null=True)
    imp_valor1 = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    imp_valor2 = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    imp_valor3 = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    imp_valor4 = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    imp_valor5 = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    dat_diasvto = models.IntegerField(blank=True, null=True)
    cod_clave = models.CharField(max_length=5, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vecvaa'


class DboVecxaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=7, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=35, blank=True, null=True)
    dat_clase = models.CharField(max_length=3, blank=True, null=True)
    dat_colsui = models.IntegerField(blank=True, null=True)
    dat_colsuc = models.IntegerField(blank=True, null=True)
    dat_tasa1 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    dat_minimponible = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vecxaa'


class DboVedfaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_ce_empresa = models.CharField(max_length=4, blank=True, null=True)
    cod_su_sucursal = models.CharField(max_length=4, blank=True, null=True)
    cod_cliente = models.CharField(max_length=6, blank=True, null=True)
    cod_familia = models.CharField(max_length=8, blank=True, null=True)
    dat_dtoitem = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_dtoadic = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vedfaa'


class DboVenuaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=3, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=35, blank=True, null=True)
    dat_proxnroa = models.IntegerField(blank=True, null=True)
    dat_proxnrob = models.IntegerField(blank=True, null=True)
    dat_proxnroe = models.IntegerField(blank=True, null=True)
    dat_prefijoa = models.CharField(max_length=5, blank=True, null=True)
    dat_prefijob = models.CharField(max_length=5, blank=True, null=True)
    dat_prefijoe = models.CharField(max_length=5, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_venuaa'


class DboVepaaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=3, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=35, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vepaaa'


class DboVephaa(models.Model):
    nro_operacion = models.IntegerField(blank=True,primary_key=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)
    cod_sucursal = models.CharField(max_length=4, blank=True, null=True)
    cod_cliente = models.CharField(max_length=6, blank=True, null=True)
    cod_succli = models.CharField(max_length=3, blank=True, null=True)
    cod_comprobante = models.CharField(max_length=7, blank=True, null=True)
    dat_numero = models.IntegerField(blank=True, null=True)
    fec_feccompro = models.DateTimeField(blank=True, null=True)
    cod_transporte = models.CharField(max_length=4, blank=True, null=True)
    cod_condvta = models.CharField(max_length=4, blank=True, null=True)
    dat_observa01 = models.CharField(max_length=50, blank=True, null=True)
    dat_observa02 = models.CharField(max_length=50, blank=True, null=True)
    dat_observa03 = models.CharField(max_length=50, blank=True, null=True)
    dat_observa04 = models.CharField(max_length=50, blank=True, null=True)
    dat_observa05 = models.CharField(max_length=50, blank=True, null=True)
    dat_forma = models.CharField(max_length=2, blank=True, null=True)
    dat_recepciono = models.CharField(max_length=35, blank=True, null=True)
    cod_lista = models.CharField(max_length=7, blank=True, null=True)
    cod_vendedor = models.CharField(max_length=4, blank=True, null=True)
    fec_entrega = models.DateTimeField(blank=True, null=True)
    dat_domentrega = models.CharField(max_length=80, blank=True, null=True)
    cod_traentrega = models.CharField(max_length=4, blank=True, null=True)
    dat_ordendecompra = models.CharField(max_length=15, blank=True, null=True)
    dat_moneda = models.CharField(max_length=20, blank=True, null=True)
    dat_retenido = models.CharField(max_length=1, blank=True, null=True)
    dat_motivo = models.CharField(max_length=20, blank=True, null=True)
    fec_retencion = models.DateTimeField(blank=True, null=True)
    cod_centrocostos = models.CharField(max_length=4, blank=True, null=True)
    dat_memo = models.TextField(blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vephaa'


class DboVepiaa(models.Model):
    nro_operacion = models.IntegerField(blank=True,primary_key=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)
    cod_sucursal = models.CharField(max_length=4, blank=True, null=True)
    cod_cliente = models.CharField(max_length=6, blank=True, null=True)
    cod_succli = models.CharField(max_length=3, blank=True, null=True)
    cod_comprobante = models.CharField(max_length=7, blank=True, null=True)
    dat_numero = models.IntegerField(blank=True, null=True)
    fec_feccompro = models.DateTimeField(blank=True, null=True)
    cod_producto = models.CharField(max_length=15, blank=True, null=True)
    cod_familia = models.CharField(max_length=8, blank=True, null=True)
    fec_feclimite = models.DateTimeField(blank=True, null=True)
    dat_cantid01 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    dat_cantid02 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    dat_entreg01 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    dat_entreg02 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    dat_factur01 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    dat_factur02 = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_precio = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    dat_descto = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    dat_desctoadi = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    cod_serie = models.CharField(max_length=7, blank=True, null=True)
    dat_retenido = models.CharField(max_length=1, blank=True, null=True)
    dat_preparado = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    cod_centrocostos = models.CharField(max_length=4, blank=True, null=True)
    dat_color = models.CharField(max_length=7, blank=True, null=True)
    dat_juego = models.CharField(max_length=2, blank=True, null=True)
    dat_terminacion = models.CharField(max_length=5, blank=True, null=True)
    dat_artstock = models.CharField(max_length=15, blank=True, null=True)
    dat_nivelurg = models.CharField(max_length=1, blank=True, null=True)
    dat_artcliente = models.CharField(max_length=20, blank=True, null=True)
    dat_obsart1 = models.CharField(max_length=15, blank=True, null=True)
    dat_obsart2 = models.CharField(max_length=15, blank=True, null=True)
    fec_proceso = models.DateTimeField(blank=True, null=True)
    cod_prefactura = models.CharField(max_length=7, blank=True, null=True)
    nro_prefactura = models.IntegerField(blank=True, null=True)
    dat_proceso = models.CharField(max_length=6, blank=True, null=True)
    fec_ultproceso = models.DateTimeField(blank=True, null=True)
    dat_facturacion = models.CharField(max_length=1, blank=True, null=True)
    dat_terminado = models.CharField(max_length=1, blank=True, null=True)
    cod_factura = models.CharField(max_length=7, blank=True, null=True)
    nro_factura = models.IntegerField(blank=True, null=True)
    imp_paripeso = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    imp_parireal = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    imp_paridolar = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    imp_parieuro = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    imp_parimerco = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vepiaa'


class DboVepraa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=3, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=35, blank=True, null=True)
    cod_pais = models.CharField(max_length=3, blank=True, null=True)
    dat_alicuota = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    dat_coeficiente = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    dat_provsicore = models.CharField(max_length=2, blank=True, null=True)
    dat_auxi1 = models.CharField(max_length=7, blank=True, null=True)
    dat_auxi2 = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vepraa'


class DboVesuaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=3, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=40, blank=True, null=True)
    cod_cliente = models.CharField(max_length=6, blank=True, null=True)
    dat_domicilio = models.CharField(max_length=30, blank=True, null=True)
    dat_localidad = models.CharField(max_length=30, blank=True, null=True)
    dat_codpostal = models.CharField(max_length=10, blank=True, null=True)
    cod_provincia = models.CharField(max_length=3, blank=True, null=True)
    cod_pais = models.CharField(max_length=3, blank=True, null=True)
    dat_telefono01 = models.CharField(max_length=30, blank=True, null=True)
    dat_telefono02 = models.CharField(max_length=30, blank=True, null=True)
    dat_email = models.CharField(max_length=30, blank=True, null=True)
    dat_contacto = models.CharField(max_length=30, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vesuaa'


class DboVetraa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=4, blank=True, null=True)
    dat_nombre = models.CharField(max_length=35, blank=True, null=True)
    dat_domicilio = models.CharField(max_length=35, blank=True, null=True)
    dat_localidad = models.CharField(max_length=35, blank=True, null=True)
    dat_codpos = models.CharField(max_length=10, blank=True, null=True)
    cod_provincia = models.CharField(max_length=3, blank=True, null=True)
    cod_pais = models.CharField(max_length=3, blank=True, null=True)
    dat_nrocuit = models.CharField(max_length=13, blank=True, null=True)
    dat_telefono01 = models.CharField(max_length=30, blank=True, null=True)
    dat_telefono02 = models.CharField(max_length=30, blank=True, null=True)
    dat_email = models.CharField(max_length=60, blank=True, null=True)
    dat_horaentre = models.CharField(max_length=40, blank=True, null=True)
    cod_recorrido = models.CharField(max_length=40, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vetraa'


class DboVeveaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=4, blank=True, null=True)
    dat_nombre = models.CharField(max_length=35, blank=True, null=True)
    dat_domicilio = models.CharField(max_length=35, blank=True, null=True)
    dat_localidad = models.CharField(max_length=35, blank=True, null=True)
    dat_codpos = models.CharField(max_length=10, blank=True, null=True)
    cod_provincia = models.CharField(max_length=3, blank=True, null=True)
    cod_pais = models.CharField(max_length=3, blank=True, null=True)
    dat_telefono01 = models.CharField(max_length=30, blank=True, null=True)
    dat_telefono02 = models.CharField(max_length=30, blank=True, null=True)
    dat_telefono03 = models.CharField(max_length=30, blank=True, null=True)
    dat_email = models.CharField(max_length=60, blank=True, null=True)
    dat_categoriaiva = models.CharField(max_length=5, blank=True, null=True)
    dat_liqiva = models.CharField(max_length=1, blank=True, null=True)
    imp_porventas = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    imp_porcobra = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    imp_comventa = models.CharField(max_length=1, blank=True, null=True)
    imp_comcobra = models.CharField(max_length=1, blank=True, null=True)
    imp_comprod = models.CharField(max_length=1, blank=True, null=True)
    dat_cuit = models.CharField(max_length=11, blank=True, null=True)
    dat_agrupado = models.CharField(max_length=10, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_veveaa'


class DboVezoaa(models.Model):
    memo = models.TextField(blank=True, null=True)
    nro_serie = models.IntegerField(blank=True,primary_key=True)
    cod_codigo = models.CharField(max_length=4, blank=True, null=True)
    dat_descripcion = models.CharField(max_length=35, blank=True, null=True)
    sys_users = models.CharField(max_length=20, blank=True, null=True)
    sys_time = models.CharField(max_length=20, blank=True, null=True)
    sys_fecha = models.DateTimeField(blank=True, null=True)
    dat_vercam = models.IntegerField(blank=True, null=True)
    fec_eliminacion = models.DateTimeField(blank=True, null=True)
    cod_empresa = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo_vezoaa'
