
def evaluar_cliente(edad: int, ingresos: float) -> dict:
  if edad > 18 and ingresos > 1000:
    if ingresos < 5000:
      return {"aprobado": True, "categoria": "Tarjeta OH Premium", "linea": 2000}

    if ingresos >= 5000 and edad >= 25:
      return {"aprobado": True, "categoria": "Tarjeta OH Premium", "linea": 10000}

    return {"aprobado": True, "categoria": "Tarjeta OH", "linea": 2000}
  else:
    return {"aprobado": False, "categoria": None, "linea": None}
