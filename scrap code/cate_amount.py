import csv

with open('Victoria_BC_Police_Department_Data_class_numbered.csv', 'rb') as file:
    reader = csv.reader(file)
    input = list(reader) #list which contains data of file
	
del input[0]

words = {'0':'Arson', '1':'Assault', '2':'Breaking and Entering', '3':'Disorder',
		 '4':'Drugs', '5':'Liquor', '6':'Other', '7':'Property Crime',
		 '8':'Robbery', '9':'Theft', '10':'Theft from Business', '11':'Theft from Vehicle',
		 '12':'Theft of Vehicle', '13':'Traffic', '14':'Weapons'}

count = {}

#6
for i in input:
	check_parent = count.get(i[5])
	
	if check_parent is None:
		count[i[5]] = 1
	else:
		count[i[5]] += 1

		
		
parentnum = open("parentnum.txt","w")
for i in range(len(count)):
	parentnum.write(sorted(count, key = count.get)[i] + ": " + str(sorted(count.values())[i]) + "\n")