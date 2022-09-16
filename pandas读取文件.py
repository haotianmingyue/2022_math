#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/8/30
# @file pandas读取文件.py
"""
pandas 读取excel文件，并将其转换成numpy。
根据文件内容具体分析。
"""
import pandas as pd
import numpy as np


# result = pd.read_excel(path)
# # 默认第一行作为列标签
# """
# filename：文件路径，可以设置为绝对路径或相对路径
# sep：分隔符，常用的有逗号 , 分隔、\t 分隔，默认逗号分隔，read_table默认是'\t'(也就是tab)切割数据集的
# header：指定表头，即列名，默认第一行，header = None, 没有表头，全部为数据内容
# encoding：文件编码方式，不设置此选项， Pandas 默认使用 UTF-8 来解码。
# index_col ，指定索引对应的列为数据框的行标签，默认 Pandas 会从 0、1、2、3 做自然排序分配给各条记录。
# 通过names=['a','b','c']可以自己设置列标题
#
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html#pandas.read_excel
# """
# # print(result.iloc[:, :])
#
# # print(result.loc[[0, 1], ['nAcid', 'XLogP']].values)
# # 通过.iloc方法根据索引获取指定的行列，然后通过 .values 转为numpy数据
# # print(result.iloc[:, 1:].values.shape)
# # print(result.iloc[2, 3].isnull())
# print(result)
# # 将缺失值填充为0
# r1 = result.fillna(0)
# print(r1)
# n_data = r1.iloc[:, 1:].values
# print(n_data)

# 然后转为tensor数据 torch.from_numpy(pd_data.values)


#  读取数据并填充缺失值，返回numpy数组
def read_excel_na(path,  row=0, column=0, value=0):
    # 返回一个numpy数组,缺失值用0填充
    '''
    :param path: 读取文件路径
    :param column: 从那一列开始读
    :param row: 从那一行开始读
    :param value: 填充值
    :return: 一个numpy对象
    '''
    result = pd.read_excel(path)
    back = result.fillna(value)
    return back.iloc[row:, column:].values


# 异常值处理 3sigma准则，用平均值代替异常值
def outlier_3sigma(n, row=0, column=0):
    '''
    :param n: numpy数组
    :param column: 从那一列开始处理
    :param row: 从哪一行开始处理
    :return: 处理后的numpy数组
    '''


    #默认第一列是数据
    for i in range(column, len(n[0])):

        mean = np.mean(n[row:, i])
        var = np.var(n[row:, i])
        sigma = var**0.5
        # 总和数
        t_v: float = 0
        # 异常值编号
        o_v = list()
        for j in range(row, len(n)):
            t_v += n[j][i]
            if n[j][i] < mean - 3*sigma or n[j][i] > mean + 3*sigma:
                o_v.append(j)

        for v in o_v:
            t_v -= n[v][i]
        # 新均值
        n_mean = t_v / (len(n) - row + 1 - len(o_v))
        for v in o_v:
            n[v][i] = n_mean

    return n











if __name__ == '__main__':
    path = "./Data/test.xlsx"

    n = read_excel_na(path, 0, 1)
    print(n)
    print(outlier_3sigma(n, 0, 0))




