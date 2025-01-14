from flask import Flask, request, jsonify
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the user
    data = request.get_json()
    user_input = data['input']
    
    # Preprocess input text
    input_vec = vectorizer.transform([user_input])
    
    # Get prediction
    prediction = model.predict(input_vec)[0]

    return jsonify({'decision': prediction})

if __name__ == "__main__":
    app.run(debug=True)
