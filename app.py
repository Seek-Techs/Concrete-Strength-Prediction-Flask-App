from flask import Flask, render_template, request
import numpy as np
import pickle
from flask_wtf import FlaskForm
from wtforms import FloatField,IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

# Initialize Flask application
app = Flask(__name__)
bootstrap = Bootstrap(app)

# Load the pre-trained model and scaler
model = pickle.load(open('gbr.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Set Flask app secret key for form security
app.config['SECRET_KEY'] = 'hard to guess string'

# Define the prediction form
class PredictForm(FlaskForm):
    cement = FloatField('Cement quantity', validators=[DataRequired()])
    blast_furnace_slag = FloatField('Blast Furnace Slag')
    fly_ash = FloatField('Fly Ash')
    water = FloatField('Water')
    superplasticizer = FloatField('Sperplasticizer', )
    coarse_aggregate = FloatField('Coarse Aggregate',)
    fine_aggregate = FloatField('Fine Aggregate')
    age = FloatField('Age in days', validators=[DataRequired()])
    submit = SubmitField('Predict')

# Define the Flask route for prediction
@app.route('/', methods=['POST', 'GET'])
def predict():
    # Create an instance of the prediction form
    form = PredictForm()
    # If form is submitted and validated
    if form.validate_on_submit():
        # Retrieve input values from the form
        cement = form.cement.data
        blast_furnace_slag = form.blast_furnace_slag.data
        fly_ash = form.fly_ash.data
        water = form.water.data
        superplasticizer = form.superplasticizer.data
        coarse_aggregate = form.coarse_aggregate.data
        fine_aggregate = form.fine_aggregate.data
        age = form.age.data

        # Create feature array for prediction
        float_features = [
            cement, 
            blast_furnace_slag, 
            fly_ash, 
            water, 
            superplasticizer, 
            coarse_aggregate,
            fine_aggregate, 
            age,
            ]
        features = [np.array(float_features)]
        final_features = scaler.transform(features)
        
        # Make prediction using the pre-trained mode
        prediction = model.predict(final_features)
        # print(prediction)

        # Render the prediction result in the HTML template
        return render_template('index.html', form=form, prediction=f'The compressive strength of concrete is {np.round(prediction[0], 2)}')
    # Render the initial form or form with errors
    return render_template('index.html', form=form, prediction=None)

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
    
    
