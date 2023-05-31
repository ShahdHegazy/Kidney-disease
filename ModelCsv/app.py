
import numpy as np
from flask import Flask, render_template, request
import pickle

# Load the model
model = pickle.load(open('RF.pkl', 'rb'))

# Create the Flask app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    if prediction == 1:
        result = "The person has kidney disease"
    elif prediction == 0:
        result = "The person does not has kidney disease"
    else:
        result = "Error"
    return render_template("index.html", prediction_text="{}".format(result))


if __name__ == "__main__":
    app.run(debug=True)
