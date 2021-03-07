# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

filepath = './vector.xlsx'  # Xlsファイルの場所

pd.options.display.precision = 3
df = pd.read_excel(filepath)  # Pandas DataFrameに読込み

#データフレームからx軸とY軸データを読み込む

#ラベルで指定する場合

name0 = df.columns[0]
name1 = df.columns[1]
name2 = df.columns[2]
name3 = df.columns[3]

V1 = df[name0]
V2 = df[name1]
V3 = df[name2]
V4 = df[name3]


colorlist = ["r", "g", "b", "c", "m", "y", "k", "w"]

plt.subplots(figsize=(10, 10))
# plt.figure()

Q = plt.quiver(0, 0, V1[0], V1[1], angles='xy',
               scale_units='xy', scale=1, color=colorlist)
qk = plt.quiverkey(Q, 0.8, 0.85 , 2, name0,
                   labelpos='E', coordinates='figure')

Q = plt.quiver(0, 0, V2[0], V2[1], angles='xy',
               scale_units='xy', scale=1, color=colorlist[1])
qk = plt.quiverkey(Q, 0.8, 0.825, 2, name1,
                   labelpos='E', coordinates='figure')

Q = plt.quiver(0, 0, V3[0], V3[1], angles='xy',
               scale_units='xy', scale=1, color=colorlist[2])
qk = plt.quiverkey(Q, 0.8, 0.80, 2, name2,
                   labelpos='E', coordinates='figure')

Q = plt.quiver(0, 0, V4[0], V4[1], angles='xy',
               scale_units='xy', scale=1, color=colorlist[3])
qk = plt.quiverkey(Q, 0.8, 0.775, 2, name3,
                   labelpos='E', coordinates='figure')

# グラフ表示
plt.xlim([-1, 11000])
plt.ylim([-3, 1])
plt.grid()
plt.draw()
# plt.show()
plt.savefig("output.png", bbox_inches='tight', dpi=100)
