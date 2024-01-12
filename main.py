from fastapi import FastAPI
from model_handler import PredictRequest
from model_handler import ModelHandler
from error_handlers import internal_error_handler

app = FastAPI()
model_handler = ModelHandler()

@app.on_event("startup")
def on_startup():
    model_handler.load_model('../decision_tree_model.pkl')

app.add_exception_handler(Exception, internal_error_handler)

@app.get('/predict_get')
def predict_get(latitude: float, longitude: float):
    prediction = model_handler.predict(latitude, longitude)
    return {'predicted_prix_m2': prediction}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=5000)
