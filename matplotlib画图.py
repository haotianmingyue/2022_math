#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/8/30
# @file matplotlib画图.py

from matplotlib import pyplot as plt
import numpy as np

# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# 显示汉字
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号为框
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y)
ax1.set_title(label='汉字')

# 设置标签
ax1.set_xlabel("x轴")
ax2.set_ylabel("y轴")

# 设置刻度
ax1.set_xticks(range(15))
# ax1.set_yticks(range(0, 2, 1))

# 设置坐标上下限值
# ax1.set_xlim(5, 10)
# ax1.set_ylim(-1, 1)

fig.show()
