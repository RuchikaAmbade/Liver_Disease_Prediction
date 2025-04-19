from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open("trained_model.pkl", "rb"))

# Initialize a single Flask app
app = Flask(__name__)

# Route for the API
@app.route("/api", methods=["POST"])
def api_predict():
    # Example JSON payload: {"age": 50, "bilirubin": 1.2, "protein": 6.4}
    data = request.get_json()
    # Include the rest of your feature inputs below
    features = np.array([data['age'], data['bilirubin'], data['protein']])  # Adjust as per your model
    prediction = model.predict([features])
    return jsonify({"Prediction": "Liver Disease" if prediction[0] == 1 else "No Liver Disease"})

# Route for the HTML Frontend
@app.route("/")
def home():
    return render_template("index.html")  # Render the form from index.html

# Route for Frontend Form Submission
@app.route("/predict", methods=["POST"])
def frontend_predict():
    # Process form inputs from the HTML frontend
    age = float(request.form["Age"])
    total_bilirubin = float(request.form["Total Bilirubin"])
    direct_bilirubin = float(request.form["Direct Bilirubin"])
    alkaline_phosphatase = float(request.form["Alkaline Phosphatase"])
    alanine_aminotransferase = float(request.form["Alanine Aminotransferase"])
    aspartate_aminotransferase = float(request.form["Aspartate Aminotransferase"])
    albumin = float(request.form["Albumin"])
    albumin_globulin_ratio = float(request.form["Albumin and Globulin Ratio"])

    # Prepare features for the model
    features = [[age, total_bilirubin, direct_bilirubin, alkaline_phosphatase,
                 alanine_aminotransferase, aspartate_aminotransferase, albumin, albumin_globulin_ratio]]
    
    # Make a prediction
    prediction = model.predict(features)
    result = "Liver Disease" if prediction[0] == 1 else "No Liver Disease"

    return f"<h1>Prediction Result: {result}</h1>"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)