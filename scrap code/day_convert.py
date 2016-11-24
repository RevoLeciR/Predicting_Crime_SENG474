import csv

with open('Victoria_BC_Police_Department_Data_new.csv','rb') as fr:
	reader = csv.reader(fr)
	testlist = list(reader)
	
labels = testlist[0]
del testlist[0]

days = {'Sunday':0, 'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6}

#i[8] is location of day of the week
for i in range(len(testlist)):
	testlist[i][8] = days[testlist[i][8]]
	
newfile = open('Victoria_BC_Police_Department_Data_day.csv','wb')
writer = csv.writer(newfile)

writer.writerow(labels)
for i in testlist:
	writer.writerow(i)
	
