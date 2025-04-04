def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = ((vuelto - pesos) * 100)
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    print("\nVuelto\n")
    print("Pesos:\n{pesos}")
    print("Centavos:\n{centavos}")
change()
