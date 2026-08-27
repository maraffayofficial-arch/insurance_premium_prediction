
from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Dict,Literal,Annotated
from config.city_tiers import tier_2_cities,tier_1_cities



class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description='Put age')]
    weight:Annotated[float,Field(...,gt=0,description='Put weight in kgs')]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description='put height in meters')]
    income_lpa:Annotated[float,Field(...,gt=0,description='Put income per year',examples=['2.3','1.2'])]
    smoker:Annotated[bool,Field(...,description='Enter you smoking status',examples=['True','False'])]
    city:Annotated[str,Field(...,description='Enter the City you reside in', examples=['mumbai','delhi'])]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'],Field(...,description='Enter your occupation',examples=['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'])]

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi


    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker==True and self.calculate_bmi>30:
            return 'High'
        elif self.smoker==False or self.calculate_bmi>27:
            return 'medium'
        else:
            return 'low'

    @field_validator("city")
    @classmethod
    def normalize_city_names(cls,city:str)->str:
        city=city.strip().title()
        return city

    

    @computed_field
    @property
    def city_tier(self)->int:
       
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

    @computed_field
    @property
    def age_group(self)->str:
        if self.age<25:
            return 'young'
        elif self.age<45:
            return 'adult'
        elif self.age<60:
            return "middle_aged"
        else:
            return 'senior'
