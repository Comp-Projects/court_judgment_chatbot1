# api/function.py
from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    # Load the CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), '../judgments.csv')
    df = pd.read_csv(csv_file_path)
    
    # Your existing logic here...
    
    return jsonify({'response': 'Your response'})

if __name__ == '__main__':
    app.run()
