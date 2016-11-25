from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn import svm
import csv
import random
import numpy as np

with open('Central_Saanich_Police_Service_class_combine_theft.csv', 'rb') as file:
    reader = csv.reader(file)
    input = list(reader) #list which contains data of file

#--SETUP--
	
del input[0]

random.shuffle(input)
random.shuffle(input)

data = []
labels = []

labels_train = []
data_train = []

data_predict = []

train_test = []

#Count how many thefts in original data
theft_count = 0
for i in input:
	if int(i[5]) == 9:
		theft_count += 1

print "\nTheft count in entire data: " + str(theft_count)	
breakpoint = 0.7
predict_set = 100-(breakpoint*100)
train_point = int(breakpoint * len(input)) #70/30

theft_percentage = float(theft_count)/float(len(input))

print "Theft percentage in entire data: " + str(theft_percentage) #0.461554779858
print "Using " + str(int(breakpoint*100)) + "/" + str(int(predict_set))
counted_thefts = 0
here = 0

for i in input:
	data.append([int(i[3]),int(i[4]),int(i[6])])
	labels.append(int(i[5]))

#--Train the data--
data_train = data[:train_point]
labels_train = labels[:train_point]

data_predict = data[train_point:]
labels_predict_actual = labels[train_point:]

pre_train_thefts = 0
for i in range(len(data_train)):
	if labels_train[i] == 9:
		pre_train_thefts += 1
		
print "\nThefts in pre training data: " + str(pre_train_thefts)
print "Size of pre training data: " + str(len(data_train))
print "Percentage of Thefts in pre training data: " + str(float(pre_train_thefts)/float(len(data_train)))

#NEW DATA TRAIN - LIMIT THEFTS BEFORE TRAINING
new_data_train = []
new_labels_train = []

softcap = 0.7
#softcap = float(raw_input("\nEnter a soft cap: "))
theftcap = softcap * int(pre_train_thefts)
print "\nSoft cap multiplier: " + str(softcap)

post_train_thefts = 0
for i in range(len(data_train)):
	if int(labels_train[i]) == 9:
		if post_train_thefts < int(theftcap):
			new_data_train.append(data_train[i])
			new_labels_train.append(labels_train[i])
		post_train_thefts += 1
	else:
		new_data_train.append(data_train[i])
		new_labels_train.append(labels_train[i])

new_train_theft = 0
for i in range(len(new_labels_train)):
	if new_labels_train[i] == 9:
		new_train_theft += 1
		
print "\nThefts in new training data: " + str(new_train_theft)
print "Size of new training data: " + str(len(new_data_train))
print "Percentage of Thefts in new training data: " + str(float(new_train_theft)/float(len(new_data_train))) + "\n"
'''
#LIMIT THEFTS IN PREDICTION SETUP. 
pre_predict_thefts = 0
for i in range(len(data_predict)):
	if int(labels_predict_actual[i]) == 9:
		pre_predict_thefts += 1

new_data_predict = []
new_labels_predict_actual = []	

pred_theftcap = softcap * int(pre_predict_thefts)

post_pred_thefts = 0
for i in range(len(data_predict)):
	if int(labels_predict_actual[i]) == 9:
		if post_pred_thefts < int(pred_theftcap):
			new_data_predict.append(data_predict[i])
			new_labels_predict_actual.append(labels_predict_actual[i])
		post_pred_thefts += 1
	else:
		new_data_predict.append(data_predict[i])
		new_labels_predict_actual.append(labels_predict_actual[i])
'''

algs = [
        GaussianNB(),
        DecisionTreeClassifier(),
        MultinomialNB(),
        BernoulliNB(),
        Perceptron(),
        LogisticRegression(),
]

print "\nSoft Cap: OFF"
for alg in algs:
        alg = alg.fit(data_train, labels_train)
        print '%s: %f' % (type(alg).__name__, alg.score(data_predict, labels_predict_actual))
#Run through each classifier, train them with the training dataset, then test it using the score function
print "\nSoft Cap: ON. Soft Cap Multiplier: " + str(softcap)
for alg in algs:
        alg = alg.fit(new_data_train, new_labels_train)
        print '%s: %f' % (type(alg).__name__, alg.score(data_predict, labels_predict_actual))
