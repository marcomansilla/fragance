# coding: utf8

db.define_table('proveedor',
    Field('nombre'),
    Field('telefono','integer'),
    Field('domicilio'),
    Field('email','string'),
    format='%(id)s - %(nombre)s'
    
    )

db.define_table('articulo',
    Field('codigo'),
    Field('descripcion','string'),
    Field('cantidad'),
    Field('plista'),
    Field('proveedor',db.proveedor),
    Field('uingreso','date'),
    format='%(descripcion)s'
    )

db.define_table('cliente',
    Field('nombre'),
    Field('rsocial'),
    Field('domicilio'),
    Field('telefono'),
    format='%(id)s - %(nombre)s'
    )

db.define_table('venta',
    Field('cliente',db.cliente),
    Field('articulo','list:integer'),
    Field('total','double'),
    Field('fventa','datetime')
    )

db.articulo.uingreso.requires=IS_DATE(format=T('%Y-%m-%d'))
