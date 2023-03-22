from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import RadioField
from wtforms import SelectField
from wtforms.fields import EmailField
from wtforms import validators
from wtforms import IntegerField
from wtforms import FloatField, DecimalField
from wtforms import BooleanField
from wtforms.fields import TimeField
from wtforms.fields import DateField
from wtforms import HiddenField
from wtforms import SubmitField
from wtforms.fields import BooleanField
from wtforms.fields import DateTimeLocalField
from wtforms.fields import TextAreaField



def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo no debe estar vacio.')

class login(Form):
    usuario = StringField("", [validators.InputRequired(message="Nombre de usuario vacio!")])
    clave = PasswordField("", [validators.InputRequired(message="Ingrese la contraseña!"),
                               validators.Length(min=6,max=15,message="Se requiere contraseña")])
    honeypot = HiddenField('',[length_honeypot])
    
    
class orden_mantenimiento(Form):
    orden=StringField("", [validators.InputRequired(message="Rellene este campo por favor")])
    
class pagina_3(Form):
     
     puestos_d_trabajo = SelectField('Puestos de trabajo', choices=[('1', 'Electricista'), ('2', 'Mecánico'), ('3', 'Supervisor'), ('4', 'Servicios Generales')])
     ficha = IntegerField("", [validators.input_required(message="Ingrese los datos en el campo soicitado")])
     tiempo_real = IntegerField("", [validators.input_required(message="Ingrese los datos en el campo soicitado")])
     checkbox=BooleanField("", validators=[validators.AnyOf([True, False])], default='checked')
     time_start= DateTimeLocalField("", format='%Y-%m-%d %H:%M:%S')
     time_end= DateTimeLocalField("", format='%Y-%m-%d %H:%M:%S')
     texto= TextAreaField("",)