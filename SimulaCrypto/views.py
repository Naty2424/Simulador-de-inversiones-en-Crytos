from datetime import date
from flask import Flask, flash, render_template,  redirect, request, url_for
from . import app
# ALMACEN
from .forms import MovimientoForm
from .models import ListaMovimientos, Movimiento


@app.route('/')
def home():
    """
    muestras los movimientos realizados
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    return render_template("inicio.html", movs=lista)


def exito():
    lista = ListaMovimientos()
    moneda_to = moneda_to.MovimientoFrom()
    return render_template('compra.html', monedas=moneda_to, movs=lista)


@app.route('/purchase', methods=['GET', 'POST'])
def compra():
    """
    permite la compra de cryptos
    """
    if request.method == "GET":
        return render_template("compra.html", movs)

    if request.method == "POST":
        """
        se agrega el movimiento a la lista, se guarda y se devuelve Ok 
        si todo correcto, si no devolvemos el error
        """
        movs = Movimiento(request.form)
        boton = request.form['boton']

        moneda_from = request.form['moneda_from']
        moneda_to = request.form['moneda_to']
        cantidad_from = float(request.form['cantidad_from'])

        if moneda_from != moneda_to and boton == 'calculadora':

            consulta = Consulta_coinap()
            cantidad_to = consulta.calcular_cantidad_to()
            precio_unitario = consulta.calcular_precio_unitario()

            return render_template('compra.html', form=movs, cantidad_to=cantidad_to, precio_unitario=precio_unitario)

        elif boton == 'OK':  # Si se presionó el botón de aceptar, validamos el formulario
            # Implementar la función para validar los datos
            if forms.validate(request.form):
                # Insertar en Lista Movimientos
                ListaMovimientos.agregar_movs(movs)
                # Redirige a una página inicial
                return redirect(url_for('exito'))
            else:
                return render_template('compra.html', error="Datos inválidos")

    return render_template('compra.html')


pass


def venta():
    """
    permite la venta de las cryptos
    """
    if request.method == "GET":
        return render_template("compra.html")
    if request.method == "POST":
        """
        se agrega el movimiento a la lista, se guarda y se devuelve Ok 
        si todo correcto, o el error
        """
        movs = Movimiento(request.forma)
        ListaMovimientos.agregar_movs(movs)
        return request.forma


def intercambio():
    """
    Permite intercsmbiar cryptos
    """


pass


# @app.route('/status')
# def home():
#    if ALMACEN == 0:
#       lista = ListaMovimientosCsv()
#    else:
#        lista = ListaMovimientosDB()
#    return render_template('inicio.html', movs=lista.movimientos)
# @app.route('/eliminar/<int:id>')
# def delete(id):
#    lista = ListaMovimientosDB()
#    template = 'borrado.html'
#    try:
#        result = lista.eliminar(id)
#        if not result:
#           template = 'error.html'
#   except:
#       template = 'error.html'
#  return render_template(template, id=id)
# @app.route('/editar/<int:id>', methods=['GET', 'POST'])
# def actualizar(id):
#    if request.method == 'GET':
#        lista = ListaMovimientosDB()
#        movimiento = lista.buscarMovimiento(id)
#        formulario = MovimientoForm(data=movimiento)
#        return render_template('form_movimiento.html', form=formulario, id=movimiento.get('id'))
#    if request.method == 'POST':
#        lista = ListaMovimientosDB()
#        formulario = MovimientoForm(data=request.form)
#
#        if formulario.validate():
#            fecha = formulario.fecha.data
#            mov_dict = {
#                'fecha': fecha.isoformat(),
#                'concepto': formulario.concepto.data,
#                'tipo': formulario.tipo.data,
#                'cantidad': formulario.cantidad.data,
#                'id': formulario.id.data
#            }
#            movimiento = Movimiento(mov_dict)
#            resultado = lista.editarMovimiento(movimiento)
#            if resultado == 1:
#                flash('El movimiento se ha actualizado correctamente')
#            elif resultado == -1:
#                flash('El movimiento no se ha guardado. Inténtalo de nuevo.')
#            else:
#                flash('Houston, tenemos un problema')
#        else:
#            print(formulario.errors)
#            return render_template('form_movimiento.html', form=formulario, id=formulario.id.data)
#    return redirect(url_for('home'))
