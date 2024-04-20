import numpy as np

from sklearn.datasets import load_iris

from sklearn import tree

iris = load_iris()

testindex = [0,50,100]

#training data

traintarget = np.delete(iris.target, testindex)

traindata = np.delete(iris.data, testindex, axis = 0)

#testing data
testtarget = iris.target[testindex]
testdata = iris.data[testindex]

clf = tree.DecisionTreeClassifier()
clf.fit(traindata, traintarget)

print(testtarget)
print(clf.predict(testdata))

#viz code


from six import StringIO
import pydot

dot_data=StringIO()
tree.export_graphviz(clf, out_file = dot_data, feature_names= iris.feature_names, class_names = iris. target_names, filled=True, rounded=True,impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())


graph[0].write_pdf("iris.pdf")

print(testdata[0], testtarget[0])

