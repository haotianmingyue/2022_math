#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/9/16
# @file Embedded嵌入法选取特征.py

from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.feature_selection import RFE
import numpy as np
import pandas as pd

path_x = './Data/Molecular_Descriptor.xlsx'
path_y = './Data/ERα_activity.xlsx'

X = pd.read_excel(path_x).iloc[:, 1:]
y = pd.read_excel(path_y).iloc[:, 2]

print(X.shape)
print(y.shape)

# print(X.columns.values)

RFR_ = RFR(n_estimators=10, random_state=0)

Model = SelectFromModel(RFR_, threshold=-np.inf, max_features=20)

x_embedded = Model.fit_transform(X, y)

# print(x_embedded.shape)

x_name = Model.get_feature_names_out(X.columns.values)

print(x_name)

Model_wrap = RFE(RFR_, n_features_to_select=20, step=50)

x_wrapped = Model_wrap.fit(X, y)

x_name_wrap = Model_wrap.get_feature_names_out(X.columns.values)

print(x_name_wrap)
