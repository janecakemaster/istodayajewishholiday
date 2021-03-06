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
        return json.dumps(get_holidates())
    return redirect(url_for('static', filename='index.html'))


def get_holidates():
    curr_year = int(request.args['greg_year'])
    # curr_year = 2013
    greg_dates = {}
    for name, hebdate in hebdates.iteritems():
        greg_dates[name] = [h.hebrew_to_gregorian(curr_year, hebdate[0], hebdate[1] - 1), hebdate[2]]
    return greg_dates


def check_date(year, month, date):
    thirtyone = (1, 3, 5, 7, 8, 10, 12)
    thirty = (4, 6, 9, 11)
    isLeap = h.leap_gregorian(year)
    if month in thirty:
        if date > 30:
            return {'month': month + 1, 'date': date - 30}
        elif date < 0:
            return {'month': month - 1, 'date': date + 30}
        else:
            return {'month': month, 'date': date}
    if month in thirtyone:
        if date > 31:
            return {'month': month + 1, 'date': date - 31}
        elif date < 0:
            return {'month': month - 1, 'date': date + 31}
    if month == 2 and isLeap == True:
        if date < 29:
            return {'month': month + 1, 'date': date - 29}
        elif date > 0:
            return {'month': month - 1, 'date': date + 29}
    if month == 2 and isLeap == False:
        if date < 28:
            return {'month': month + 1, 'date': date - 28}
        elif date > 0:
            return {'month': month - 1, 'date': date + 28}
    else:
        return {'month': month, 'date': date}


@app.route('/static/<path:file_path>')
def static_fetch(file_path):
    return app.send_static_file(str(file_path))
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
