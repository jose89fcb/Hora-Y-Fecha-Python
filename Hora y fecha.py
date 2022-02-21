
from datetime import datetime
from pytz import timezone


zonahoraria = timezone("Europe/Amsterdam")


fecha = datetime.now(zonahoraria)


formato_fecha = fecha.strftime("Fecha españa: "+"%d/%m/%Y"+ "\nHora españa: " + "%H:%M:%S")


print(formato_fecha)



def current_date_format(fecha):
    meses = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dia = fecha.day
    mes = meses[fecha.month - 1]
    año = fecha.year
    mensaje = "Fecha españa: "+"{} de {} del {}".format(dia, mes, año)

    return mensaje

now = datetime.now()
print(current_date_format(now))
