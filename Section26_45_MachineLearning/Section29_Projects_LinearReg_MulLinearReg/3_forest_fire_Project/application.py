import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Write application as file name for deployment

# import ridge regressor and StandardScaler pickle
ridge_model = pickle.load(open("models/RidgeCV_fire.pkl", "rb"))
standard_scaler = pickle.load(open("models/scaler.pkl", "rb"))

application = Flask(__name__)
app = application


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        Temperature = int(
            request.form.get("Temperature")
        )  # Match With name="Temperature" of home.html
        RH = int(request.form.get("RH"))
        Ws = int(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = int(request.form.get("Classes"))
        Region = int(request.form.get("Region"))

        new_data_scaled = standard_scaler.transform(
            [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        )
        result = ridge_model.predict(
            new_data_scaled
        )  # Result in form of list so result[0]

        return render_template("home.html", results=result[0])
    # 29,57,18,0.0,65.7,3.4,1.3,1,1 -> 0.77
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # host=0.0.0.0 for publicly
