#Raíces de un polinomio de grado 2
#Solicitando los valores al usaurio
a = float(input('Por favor, ingrese el valor de a: '))
b = float(input('Por favor, ingrese el valor de b: '))
c = float(input('Por favor, ingrese el valor de c: '))

#Comprobando si tiene solución en los números reales
def realImaginary():
    answer = b**2-(4*a*c)
    if answer >= 0:
        root1 = round((-b+pow(answer,0.5))/(2*a),1)
        root2 = round((-b-pow(answer,0.5))/(2*a),1)
        message = 'Las raices de la ecuación cuadrática {}X^2 {}X {} son x1 = {} y x2 = {}'.format(a,b,c,root1, root2)
    else:
        message = 'La ecuación cuadrática no tiene solución en los números reales'
    return message

print(realImaginary())