from fastapi import FastAPI, File, UploadFile
from io import StringIO
import pandas as pd
import joblib

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The API is working successfully..."}


@app.post("/batch_prediction")
async def predict(file: UploadFile = File(...)):
    # Cargar el modelo de predicción
    model = joblib.load("model/tree_model.joblib")

    # Leer el contenido del archivo CSV
    content = await file.read()
    data = pd.read_csv(StringIO(content.decode("utf-8")))

    # Realizar la predicción
    predictions = model.predict(data)

    # Retornar las predicciones
    return {"predictions": list(predictions)}
