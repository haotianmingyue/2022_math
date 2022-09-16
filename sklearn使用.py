#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/9/13
# @file sklearn使用.py
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


path = "./Data/test.xlsx"
data = pd.read_excel(path)

print(data)


# imp_mean = SimpleImputer()
#
# ages = data.iloc[:, 1].values.reshape(-1, 1)
# # print(ages)
# imp_mean = imp_mean.fit_transform(ages)
#
# print(imp_mean)


y = data.iloc[:, -1]

le = LabelEncoder()
le = le.fit(y)
label = le.transform(y)
print(label)