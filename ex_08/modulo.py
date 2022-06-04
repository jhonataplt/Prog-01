def divisor(massaFinal, segundos):
    while massaFinal >= 0.5:
        massaFinal /= 2
        segundos += 50
    return massaFinal, segundos;

def conversorDeSegundos (segundos):
    minutos = segundos // 60
    horas = segundos // 3600
    segundos %= 60
    tempoDecorrido = (f'{horas}:{minutos}:{segundos}')
    return tempoDecorrido;