import csv

with open('Victoria_BC_Police_Department_Data_date.csv','rb') as fr:
	reader = csv.reader(fr)
	testlist = list(reader)


removelist = ['SUSPICIOUS PERS/VEH/OCCURRENCE','BYLAW-NOISE','DRIVING COMPLAINTS','ANIMAL CALLS','FALSE ALARMS','EXCESSIVE SPEED-OVER 40KM',
			  'VI-VEHICLE IMPOUNDMENT','BUSINESS','LIQUOR-INTOX IN PUBLIC PLACE','TRAFFIC-WRITTEN WARNING','LIQUOR-CONSUME IN PUBLIC PLACE']
print len(testlist)
count = 0
delcount = 0

newlist = []
'''
TO BE REMOVED
Let's scrap, traffic (driving complaints), animal calls, false alarms, suspicious per/vehicle, 
vehicle stop, intoxicated in public?, and community policing
'''

for i in testlist:
	if i[1] not in removelist:
		newlist.append(i)
	count += 1


for i in range(len(newlist)):
	if newlist[i][1] in removelist:
		print newlist[i]

print len(newlist)

output = open('Victoria_BC_Police_Department_Data_new.csv', 'wb')
writer = csv.writer(output)

for i in newlist:
	writer.writerow(i)
	
