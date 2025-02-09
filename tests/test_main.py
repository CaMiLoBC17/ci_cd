import unittest
from fastapi.testclient import TestClient
from main import app  # Importamos la aplicación FastAPI

class TestMain(unittest.TestCase):
    def setUp(self):
        # Creamos un cliente de prueba para hacer solicitudes a la API
        self.client = TestClient(app)

    def test_root_endpoint(self):
        # Probamos que el endpoint raíz devuelve el mensaje correcto
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "The API is working successfully..."})

    def test_batch_prediction_endpoint(self):
        # Probamos que el endpoint de predicción funciona correctamente
        # Leemos el archivo CSV real desde la ruta 'data/xtest.csv'
        with open('data/xtest.csv', 'rb') as f:
            # Hacemos la solicitud POST con el archivo CSV de test
            response = self.client.post(
                "/batch_prediction", files={"file": ("xtest.csv", f, "text/csv")}
            )

        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        self.assertIn("predictions", response.json())

if __name__ == "__main__":
    unittest.main()
