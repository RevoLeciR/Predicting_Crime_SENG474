from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import Perceptron, LogisticRegression
import csv
import random
import numpy as np

with open('Victoria_BC_Police_Department_Data_class_combine_theft.csv', 'rb') as file:
    reader = csv.reader(file)
    input = list(reader) #list which contains data of file

	
del input[0]

random.shuffle(input)

data = []
labels = []

labels_train = []
data_train = []

data_test = []

train_test = []


train_point = int(0.7 * len(input)) #70/30
#print train_point

theft_count = 0
'''
for i in input:
	if i[5] == 9:
		theft_count += 1

print theft_count, len(input), (float(theft_count)/float(len(input))
#print '-----'
'''
for i in input:
	#3-hour, 4-day of the week, 6-month, 7-day of the month
	data.append([int(i[3]),int(i[4]),int(i[6])])
	labels.append(int(i[5]))
	if int(i[5]) == 9:
		theft_count += 1

print theft_count, len(input)

data_train = data[:train_point]
labels_train = labels[:train_point]

data_test = data[train_point:]
labels_predict_actual = labels[train_point:]

'''
for i in range(len(data_train)):
	print str(data_train[i]) + " -> " + str(labels_train[i])
'''
#print data_train

'''
clf = GaussianNB()
clf = clf.fit(data_train, labels_train)

predict = clf.predict(data_test)

correct = 0
for i in range(midpoint):
	if predict[i] == labels_predict_actual[i]:
		correct += 1
		
print correct		
print "GaussianNB: " + str((correct/float(len(data_test))))
'''

algs = [
        GaussianNB(),
        DecisionTreeClassifier(),
        MultinomialNB(),
        BernoulliNB(),
        Perceptron(),
        LogisticRegression(),
]

#Run through each classifier, train them with the training dataset, then test it using the score function
for alg in algs:
        alg = alg.fit(data_train, labels_train)
        print '%s: %f' % (type(alg).__name__, alg.score(data_test, labels_predict_actual))
