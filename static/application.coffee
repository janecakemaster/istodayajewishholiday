$ ->
  if navigator.geolocation
    navigator.geolocation.getCurrentPosition gotPosition, errorPosition, timeout: 20000