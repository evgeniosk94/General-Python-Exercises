from flask import Flask, request, jsonify       # flask is a module that  allows to write a python service which can serve http requests 
import util                                     # 
app = Flask(__name__)                           # Create the app with Flask

@app.route('/get_location_names')                            # Expose http end point, this will return Hi
def get_location_names():
        response = jsonify({
                'locations': util.get_location_names()      # Util will contain all the core routines 
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        
        return response 

@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bedroom = int(request.form['bedroom'])
        bath = int(request.form['bath'])
        
        estimated_price = util.get_estimated_price(location, total_sqft, bedroom, bath)
        
        if estimated_price == "Invalid Location":
                return jsonify({'error': "Invalid location given."}), 400 # Return HTTp 400 error
        
        # Convert to Python float (if it's NumPy type)
        if hasattr(estimated_price, 'item'):
                estimated_price = estimated_price.item()    

        response = jsonify({
                'estimated_price': estimated_price
         })

        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

        
if __name__ == "__main__":
        print("Starting Python Flask Server for Home Price Prediction...")
        util.load_saved_artifacts()
        app.run()                                               # It will run the application in a specific port