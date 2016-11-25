import csv

with open('Victoria_BC_Police_Department_Data_class_combine.csv', 'rb') as file:
    reader = csv.reader(file)
    input = list(reader) #list which contains data of file

writefile = open('Victoria_BC_Police_Department_Data_class_combine_theft.csv', 'wb')
writer = csv.writer(writefile)

writer.writerow(input[0]) #headings

del input[0]

for i in input: #i5
	if int(i[5]) is 0:
		i[5] = 7
	elif int(i[5]) is 8:
		i[5] = 1
	elif int(i[5]) is 2:
		i[5] = 7
	elif int(i[5]) is 12:
		i[5] = 11
	
	elif int(i[5]) is 12:
		i[5] = 9
	elif int(i[5]) is 10:
		i[5] = 9	
	elif int(i[5]) is 11:
		i[5] = 9

	writer.writerow(i)