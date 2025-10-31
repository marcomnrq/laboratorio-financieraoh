from locust import HttpUser, task, between
import random

# Endpoint de "Hola Mundo"
class HolaMundo(HttpUser):
  wait_time = between(1, 3)
  @task
  def get_hola_mundo(self):
    self.client.get("/")

# Endpoint de /evaluaciones/tarjetas
class EvaluacionesTarjetas(HttpUser):
  wait_time = between(1, 3) # Cada usuario del test de carga espera entre 1 y 3 segundos.
  grupo_de_edades = [7, 15, 19, 25, 50, 60, 70]
  grupo_de_ingresos = [500, 1000, 2000, 4000, 5500, 7500]

  @task(80)
  def get_evaluaciones_tarjetas(self):
    edad = random.choice(self.grupo_de_edades)
    ingresos = random.choice(self.grupo_de_ingresos)

    self.client.get("/evaluaciones/tarjetas", params={
      "edad": edad,
      "ingresos": ingresos,
    })

  @task(20)
  def get_evaluacion_tarjeta_incorrecto(self):
    with self.client.get("/evaluaciones/tarjetas", params={
      "edad": -50,
      "ingresos": 10000
    }, catch_response=True) as response:
      if response.status_code == 400:
        response.success()
      else:
        response.failure("Status error incorrecto.")

