import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Function to generate synthetic data and train the model
def create_model():
    # Set random seed for reproducibility
    np.random.seed(42)

    # Number of samples
    num_samples = 1000

    # Generate synthetic data
    data = {
        'age': np.random.randint(18, 60, num_samples),                      # Age between 18 and 60
        'income': np.random.randint(20000, 120000, num_samples),             # Annual income between $20,000 and $120,000
        'loan_amount': np.random.randint(5000, 50000, num_samples),          # Loan amount between $5,000 and $50,000
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Define a simple rule for eligibility
    df['eligible'] = np.where((df['income'] > 50000) & (df['loan_amount'] < 0.3 * df['income']), 1, 0)

    # Features and target variable
    X = df[['age', 'income', 'loan_amount']]
    y = df['eligible']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    return model

# Create and train the model at the start of the app
model = create_model()

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    age = int(request.form['age'])
    income = float(request.form['income'])
    loan_amount = float(request.form['loan_amount'])

    # Create a DataFrame for prediction
    input_data = pd.DataFrame({
        'age': [age],
        'income': [income],
        'loan_amount': [loan_amount]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Prepare the result
    result = 'Eligible for Loan' if prediction[0] == 1 else 'Not Eligible for Loan'
    
    return render_template('result.html', result=result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
