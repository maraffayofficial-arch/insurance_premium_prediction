from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import make_prediction
from model.predict import model,MODEL_VERSION
from schema.prediction_response import predicted_response

app=FastAPI()


@app.get('/')
def home():
    return {'message':'Premium Category API'}

@app.get('/health')
def health_check():
    return {'status':'OK',
            'Model_lodead' :model is not None,
            'Model_version': MODEL_VERSION
            }


@app.post("/predict",response_model=predicted_response)
def predict(data:UserInput): # importing the user input as the above pydantic model
    input_dict={
       'bmi':data.calculate_bmi,
       'income_lpa':data.income_lpa,
       'occupation':data.occupation,
       'age_group':data.age_group,
       'lifestyle_risk':data.lifestyle_risk,
       'city_tier':data.city_tier
    }
    # return print('check 1')
    try:
        prediction=make_prediction(input_dict)
        return JSONResponse(status_code=200,content={'predicted_category':prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
