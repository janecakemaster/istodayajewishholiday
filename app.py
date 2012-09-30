import os
import ast
from flask import *
from holidays import *


app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('static', filename='index.html'))


@app.route('/date')
def get_page():
    return request.args.get('date', '')

# parse holidates.txt 
# put those dates into function
# store greg dates in an array
# compare to current date
def get_holidays():
	h = Holidays()
	# gregdate
	hebdates = open('holidates.txt').read()
	hebdates = ast.literal_eval(hebdates)
	for key, items in hebdates.iteritems():
		if len(items) == 3:
			date = items[0]
			month = items[1]
			duration = items[2]
			print key
			# greg_year = 
			# h.hebrew_to_gregorian(greg_year, month, date, 1)
	return

@app.route('/static/<path:file_path>')
def static_fetch(file_path):
	return app.send_static_file(str(file_path))

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)



