from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import joblib

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Root</h3>"
    return html.format(format)

# TO DO:  Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction

    input looks like:
    {
        "data":[
            [0,0],
            [1,1]
        ]
    }
    result looks like:
    { "prediction": [ 1 ] }

    """

    try:
        print("try to load joblib")
        clf = joblib.load("binary_clf.joblib")
    except:
        LOG.info("Model not loaded")
        return "Model not loaded"

    json_payload_data = request.json["data"]
    LOG.info("JSON payload: json_payload_data %s" % json_payload_data)
    
    prediction = clf.predict(json_payload_data)

    strResult = "["    
    for x in prediction:
        strResult = strResult + str(x) + ","
    strResult = strResult[:-1]
    strResult += "]"
    

    return jsonify({'prediction': strResult})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
