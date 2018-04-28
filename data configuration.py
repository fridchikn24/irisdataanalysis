from pandas import read_csv, DataFrame
import numpy

idf = DataFrame()
idf = read_csv('iris data.csv', names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'iris class'])

t = 1