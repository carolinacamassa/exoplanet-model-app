#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify, Markup
# form imports
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DecimalRangeField
from wtforms.fields import SubmitField

import logging, io, os, sys
# model imports
# import pandas as pd
# import numpy as np
# import scikit-learn
# from joblib import load


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
    return render_template('index.html', form=form)
    	# on load set form with defaults
    	# return render_template('index.html', quality_prediction=1 #,
    	# 		other args, form = form)

# model related variables
# gbm_model = None
features = ['P_RADIUS_EST',
			 'P_MASS_EST',
			 'P_PERIOD',
			 'P_DISTANCE_EFF',
			 'S_RADIUS_EST',
			 'S_MAG']



# Load the serialized ML model
# @app.before_first_request
# def startup():
# 	global rforest
# 	rforest = load(open("static/model.joblib"))
#

#
# @app.route('/background_process', methods=['POST', 'GET'])
# def background_process():
#
# 	density = float(request.args.get('density'))
# 	pH = float(request.args.get('pH'))
# 	sulphates = float(request.args.get('sulphates'))
# 	alcohol = float(request.args.get('alcohol'))
# 	color = int(request.args.get('color'))
#
#
# 	# create data set of new data
# 	x_user = pd.DataFrame([[p_radius,
# 		p_mass, p_period, p_distance, s_radius,s_mag  ]], columns = features)
#
#
# 	# predict quality based on incoming values
# 	prediction = rforest.predict_proba(x_user[features])
#
# 	# get best quality prediction from original quality scale
# 	predicted_quality = [0,1,2][np.argmax(prediction[0])]
# 	return jsonify({'quality_prediction':predicted_quality})
