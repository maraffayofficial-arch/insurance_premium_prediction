import pickle as pkl
import pandas as pd

with open("model/model.pkl",'rb') as f:
    model=pkl.load(f)

MODEL_VERSION='10.0.0'
# brign out all the classes in the model that could exist
model_classes=model.classes_.tolist()

def make_prediction(input:dict):
    input_df=pd.DataFrame([input])
    predicted_class=model.predict(input_df)[0]
    probabilities=model.predict_proba(input_df)[0]
    confidence_score=max(probabilities)

    class_probab=dict(zip(model_classes,map(lambda p: round(p, 4),probabilities)))
    return {
        'prediction':predicted_class,
        'confidence':round(confidence_score,4),
        'class_probabilities':class_probab

    }


