# Command to compile: coffee -bc *.coffee
# From https://github.com/mikeplate/Mobile-Web-Demo/blob/master/geolocation/sunrise.html
# $ ->
#   if navigator.geolocation
#     navigator.geolocation.getCurrentPosition gotPosition, errorPosition, timeout: 20000

$ ->
  $.get
    url: '/' # This is the API url that is going to be called. Must be the same as in Flask.
    data: # This is the data that is sent to flask and can be accessed through the request object in flask
      date: new Date() # Sends the current date/
    success: (data) ->
      $('.inject-target').html data # Inject the data from flask in into the element with inject-target class.