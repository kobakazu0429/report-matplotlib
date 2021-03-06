# coding: utf-8
import math
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

en = FontProperties(
    fname="/Library/Fonts/Times New Roman.ttf")
jp = FontProperties(
    fname="./font.ttc")

FONT_SIZE = 18

# ‘best’
# ‘upper right’
# ‘upper left’
# ‘lower left’
# ‘lower right’
# ‘right’
# ‘center left’
# ‘center right’
# ‘lower center’
# ‘upper center’
# ‘center’

LOC = 'best'

# フォントサイズ
plt.rcParams["font.size"] = FONT_SIZE

# x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.direction'] = 'in'

# y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'

# x軸主目盛り線の線幅
plt.rcParams['xtick.major.width'] = 1.0

# y軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0

# 軸の線幅edge linewidth。囲みの太さ
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['axes.grid'] = True

filepath = './data.xlsx'  # Xlsファイルの場所

pd.options.display.precision = 3
df = pd.read_excel(filepath)  # Pandas DataFrameに読込み

#データフレームからx軸とY軸データを読み込む

#列で指定
# x=df[[0]]
# y=df[[1]]

#ラベルで指定する場合
xColumn = df.columns[0]
yColumn = df.columns[1]
x = df[xColumn]
y = df[yColumn]

# インチ指定
fig = plt.figure(figsize=(12, 10))
fig.subplots_adjust(left=0.2)

ax = fig.add_subplot(111)

ax.set_xlabel(xColumn, fontdict={"fontproperties": en}, fontsize=FONT_SIZE+2)
ax.set_ylabel(yColumn, fontdict={"fontproperties": en}, fontsize=FONT_SIZE+2)

ax.yaxis.set_label_coords(-0.1, 0.5)

ax.set_axisbelow(True)

# y軸小数点以下3桁表示
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.3f'))

# 軸の数字にオフセット(+1.05e9 など)を使わずに表現する
plt.gca().xaxis.get_major_formatter().set_useOffset(False)

# 軸の数字が整数になるようにする
# plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# 軸目盛りの個数指定: y軸, 6個以内
plt.locator_params(axis='y', nbins=6)

plt.scatter(x, y)
# plt.xticks(x, x)

# 凡例をまとめて出力する
handler, label = ax.get_legend_handles_labels()
ax.legend(handler, label, loc=LOC, borderaxespad=0.)

plt.savefig("output.png")
