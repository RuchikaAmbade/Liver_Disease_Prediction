from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    features = [float(request.form.get(f)) for f in [
        'Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphatase',
        'Alanine_Aminotransferase', 'Aspartate_Aminotransferase',
        'Albumin', 'Albumin_and_Globulin_Ratio'
    ]]
    
    # Make prediction
    prediction = model.predict([features])[0]
    result = "Liver Disease Detected" if prediction == 1 else "No Liver Disease"
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
