import os
from flask import Flask, request
import holidays
from holidays import Holidays


app = Flask(__name__)

@app.route('/')
def get_page():
    return request.args.get('date', '')

# parse holidates.txt 
# put those dates into function
# store greg dates in an array
# compare to current date

def get_holidays():
	h = Holidays()
	hebdates = open('jewholidays.txt').read
	for key, items in hebdates.iteritems():
		year =
		, hebrew_month, hebrew_day, year_is_gregorian=1
		h.hebrew_to_gregorian
	hebdates.close()

	return

@app.route('/static/<path:file_path>')
def static_fetch(file_path):
  return app.send_static_file(str(file_path))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



