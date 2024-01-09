# Concrete Strength Prediction App

This Flask web application predicts the compressive strength of concrete based on user-input parameters. It uses a Gradient Boosting Regressor model trained on historical data.

## File Structure

- `app.py`: Main application script.
- `gbr.pkl`: Pickled Gradient Boosting Regressor model.
- `scaler.pkl`: Pickled StandardScaler used for feature scaling.
- `templates/index.html`: HTML template for the user interface.
- `requirements.txt`: List of Python dependencies.

## Running the Application

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the Flask application: `python app.py`.
3. Open a web browser and go to `http://localhost:5000`.

## Explanation of Files

- `app.py`: The main application script containing the Flask app and prediction logic.
- `gbr.pkl`: Serialized Gradient Boosting Regressor model for concrete strength prediction.
- `scaler.pkl`: Serialized StandardScaler for feature scaling.
- `templates/index.html`: HTML template for rendering the user interface and displaying predictions.
- `requirements.txt`: A list of Python dependencies required to run the application.

## Usage

1. Input values for various concrete parameters in the provided form.
2. Click on the "Predict" button to get the predicted compressive strength.
