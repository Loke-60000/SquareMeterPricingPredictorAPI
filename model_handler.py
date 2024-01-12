import pickle
import numpy as np
from fastapi import HTTPException
from pydantic import BaseModel

class PredictRequest(BaseModel):
    latitude: float
    longitude: float

class ModelHandler:
    def __init__(self):
        self.model = None

    def load_model(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                self.model = pickle.load(file)
        except FileNotFoundError:
            print('Model file not found')

    def predict(self, latitude, longitude):
        if self.model is None:
            raise HTTPException(status_code=503, detail="Model not loaded")
        input_data = np.array([[latitude, longitude]])
        return self.model.predict(input_data)[0]
