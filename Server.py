from flask import Flask, request, jsonify, render_template
import Global

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/api/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': Global.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = float(request.form['bath'])

    response = jsonify({
        'estimated_price': Global.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    Global.load_saved_artifacts()
    print("Starting Python Flask Server")
    app.run(debug=True)
