from pydantic import BaseModel

class LoanData(BaseModel):
    gender: str
    married: str
    dependents: str
    education: str
    self_employed: str
    applicant_income: float
    coapplicant_income: float
    loan_amount: float
    loan_amount_term: float
    credit_history: str
    property_area: str

    class Config:
        schema_extra = {
            "example": {
                "gender": "Male",
                "married": "Married",
                "dependents": "2",
                "education": "Graduate",
                "self_employed": "No",
                "applicant_income": 5000.0,
                "coapplicant_income": 3000.0,
                "loan_amount": 10000.0,
                "loan_amount_term": 12.0,
                "credit_history": "Yes",
                "property_area": "Urban"
            }
        }
