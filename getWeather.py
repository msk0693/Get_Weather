import webbrowser, sys

if len(sys.argv) > 1:
	location = '+'.join(sys.argv[1:])
else:
	print "\nEnter an Area to Get Today's Weather"
	city = raw_input("City: ")
	state = raw_input("State: ")
	zipp = raw_input("Zip: ")

	location = city + '+' + state + '+' + zipp

webbrowser.open('https://weather.com/weather/today/l/' + location)


