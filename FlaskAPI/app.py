import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #creating a class object which contains the methods and functions
app.config["DEBUG"] = True #shows a specific error when the code is malformed
model = pickle.load(open('rfmodel.pkl', 'rb'))

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('index.html')


# 'POST': Here it means that the function is receiving data from the user
# 'GET' : If GET would have been used, the function would also send data.
@app.route('/predict' ,methods = ['GET','POST']) # form action=url_for('predict').The predict in "url_for" points here
def predict():
    if request.method == 'POST':
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        car_age = int(request.form['car_age'])
    
        Fuel_Type = request.form['Fuel_Type']
        if Fuel_Type == 'CNG':
            Fuel_Type_CNG = 1
            Fuel_Type_Diesel = 0
            Fuel_Type_Petrol = 0
        elif Fuel_Type == 'Diesel':
            Fuel_Type_CNG = 0
            Fuel_Type_Diesel = 1
            Fuel_Type_Petrol = 0
        else:
            Fuel_Type_CNG = 0
            Fuel_Type_Diesel = 0
            Fuel_Type_Petrol = 1
        
        Seller_Type = request.form['Seller_Type']
        if Seller_Type == 'Dealer':
            Seller_Type_Dealer = 1
            Seller_Type_Individual = 0
        else:
            Seller_Type_Dealer = 0
            Seller_Type_Individual = 1
        
        Transmission_Type = request.form['Transmission_Type']
        if Transmission_Type == 'Automatic':
            Transmission_Automatic = 1
            Transmission_Manual = 0
        else:
            Transmission_Automatic = 0
            Transmission_Manual = 1
          
        feats = np.array([[Present_Price, Kms_Driven,Owner, car_age, Fuel_Type_CNG, Fuel_Type_Diesel, Fuel_Type_Petrol, 
                       Seller_Type_Dealer,Seller_Type_Individual, Transmission_Automatic, Transmission_Manual]])
                     
        prediction = model.predict(feats)
    
        output = round(prediction[0], 2) # [0]: CHOOSING THE FIRST ARRAY(THE PREDICTION) FROM A 2D ARRAY.
        
        if output < 0:
            return render_template('index.html', prediction_text = 'The car should not be sold')
        else:
            return render_template('index.html', prediction_text = 'The predicted selling price of the car is: {}'.format(output))
    else:
        return render_template('index.html')
            
    
    




if __name__ == "__main__":
    app.run(debug = True)
