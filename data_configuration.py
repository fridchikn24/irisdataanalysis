import pandas as pd
from pandas import read_csv, DataFrame
import numpy


def iris_get():
    idf = DataFrame()
    idf = read_csv('iris data.csv', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_class'])
    return idf

def data_split(bigframe, string):
    ndf = dict(list(bigframe.groupby('iris_class')))
    newdf = ndf[string]
    return newdf

def sig_values(frame):
    sf = pd.DataFrame([frame.mean, frame.std, frame.var, frame.count],
                   index=['mean','stddev', 'var','count'])
    return sf

