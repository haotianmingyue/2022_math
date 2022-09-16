#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/9/16
# @file PCA.py

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pandas as pd


iris = load_iris()

y = iris.target
x = iris.data

print(x.shape)
print(pd.DataFrame(x))


pca = PCA(n_components=2)
pca_data = pca.fit_transform(x)

print(pca_data)
