import webbrowser
from OAuth_cal import getFutureEvents, updateEvent

def main():
	#Give the user a reference for google calendar colours
	webbrowser.open('https://eduardopereira.pt/wp-content/uploads/2012/06/google_calendar_api_event_color_chart.png', new=2)
	#retreive next 100 events
	events = getFutureEvents()

	#retreive info on events to change through user input
	numClasses = input("Number of classes this semester: ")
	numClasses = int(numClasses)

	classColours = {}

	#creat a dictionary containing the class color info (className : colourCode)
	for x in range(0,numClasses):
		className = input("Class name: ")
		classColourID = input("ColourID to set (see webpage that opened): ")

		classColours[className] = classColourID

	#probably not efficent but meh
	for event in events:
		for className in classColours:
			#if the name of the course is contained in the title then change the colour
			if(className in event['summary']):
				event['colorId'] = classColours[className]
				updateEvent(event)

	print("Finished. Enjoy your colourful timetable :)")

if __name__ == '__main__':
    main()