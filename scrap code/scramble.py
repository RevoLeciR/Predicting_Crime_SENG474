import csv
import random

with open('Victoria_BC_Police_Department_Data_class_numbered.csv', 'rb') as read:
	reader = csv.reader(read)
	testlist = list(reader)

top = testlist[0]
del testlist[0]
random.shuffle(testlist)

writefile = open('Victoria_BC_Police_Department_Data_class_numbered_random.csv','wb')
writer = csv.writer(writefile)
writer.writerow(top)

for i in range(30):
	writer.writerow(testlist[i])