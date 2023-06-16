import datetime

def horas():
    hora = datetime.datetime.now().strftime('%H:%M')
    return hora