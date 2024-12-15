from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    DecimalField,
    HiddenField,
    RadioField,
    StringField,
    SubmitField,
    SelectField
)
from wtforms.validators import DataRequired, NumberRange

from .models import monedas


def validate_moneda(form, field):
    if field.data not in monedas:
        raise ValidationErr(
            'No se permite una trasacción con moneda de origen y destino iguales')


class MovimientoForm(FlaskForm):

    moneda_from = SelectField('From:', choices=[
        ('', ''),
        ('EUR', 'Euro'),
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('ADA', 'Cardano'),
        ('SOL', 'Solana'),
        ('XRP', 'Ripple'),
        ('DOT', 'Polkadot'),
        ('DOGDE', 'Dogecoin')], validators=[DataRequired('Debe ingresar una moneda'), validate_moneda])

    moneda_to = SelectField('To', choices=[
        ('', ''),
        ('EUR', 'Euro'),
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('ADA', 'Cardano'),
        ('SOL', 'Solana'),
        ('XRP', 'Ripple'),
        ('DOT', 'Polkadot'),
        ('DOGDE', 'Dogecoin')], validators=[DataRequired('Debe ingresar una moneda'), validate_moneda])

    Q = DecimalField('Q', validators=[
        DataRequired('Debes indicar una cantidad correcta')
    ])

    PU = DecimalField('P.U', validators=[
        DataRequired('Debes indicar una cantidad correcta')
    ])

    submit = SubmitField('Guardar')
