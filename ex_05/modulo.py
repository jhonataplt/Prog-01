def delta(a, b, c):
    delta = float(0.0);
    delta = (b ** 2) - 4 * a * c;
    return delta;

def bhaskara(delta, a, b):
    x1 = (-b + (delta ** 0.5)) / (2 * a);
    x2 = (-b - (delta ** 0.5)) / (2 * a);
    resultado = [x1, x2];
    return resultado;