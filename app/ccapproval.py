import pickle
import pandas as pd
import numpy as np


attributes = ['Gender', 'Age', 'Debt',
              'Married', 'BankCustomer', 'EducationLevel',
              'Ethnicity', 'YearsEmployed', 'PriorDefault',
              'Employed', 'CreditScore', 'DriversLicense',
              'Citizen', 'ZipCode', 'Income',
              'ApprovalStatus']

def create_application(data):
    df = pd.DataFrame(columns=attributes)
    
    df.loc[0, 'Gender'] = data['Gender']   
    df.loc[0, 'Age'] = data['Age']
    df.loc[0, 'Debt'] = data['Debt']
    df.loc[0, 'Married'] = data['Married']
    df.loc[0, 'BankCustomer'] = data['BankCustomer']
    df.loc[0, 'EducationLevel'] = data['EducationLevel']
    df.loc[0, 'Ethnicity'] = data['Ethnicity']
    df.loc[0, 'YearsEmployed'] = data['YearsEmployed']
    df.loc[0, 'PriorDefault'] = data ['PriorDefault']
    df.loc[0, 'Employed'] = data['Employed']
    df.loc[0, 'CreditScore'] = data['CreditScore']
    df.loc[0, 'DriversLicense'] = data['DriversLicense']
    df.loc[0, 'Citizen'] = data['Citizen']
    df.loc[0, 'ZipCode'] = data['ZipCode']
    df.loc[0, 'Income'] = data['Income']
    df.loc[0, 'ApprovalStatus'] = np.nan

    return df

def isPreapproved(df):
    model = pickle.load(open('app/model.pkl', 'rb'))
    prediction = model.predict(df)
    
    if prediction == '+':
        return 'Approved'
    else:
        return 'Declined'
