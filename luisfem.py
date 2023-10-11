def tablamultiplicar(numero: int):

    if numero < 1 or numero > 10:
       print(f"No se puede procesar el numero {numero}")
    else:   
       for a in range(1, 11):
           print(f"{numero} x {a} = {numero * a}")
 
tablamultiplicar(2)
tablamultiplicar(11)
tablamultiplicar(5)
tablamultiplicar(0)
tablamultiplicar(10)
tablamultiplicar(12)
