from fastapi import FastAPI
from app.schemas import LoanData
import pickle
import numpy as np
import pandas as pd

app = FastAPI()

with open('classifier.pkl', 'rb') as file:
    classifier = pickle.load(file)

@app.get('/')
async def home():
    return "Check you are eligible for Loan or Not!"

@app.post('/check-status')
async def check_loan_status(request: LoanData):
    data = request.dict()

    gender = 1 if data['gender'] == "Male" else 0
    married = 1 if data['married'] == "Married" else 0
    dependents = int(data['dependents'].rstrip("+"))
    education = 1 if data['education'] == 'Graduate' else 0
    self_employed = 1 if data['self_employed'] == 'Yes' else 0
    applicant_income = float(data['applicant_income'])
    coapplicant_income = float(data['coapplicant_income'])
    loan_amount = float(data['loan_amount'])
    loan_amount_term = float(data['loan_amount_term'])
    credit_history = 1 if data['credit_history'] == 'Yes' else 0
    property_area = 1 if data['property_area'] == "Urban" else (2 if data['property_area'] == "Semiurban" else 0)

    input_data = np.array([[gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]])

    prediction = classifier.predict(input_data)

    if prediction[0] == 1:
        return "Congratulations! Your loan application is Approved."
    else:
        return "Sorry, your loan application is Rejected."
