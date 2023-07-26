import pysurfline as surfAPI
params = {
    "spotId": "584204204e65fad6a7709aad",
    "days": 5,
    "intervalHours": 3,
}

def display(params):

	report = surfAPI.SurfReport(params)


	df = str(report.surf)
	data = df.split()
	
	# catg, dates, times, minWave, maxWave, windSpeed, windType, windDirection = [],[],[],[],[],[],[],[]

	catg = ['Date','Time','Smallest waves [m]','Biggest waves [m]','Wind Speed [kph]','Wind direction','Wind angle']
	
	#category

	data = data[6:len(data)]
	for z in range(len(data)):
		if data[z] == 'NaN':
			data[z] = 'Flat'


	
	# # print(data, '\n\n')
	# #dates
	# dates = data[::7]
	# # print(dates, '\n\n')
	# # #dates

	# #times
	# times = data[1::7]
	# # print(times, '\n\n')
	# # #times

	# #minWave
	# minWave = data[2::7]
	# # print(minWave, '\n\n')
	# # #minWave

	# #maxWave
	# maxWave = data[3::7]
	# # print(maxWave, '\n\n')
	# # #maxWave

	# #windspeed
	# windSpeed = data[4::7]
	# # print(windSpeed, '\n\n')
	# # #windspeed

	# #windtype
	# windType = data[5::7]
	# # print(windType, '\n\n')
	# # #windtype

	# #direction
	# windDirection = data[6::7]
	# # print(windDirection, '\n\n')
	# # #direction

	
	return data, catg


