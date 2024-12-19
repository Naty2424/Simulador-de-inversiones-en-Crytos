from datetime import date
from flask import Flask, jsonify, flash, render_template,  redirect, request, url_for
from . import app

from .forms import MovimientoForm
from .models import Coinapi, ListaMovimientos, Movimiento


@app.route('/')
def home():
    """
    muestras los movimientos realizados
    """
    lista = ListaMovimientos()
   # lista.leer_desde_archivo()
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
        return render_template("compra.html", movimiento)

    if request.method == "POST":
        """
        se agrega el movimiento a la lista, se guarda y se devuelve Ok
        si todo correcto, si no devolvemos el error
        """
        movimiento = MovimientoForm(request.form)
        calcular = Movimiento()
        coinapi = Coinapi()
       # p_u =
        boton = request.form['boton']

        moneda_from = request.form['moneda_from']
        moneda_to = request.form['moneda_to']
        cantidad_from = float(request.form['cantidad_from'])

        if moneda_from != moneda_to and boton == 'calculadora':
            consulta = coinapi.consulta_coinap(
                moneda_to, cantidad_from, cantidad_to)
            cantidad_to = calcular.calcular_cantidad_to()
            precio_unitario = consulta.calcular_precio_unitario()

            return render_template('compra.html', form=movimiento, cantidad_to=cantidad_to, precio_unitario=precio_unitario)

        elif boton == 'OK':  # Si se presionó el botón de aceptar, validamos el formulario
            # Implementar la función para validar los datos
            if forms.validate(request.form):
                # Insertar en Lista Movimientos
                Movimiento.agregar_movs(movimiento)
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
        movimiento = Movimiento(request.form)
        ListaMovimientos.agregar_movs(movimiento)
        return request.form


def intercambio():
    """
    Permite intercsmbiar cryptos
    """


pass


@app.route('/calcular', methods=['GET'])
def calcular_inversion():
    # Se cargan los datos de DB
    movimientos = pd.read_csv('movimientos.csv')

    saldo_eur_invertido = (movimiento[movimientos['moneda_to'] == 'EUR']['cantidad_to'].sum() -
                           movimiento[movimientos['moneda_from'] == 'EUR']['cantodad_from'].sum())

    # Total de Eur invertidos
    total_eur_invertido = movimiento[movimientos['moneda_from']
                                     == 'EUR']['cantidad_from'].sum()

    # Valor actual de las cryptos
    valor_act_crypto = 0

    # Obtenemos todas las cryptos únicas
    cryptos = movimiento[movimientos['moneda_from']
                         != 'EUR']['moneda_from'].unique()
    for crypto in cryptos:
        total_crypto = (movimiento[movimientos['moneda_to'] == crypto]['cantidad_to']. sum() -
                        movimiento[movimientos['moneda_from'] == crypto]['cantidad_from'].sum())

    # Convertir crypto a eur con CoinApi
    if total_crypto > 0:
        tasa_cambio = get_crypto_to_eur(crypto)
        valor_actual_crypto += total_crypto * tasa_cambio

    # Cálculo final
    valor_act = total_eur_invertido + saldo_eur_invertido + valor_act_crypto

    # Devolver los datos de CoinApi
    resultado = {'saldo_eur_invertido': round(saldo_eur_invertido, 2),
                 'total_eur_invertido': round(total_eur_invertido, 2),
                 'valor_act_crypto': round(valor_act_crypto, 2),
                 'valor_act_total': round(valor_act_total, 2)
                 }
    return jsonify(resultado)


@ app.route('/status')
def cambio_crytpo_to_eur(crypto):
    pass
