def delta(a, b, c):
    delta = float(0.0);
    delta = (b ** 2) - 4 * a * c;
    return delta;

def bhaskarax1(delta, a, b):
    x1 = (-b + (delta ** 0.5)) / (2 * a);    
    return x1;

def bhaskarax2(delta, a, b):
    x2 = (-b - (delta ** 0.5)) / (2 * a);
    return x2;