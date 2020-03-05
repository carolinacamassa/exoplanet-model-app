#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify
import logging, sys
from flask_wtf.csrf import CSRFProtect
# form imports
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DecimalRangeField
from wtforms.fields import SubmitField

# model imports
import pandas as pd
import numpy as np
import sklearn
from joblib import load


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ty4425hk54a21eee5719b9s9df7sdfklx'
csrf = CSRFProtect(app)
csrf.init_app(app)

@app.before_first_request
def startup():
    global rforest
    global score
    score = [0]
    rforest = load("model/model.joblib")



# form to collect user input:
class InputForm(FlaskForm):
    default_val = [10, 1,30,0.1,1,5]
    p_radius = DecimalRangeField('Radius', default =  default_val[0] )
    p_mass = DecimalRangeField('Mass', default = default_val[1] )
    p_period = DecimalRangeField('Period', default = default_val[2]  )
    p_distance = DecimalRangeField('Effective th. distance from star', default = default_val[3]  )
    s_radius = DecimalRangeField('Radius',default =  default_val[4] )
    s_mag = DecimalRangeField('Magnitude',default =  default_val[5]  )
    submit = SubmitField('Submit')


# Load the serialized ML model


@app.route("/", methods=['POST', 'GET'])
def index():
    global score
    form = InputForm()
    logging.warning("Index page loading.")
    probability = 100
    if form.validate_on_submit():
        x_user = pd.DataFrame([[form.p_radius.data,
    		form.p_mass.data, form.p_period.data, form.p_distance.data,
            form.s_radius.data,form.s_mag.data]], columns = features)
        score = rforest.predict(x_user[features])
        probs =  rforest.predict_proba(x_user[features])
        probability = np.max(probs)*100
        print(probs, file = sys.stderr)
    return render_template('index.html', form=form, prob = probability ,hab_score = score[0])






# model related variables
features = ['P_RADIUS_EST',
			 'P_MASS_EST',
			 'P_PERIOD',
			 'P_DISTANCE_EFF',
			 'S_RADIUS_EST',
			 'S_MAG']
