from califica import evaluar_cliente

# Edad: 17 , Ingresos: 2000
def test_rechazo_por_edad():
  resultado = evaluar_cliente(edad=17, ingresos=2000)
  assert resultado["aprobado"] == False
  assert resultado["categoria"] == None

# Edad: 19, Ingresos: 900
def test_rechazo_por_ingresos():
  resultado = evaluar_cliente(edad=19, ingresos=900)
  assert resultado["aprobado"] == False

# Tarjeta OH Regular
def test_oh_regular():
  resultado = evaluar_cliente(edad=22, ingresos=2000)
  assert resultado["aprobado"] == True
  assert resultado["categoria"] == "Tarjeta OH"

def test_oh_premium():
  resultado = evaluar_cliente(edad=30, ingresos=5500)
  assert resultado["aprobado"] == True
  assert resultado["categoria"] == "Tarjeta OH Premium"

def test_oh_regular_por_edad():
  resultado = evaluar_cliente(edad=24, ingresos=6000)
  assert resultado["aprobado"] == True
  assert resultado["categoria"] == "Tarjeta OH"
