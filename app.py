from flask import Flask, render_template, request
import pandas as pd
import joblib
app = Flask(__name__)
file = open("model/logistic_regression_model.pkl", "rb")
model = joblib.load(file)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        form_data = request.form.to_dict()

        try:
            df = pd.DataFrame([form_data])
            df = df.astype(float)
        except ValueError:
             return "Please provide valid numeric inputs."
        prediction = model.predict(df)

        result = "Malignant" if prediction[0] == 1 else "Benign"

        return render_template("predict.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
    
