# coding: utf8

def index():
    form = SQLFORM(db.venta)

    return dict(form=form)
