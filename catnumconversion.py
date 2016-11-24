import csv

#read in csv file
with open('Central_Saanich_Police_Service_day.csv', 'rb') as file:
        reader = csv.reader(file)
        datalist = list(reader)	#list which contains data of file

for i in range(1,len(datalist)):
        tempList = datalist[i]	#temporary list of the current row in the file

	#converts word in row to corresponding numerical value
        for y in range(0,len(tempList)):
                if tempList[5] == "Arson":
                        datalist[i][5] = 0
		if tempList[5] == "Assault" or tempList[5] == "Assault with Deadly Weapon":
                        datalist[i][5] = 1
                if tempList[5] == "Breaking & Entering":
                        datalist[i][5] = 2
                if tempList[5] == "Disorder":
                        datalist[i][5] = 3
                if tempList[5] == "Drugs":
                        datalist[i][5] = 4
                if tempList[5] == "Liquor":
                        datalist[i][5] = 5
                if tempList[5] == "Other":
                        datalist[i][5] = 6
                if tempList[5] == "Property Crime":
                        datalist[i][5] = 7
                if tempList[5] == "Robbery":
                        datalist[i][5] = 8
                if tempList[5] == "Theft":
                        datalist[i][5] = 9
                if tempList[0] == "THEFT-SHOPLIFTING UNDER $5000" or tempList[0] == "THEFT-SHOPLIFTING OVER $5000":
                        datalist[i][5] = 10
                if tempList[5] == "Theft from Vehicle":
                        datalist[i][5] = 11
                if tempList[5] == "Theft of Vehicle":
                        datalist[i][5] = 12
                if tempList[5] == "Traffic":
                        datalist[i][5] = 13
                if tempList[5] == "Weapons Offense":
                        datalist[i][5] = 14

#write to csv file
with open('Central_Saanich_Police_Service_class_numbered.csv', 'wb') as fw:
        write = csv.writer(fw, delimiter=',')

        for row in datalist:
                write.writerow(row)

