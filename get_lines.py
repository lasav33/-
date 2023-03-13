def zise(z):
    x = z['lowerCorner'].split()
    y = z['upperCorner'].split()
    return [str(abs(float(x[0]) - float(y[0]))), str(abs(float(x[1]) - float(y[1])))]