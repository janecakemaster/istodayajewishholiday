import os
import ast
from flask import Flask, request, redirect, url_for
from holidays import Holidays
import json

app = Flask(__name__)
hebdates = {}
h = Holidays()
with open('holidates.txt') as fd:
	hebdates = fd.read()
hebdates = ast.literal_eval(hebdates)

@app.route('/', methods=["GET"])
def index():
	if request.args.get('greg_year'):
		return json.dumps(get_holidays())
	return redirect(url_for('static', filename='index.html'))

def get_holidays():
	# year = int(request.args['greg_year'])
	year = 2013
	greg_dates = {}
	for name, hebdate in hebdates.iteritems():
		greg_dates[name] = h.hebrew_to_gregorian(year, hebdate[0], hebdate[1])
	return greg_dates

@app.route('/static/<path:file_path>')
def static_fetch(file_path):
	return app.send_static_file(str(file_path))

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)

