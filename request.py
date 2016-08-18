from urllib2 import urlopen, URLError
import subprocess

try:
	request = urlopen("http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=en")
	subprocess.call(["cowsay", request.read()])
except URLError, e:
	print("Error.")
