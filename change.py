def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = ((vuelto - pesos) * 100)
    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
change()
