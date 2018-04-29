import pandas as pd
from pandas import read_csv, DataFrame
import numpy


def iris_get():
    idf = DataFrame()
    idf = read_csv('iris data.csv', names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'iris class'])
    return idf

def data_split(bigframe, string):
    newdf = bigframe.loc['string']
    return newdf

def sig_values(frame):
    sf = pd.Series([frame.mean, frame.std, frame.var, frame.count],
                   index=['mean','stddev', 'var','count'])
    return sf

