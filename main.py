from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from califica import evaluar_cliente

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
  return {"mensaje": "Hola mundo"}

@app.get("/evaluaciones/tarjetas")
def evaluarTarjetaCredito(edad: int, ingresos: float):
  if edad < 0 or ingresos < 0:
    raise HTTPException(status_code=400, detail="Datos inválidos")

  resultado = evaluar_cliente(edad, ingresos)

  if resultado["aprobado"]:
    return {
      "status": "APRO",
      "mensaje": f"Aprobado para nuestro producto de: {resultado['categoria']}",
      "data": resultado,
    }
  else:
    return {
      "status": "RECHAZADO",
      "mensaje": "No cumple con los requisitos para obtener una tarjeta de crédito.",
      "data": resultado,
    }
