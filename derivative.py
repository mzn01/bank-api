def derivative(x):
    h=0.0001
    d=((x+h)**2-x**2)/h

    return d

w=derivative(2)
print(w)