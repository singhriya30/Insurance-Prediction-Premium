from altair import value
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import MODEL_VERSION, model, predict_output
from schema.prediction_response import PredictionResponse
import pandas as pd
app = FastAPI()




@app.get('/')
def home():
    return {'message': 'Welcome to the Insurance Premium Prediction API.'}

@app.get('/health')
def health_check():
    return {
        'status': 'healthy',
        'Version': MODEL_VERSION
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):
    try:
        user_input = {
            'bmi': data.bmi,
            'age_group': data.age_group,
            'lifeStyle_risk': data.dict()['lifeStyle_risk'],
            'city_tier': data.city_tier,
            'income_lpa': data.income_lpa,
            'occupation': data.occupation
        }
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'response': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})