from datetime import date

from flask import flash, render_template,  redirect, request, url_for
from . import ALMACEN, app

from .forms import MovimientoForm
from .models import ListaMovimientosCsv, ListaMovimientosDB, Movimiento


@app.route('/')
  def home ():
   """"
   muestras los movimientos realizados
   """

 @app.route('/purchase', methods=['GET', 'POST'])
   def compra():
   """
   permite al compra de cryptos
   """
# pass
  def venta():
  """
  permite la venta de las cryptos
  """
# pass
  def intercambio():
     """
     Permite intercsmbiar cryptos
     """
     
# pass
 @app.route('/status')
 def home():
     if ALMACEN == 0:
         lista = ListaMovimientosCsv()
     else:
         lista = ListaMovimientosDB()
    return render_template('inicio.html', movs=lista.movimientos)
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
