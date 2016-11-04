from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import Perceptron, LogisticRegression

iris = datasets.load_iris()

data_train, data_test, labels_train, labels_test = train_test_split(
	iris.data, iris.target, test_size=0.4, random_state=0)

algs = [
	GaussianNB(), 
	DecisionTreeClassifier(),
	MultinomialNB(),
	BernoulliNB(), 
	Perceptron(), 
	LogisticRegression(), 
]

# Run through each classifier, train them with the training dataset, then test it using the score function
for alg in algs:
	alg = alg.fit(data_train, labels_train)
	print '%s: %f' % (type(alg).__name__, alg.score(data_test, labels_test))
