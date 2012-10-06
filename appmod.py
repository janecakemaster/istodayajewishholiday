import json
import ast
import urllib2

url = 'http://www.hebcal.com/hebcal/?v=1;cfg=json;nh=on;year=now;month=x;ss=on;mf=on;m=72;s=on'
response = urllib2.urlopen(url).read()
data = ast.literal_eval(response)
now = data['date']
dates = data['items']
