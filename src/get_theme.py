import requests, time, sys
from pyquery import PyQuery as pq

location = " ".join(sys.argv[1:])

# Query google for sunrise, parse the page for the time, and convert to float.
resp = requests.get('http://google.com/search?q=sunrise:'+location)
sunrise = pq(resp.text).find('li.g:first td.r:first b:first').text()
h,m = map(float, sunrise[:-2].split(':'))
sunrise = h + m / 60. 

# Query google for sunrise, parse the page for the time, and convert to float.
resp = requests.get('http://google.com/search?q=sunset:'+location)
sunset = pq(resp.text).find('li.g:first td.r:first b:first').text()
h,m = map(float, sunset[:-2].split(':'))
sunset = 12. + h + m / 60. 

# Set the current time.
current_time = time.strftime('%I,%M,%p')
h,m,ap = current_time.split(',')
h, m = float(h), float(m)
h += 0. if ap.lower()=='am' else 12.
current_time = h + m / 60.


if current_time >= sunrise and current_time < sunset:
    print "Day"
else:
    print "Night"
