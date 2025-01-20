from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('final_model_pix.pkl', 'rb') as f:
    pipeline = pickle.load(f)

@app.route('/')
def home():
    return jsonify({'message': 'API SUMUP ;)'})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Api Deve enviar dados'}), 400
        
        features = np.array(list(data.values())).reshape(1, -1)

        prediction_prob = pipeline.predict_proba(features)[:, 1][0]
        return jsonify({
            'prob': float(prediction_prob),
            'classe': 'Fraude' if prediction_prob >= 0.7 else 'Nao Fraude'
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True) 