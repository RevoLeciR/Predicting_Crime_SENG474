import csv


with open('Central_Saanich_Police_Service.csv', 'rb') as fr:
	reader = csv.reader(fr)
	testlist = list(reader)

#format of the date/time is "MM/DD/YYYY HH:MM:SS AM/PM" on first column
for i in range(1,len(testlist)):
	month = testlist[i][0].split()[0][0] + testlist[i][0].split()[0][1]
	day = testlist[i][0].split()[0][3] + testlist[i][0].split()[0][4]
	year = testlist[i][0].split()[0][6] + testlist[i][0].split()[0][7] + testlist[i][0].split()[0][8] + testlist[i][0].split()[0][9]
	
	testlist[i][10] = month
	testlist[i][11] = day
	testlist[i][12] = year

with open('testcsvnew.csv', 'wb') as fw:
	write = csv.writer(fw, delimiter=',')
	
	for row in testlist:
		write.writerow(row)