from datetime import date, datetime

import csv
import sqlite3

RUTA_DB = 'SimulaCrypto/data/movimientos.db'


class DBManager:
    """
    Clase para interactuar con la base de datos.
    """

    def __init__(self, ruta):
        self.ruta = ruta

    def consultarSQL(self, consulta):

        # 1. Conectar a la base de datos
        conexion = sqlite3.connect(self.ruta)

        # 2. Abrir cursor
        cursor = conexion.cursor()

        # 3. Ejecutar la consulta
        cursor.execute(consulta)

        # 4. Tratar los datos
        # 4.1. Obtener los datos
        datos = cursor.fetchall()

        self.registros = []
        nombres_columna = []

        for columna in cursor.description:
            nombres_columna.append(columna[0])

        # [ "id", "fecha", "concepto", "tipo", "cantidad"  ]
        # (
        # (   1 , '2024-11-01', 'Calabaza', 'G', '3.56'  )
        # )

        # 4.2. Guardar los datos localmente
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columna:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.registros.append(movimiento)

        # 5. Cerrar la conexión
        conexion.close()

        # 6. Devolver el resultado
        return self.registros

    def borrar(self, id):

        sql = 'DELETE FROM movimientos WHERE id=?'
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()

        resultado = False
        try:
            cursor.execute(sql, (id,))
            conexion.commit()
            if cursor.rowcount > 0:
                resultado = True
            else:
                resultado = False
        except:
            conexion.rollback()

        conexion.close()
        return resultado

    def obtenerMovimiento(self, id):
        sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos WHERE id=?'

        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(sql, (id,))

        datos = cursor.fetchone()
        resultado = None
        if datos:
            nombres_columna = []

            for columna in cursor.description:
                nombres_columna.append(columna[0])

            movimiento = {}
            indice = 0
            for nombre in nombres_columna:
                movimiento[nombre] = datos[indice]
                indice += 1
            movimiento['fecha'] = date.fromisoformat(movimiento['fecha'])
            resultado = movimiento

        conexion.close()
        return resultado

    def actualizarMovimiento(self, movimiento):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        sql = 'UPDATE movimientos SET fecha=?, concepto=?, tipo=?, cantidad=? WHERE id=?'

        resultado = -1

        try:
            params = (
                movimiento.fecha,
                movimiento.concepto,
                movimiento.tipo,
                movimiento.cantidad,
                movimiento.id
            )
            cursor.execute(sql, params)
            conexion.commit()
            resultado = cursor.rowcount
        except Exception as ex:
            print('Ha ocurrido un error al actualizar el movimiento en la BD')
            print(ex)
            conexion.rollback()

        conexion.close()
        return resultado


class Movimiento:

    def __init__(self, dict_mov):
        self.errores = []

        # Validación de la hora

        try:
            self.hora = datetime.fromisoformat(hora)
        except ValueError:
            self.hora = None
            mensaje = f'La hora {hora} no es una hora ISO 8601 válida'
            self.errores.append(mensaje)
        except TypeError:
            self.hora = None
            mensaje = f'La hora {hora} no es una cadena'
            self.errores.append(mensaje)
        except:
            self.hora = None
            mensaje = f'Error desconocido con la hora'
            self.errores.append(mensaje)

        # Validación de la moneda
        if moneda in monedas:
            self.moneda = []
        else:
            raise ValueError(f'La moneda {moneda} no es valida')

         # Validación de la cantidad
        try:
            valor = float(cantidad)
            if valor > 0:
                self.cantidad = valor
            else:
                self.cantidad = 0
                mensaje = f'El importe de la cantidad debe ser un número mayor que cero'
                self.errores.append(mensaje)
        except ValueError:
            self.cantidad = 0
            mensaje = f'El valor no es convertible a número'
            self.errores.append(mensaje)

        self.moneda = moneda
        self.cantidad = cantidad

    def calcular_cantidad_to():

    def calcular_precio_unitario():

        precio_unitario = cantidad_from / cantidad_to

    def Consulta_coinap(moneda_from, moneda_to, cantidad_from, cantidad_to):
        api_key = 'tu_api_key_aquí'  # Reemplaza con tu API key
        url = f'https://rest.coinapi.io/v1/exchangerate/{
            cantidad_from}/{cantidad_to}?apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        rate = data['rate']
        total_to = rate * amount

    def agregar_movs():
        movement = {
            'fecha': datetime.now().date(),
            'hora': datetime.now().time(),
            'moneda_from': moneda_from,
            'moneda_to': moneda_to,
            'cantidad_from': cantidad_from,
            'cantidad_to': cantidad_to,
        }
        movs.append(movement)
        return redirect(url_for('exito'))

    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        return f'{self.fecha} | {self.concepto} | {self.tipo} | {self.cantidad}'

    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    def __init__(self):
        try:
            self.cargar_movimientos()
        except:
            self.movimientos = []

    def guardar(self):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos')

    def agregar(self, movimiento):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos')

    def cargar_movimientos(self):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos')

    def eliminar(self, id):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos')

    def buscarMovimiento(self, id):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos')

    def editarMovimiento(self, movimiento):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos')

    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result

    def __repr__(self):
        return self.__str__()


class ListaMovimientosDB(ListaMovimientos):

    def cargar_movimientos(self):
        db = DBManager(RUTA_DB)
        sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos'
        datos = db.consultarSQL(sql)

        self.movimientos = []
        for dato in datos:
            mov = Movimiento(dato)
            self.movimientos.append(mov)

    def eliminar(self, id):
        # TODO: Eliminar de verdad el movimiento
        db = DBManager(RUTA_DB)
        resultado = False

        try:
            resultado = db.borrar(id)
        except:
            print(
                f'El DB Manager ha fallado al borrar el movimiento con id {id}')

        return resultado

    def buscarMovimiento(self, id):
        db = DBManager(RUTA_DB)
        return db.obtenerMovimiento(id)

    def editarMovimiento(self, movimiento):
        db = DBManager(RUTA_DB)
        return db.actualizarMovimiento(movimiento)
