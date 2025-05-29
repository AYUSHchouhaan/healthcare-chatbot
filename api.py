from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

def load_data():
    return pd.read_csv(r"D:\UsesandAlternatives\medicines_50.csv")

df = load_data()

@app.route('/add_medicine/', methods=['POST'])
def add_medicine():
    global df  
    
    data = request.get_json()

    required_fields = ['medicine_name', 'usage', 'expiry_date', 'active_ingredients', 'side_effects', 'alternatives']
    
    for field in required_fields:
        if field not in data or not data[field]:  
            return jsonify({'error': f'Missing or empty field: {field}'}), 400

    if df[df["Medicine Name"].str.contains(data["medicine_name"], case=False, na=False)].empty:
     
        new_data = pd.DataFrame([{
            "Medicine Name": data["medicine_name"],
            "Usage": data["usage"],
            "Expiry Date": data["expiry_date"],
            "Active Ingredients": data["active_ingredients"],
            "Side Effects": data["side_effects"],
            "Alternatives": data["alternatives"]
        }])
        
        df = pd.concat([df, new_data], ignore_index=True)
        
        df.to_csv(r"D:\UsesandAlternatives\medicines_50.csv", index=False)  
        
        return jsonify({"message": f"Medicine '{data['medicine_name']}' added successfully!"}), 201
    else:
        return jsonify({"error": "Medicine already exists"}), 400

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8000)
