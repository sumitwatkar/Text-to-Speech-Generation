# Importing necessary modules and functions
from src.exception import CustomException
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from src.components.get_accent import get_accent, get_accent_message
import sys
from src.components.text_to_speech import TTSGeneration

# Creating Flask app instance
app = Flask(__name__)
CORS(app)  # Allowing Cross-Origin Resource Sharing (CORS) for the Flask app

# Route for the home page
@app.route('/', methods=['GET'])
@cross_origin()
def home():
    try: 

        accent_list = get_accent_message()  # Getting accent messages using get_accent_message function
        return render_template('index.html', accent_list=accent_list)  # Rendering the index.html template with accent_list as context
    
    except Exception as e:
        raise CustomException(e, sys)

# Route for prediction
@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predict():
    try:
        if request.method == 'POST':

            data = request.json['data']  # Retrieving data from JSON payload
            
            accent_input = request.json['accent']  # Retrieving accent input from JSON payload
            
            accent = get_accent(accent_input)  # Getting accent using get_accent function
            
            result = TTSGeneration().text_to_speech(data, accent)  # Generating text-to-speech result
            
            return {"data": result.decode("utf-8")}  # Returning the result as JSON response
    
    except Exception as e:
        raise CustomException(e, sys)

# Running the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)  # Running the app on host 0.0.0.0 and port 8080 in debug mode