import csv

with open('Victoria_BC_Police_Department_Data_date.csv','rb') as fr:
	reader = csv.reader(fr)
	testlist = list(reader)

del testlist[0]
	
child_word = {}
parent_word = {}

child_whole = {}
parent_whole = {}

parent_child = {}

other = {}
other_count = 0
listcount = 0

#1 for incident_type_primary; 9 for parent_incident type
#output of primary is in caps; parent_incident is in normal
for i in range(len(testlist)):
	listcount += 1
	#print testlist[i][1]
	#print testlist[i][9]
	#print testlist[i][1]
	#print testlist[i][1].split()
	#print len(testlist[i][1].split())
	
#----- WHOLE SECTION ----	
	temp_child_whole = testlist[i][1] #String variable
	check_child_whole = child_whole.get(temp_child_whole)

	if check_child_whole is None:
		child_whole[temp_child_whole] = 1
	else:
		child_whole[temp_child_whole] += 1
		
	temp_parent_whole = testlist[i][9]
	check_parent_whole = parent_whole.get(temp_parent_whole)
	
	if check_parent_whole is None:
		parent_whole[temp_parent_whole] = 1
	else:
		parent_whole[temp_parent_whole] += 1
	
	if (temp_parent_whole == "Other"):
		parentchild = temp_parent_whole + "//" + temp_child_whole
		other_count += 1
	
		check_parentchild = other.get(parentchild)
		if check_parentchild is None:
			other[parentchild] = 1
		else:
			other[parentchild] += 1

#----- WORD SECTION -----		
	for j in range(len(testlist[i][1].split())):
		temp_child_word = testlist[i][1].split()[j]
		check_child_word = child_word.get(temp_child_word)
		
		if check_child_word is None:
			child_word[temp_child_word] = 1
		else:
			child_word[temp_child_word] += 1
		
	for k in range(len(testlist[i][9].split())):
		temp_parent_word = testlist[i][9].split()[k]
		check_parent_word = parent_word.get(temp_parent_word)
		
		if check_parent_word is None:
			parent_word[temp_parent_word] = 1
		else:
			parent_word[temp_parent_word] += 1

print other
print other_count
print listcount
'''			
new_parent_file = open("parent_crime.txt", "w")
new_parent_file.write("Parent Whole\n")
for i in range(len(parent_whole)):
	new_parent_file.write(sorted(parent_whole, key = parent_whole.get)[i] + ": " + str(sorted(parent_whole.values())[i]) + "\n")

new_parent_file.write("\nParent Words\n")
for i in range(len(parent_word)):
	new_parent_file.write(sorted(parent_word, key = parent_word.get)[i] + ": " + str(sorted(parent_word.values())[i]) + "\n")
	
new_parent_file.close()

new_child_file = open("child_crime.txt", "w")
new_child_file.write("Child Whole\n")
for i in range(len(child_whole)):
	new_child_file.write(sorted(child_whole, key = child_whole.get)[i] + ": " + str(sorted(child_whole.values())[i]) + "\n")

new_child_file.write("\nChild Words\n")
for i in range(len(child_word)):
	new_child_file.write(sorted(child_word, key = child_word.get)[i] + ": " + str(sorted(child_word.values())[i]) + "\n")
new_child_file.close()
'''

'''			
temp_str = "hi" + ':' + "there"

print temp_str
'''

'''
print 'parent word'
print sorted(parent_word.values())
print sorted(parent_word, key = parent_word.get)
print ''

print 'parent whole'
print sorted(parent_whole.values())
print sorted(parent_whole, key = parent_whole.get)

print ''

print 'child word'
print sorted(child_word.values())
print sorted(child_word, key = child_word.get)

print ''

print 'child whole'
print sorted(child_whole.values())
print sorted(child_whole, key = child_whole.get)
'''

'''
print 'Printing Child Whole Dictionary'			
print child_whole
print ''
print 'parent whole'
print parent_whole
print ''
print 'child word'
print child_word
print ''
print 'parent word'
print parent_word
'''