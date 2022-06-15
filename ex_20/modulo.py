def calcAreaTriangulo(a, b):

    x = float(0.0);
    y = float(0.0);
    area = float(0.0);

    x = float(0.0);
    y = float(0.0);

    if a == 0 or b == 0:
        area = 0;
    else:
        x = b/ a;
        y = a * x + b;

        area = (x * y) / 2;
        area /= 2;

    return area;