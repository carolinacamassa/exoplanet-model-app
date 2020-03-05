#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify
import logging
# form imports
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DecimalRangeField
from wtforms.fields import SubmitField

# model imports
import pandas as pd
import numpy as np
import scikit-learn
from joblib import load


app = Flask(__name__)

# form to collect user input:
class InputForm(FlaskForm):
    p_radius = DecimalRangeField('Radius', default = 10 )
    p_mass = DecimalRangeField('Mass', default = 1 )
    p_period = DecimalRangeField('Period', default = 30 )
    p_distance_eff = DecimalRangeField('Effective th. distance from star', default = 0.005 )
    s_radius = DecimalRangeField('Radius', default = 1 )
    s_mag = DecimalRangeField('Magnitude', default = 5 )
    submit = SubmitField('Submit')



@app.route("/", methods=['POST', 'GET'])
def index():
    logging.warning("Index page loading.")
    form = InputForm( meta={'csrf': False})
    if request.method == 'POST' and form.validate():
        x_user = pd.DataFrame([[p_radius.data,
    		p_mass.data, p_period.data, p_distance.data,
            s_radius.data,s_mag.data]], columns = features)

        score = rforest.predict(x_user[features])
        return render_template('index.html', form=form, hab_score = score )
    else:
        return render_template('index.html', form=form, hab_score = 't.b.d.' )


# model related variables
# gbm_model = None
features = ['P_RADIUS_EST',
			 'P_MASS_EST',
			 'P_PERIOD',
			 'P_DISTANCE_EFF',
			 'S_RADIUS_EST',
			 'S_MAG']



# Load the serialized ML model
@app.before_first_request
def startup():
	global rforest
	rforest = load(open("static/model.joblib"))



# @app.route('/background_process', methods=['POST', 'GET'])
# def background_process():
# 	density = float(request.args.get('density'))
# 	pH = float(request.args.get('pH'))
# 	sulphates = float(request.args.get('sulphates'))
# 	alcohol = float(request.args.get('alcohol'))
# 	color = int(request.args.get('color'))
#
#
# 	# create data set of new data
#
#
# 	# predict quality based on incoming values
#
#
# 	# get best quality prediction from original quality scale
# 	return jsonify({'hab_score':h_score})
