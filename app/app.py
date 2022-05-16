import ccapproval

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply', methods=['POST'])
def apply():
    gender = request.form['Gender']
    age = request.form['Age']
    debt = request.form['Debt']
    married = request.form['Married']
    bank_customer = request.form['BankCustomer']
    education_level = request.form['EducationLevel']
    ethnicity = request.form['Ethnicity']
    years_employed = request.form['YearsEmployed']
    prior_default = request.form['PriorDefault']
    employed = request.form['Employed']
    credit_score = request.form['CreditScore']
    drivers_license = request.form['DriversLicense']
    citizen = request.form['Citizen']
    zipcode = request.form['ZipCode']
    income = request.form['Income']

    features = {'Gender': gender, 'Age': age, 'Debt': debt,
                'Married': married, 'BankCustomer': bank_customer,
                'EducationLevel': education_level, 'Ethnicity': ethnicity,
                'YearsEmployed': years_employed, 'PriorDefault': prior_default,
                'Employed': employed, 'CreditScore': credit_score,
                'DriversLicense': drivers_license, 'Citizen': citizen,
                'ZipCode': zipcode, 'Income': income}

    application = ccapproval.create_application(features)
    result = ccapproval.isPreapproved(application)

    return render_template('index.html', preapproval_status=result)
 
if __name__ == '__main__':
    app.run()
