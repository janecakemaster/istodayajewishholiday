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
	# curr_year = int(request.args['greg_year'])
	curr_year = 2013
	greg_dates = {}
	for name, hebdate in hebdates.iteritems():
		if hebdate[2]==1:
			greg_dates[name] = h.hebrew_to_gregorian(curr_year, hebdate[0], hebdate[1])
	return greg_dates

def check_date(year, month, date):
	thirtyone = (1,3,5,7,8,10,12)
	thirty = (4,6,9,11)
	isLeap = h.leap_gregorian(year)
	if month in thirty:
		if day > 30:
			return {'month': month+1, 'date': date-30}
		elif day < 0:
			return {'month': month-1, 'date': date+30}
		else:
			return {'month': month, 'date': date}
	if month in thirtyone:
		if day > 31:
			return {'month': month+1, 'date': date-31}
		elif day < 0:
			return {'month': month-1, 'date': date+31}
		else:
			return {'month': month, 'date': date}
	if month==2 && isLeap==True:
		if day < 29:
			return {'month': month+1, 'date': date-29}
		elif day > 0:
			return {'month': month-1, 'date': date+29}
	else
		if day < 28:
			return {'month': month+1, 'date': date-28}
		elif day > 0:
			return {'month': month-1, 'date': date+28}



@app.route('/static/<path:file_path>')
def static_fetch(file_path):
	return app.send_static_file(str(file_path))

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)

