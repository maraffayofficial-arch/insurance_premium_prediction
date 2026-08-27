from pydantic import BaseModel,Field
from typing import Annotated,Dict

class predicted_response(BaseModel):
    prediction:Annotated[str,Field(...,description='Your premium category')]
    confidence:Annotated[float,Field(...,description='The confdence of the model on predicted premium category')]
    class_probabilities:Dict[str,float]=Field(...,description='The confdence of the model on predicted premium category')