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
    model = joblib.load("tree_model.joblib")

    content = await file.read()
    data = pd.read_csv(StringIO(content.decode("utf-8")))

    predictions = model.predict(data)
    return {"predictions": list(predictions)}
