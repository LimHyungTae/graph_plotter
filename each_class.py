COLORSET = [(241/255.0, 50/255.0, 50/255.0), (19/255.0, 163/255.0, 153/255.0),(2/255.0, 23/255.0, 157/255.0),  (191/255.0, 17/255.0, 46/255.0)]
# COLORSET = [(241/255.0, 50/255.0, 50/255.0), (2/255.0, 23/255.0, 157/255.0)]
SOFT_COLORSET = [(241/255.0, 187/255.0, 165/255.0), (174/255.0, 245/255.0, 231/255.0), (115/255.0, 123/255.0, 173/255.0), (232/255.0, 138/255.0, 139/255.0)]
LINE = [':', '-.', '--', '--']
LABEL = ['ref-d', 'rgb']
# LABEL = ['PF', 'Multimodal+A.'] #Non-multimodal', 'Bi-multimodal']
MARKER = ['o','^','s','*', "v"]

import matplotlib.pyplot as plt

from random import random
import numpy as np


import os
legends = ["rgb", "ref-d"]
folder_dir = "each_w_header"
csv_names = ["ref_d_each_class.csv", "rgb_each_class.csv"]

fig1, ax1 = plt.subplots()
from matplotlib.ticker import FormatStrFormatter
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
import pandas as pd

KEYS = ["rmse", "absrel", "delta1", "delta2"]
key = KEYS[0]

reader = pd.read_csv(os.path.join(folder_dir, "gt_each_class.csv"))
x = list(reader["mean"]) # key: "mean" or "std"

targets = []
for idx, csv_name in enumerate(csv_names):
    reader = pd.read_csv(os.path.join(folder_dir, csv_name))
    data = list(reader[key])
    x_pt, y_pt = (list(t) for t in zip(*sorted(zip(x, data))))
    plt.plot(x_pt, y_pt, color=COLORSET[idx], marker=MARKER[idx],
                         linestyle=LINE[idx], label=LABEL[idx],
                        linewidth=2)
# plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
# plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
# plt.xlim(0., 0.6)
# plt.ylim(0.45, 0.6)
plt.legend()
# plt.xlim(-0.5,1.5)
# plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
# plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
# plt.ylim(-0.5,1.5)
plt.xlabel("Inference time [ms]")
plt.ylabel("RMSM [m]")
fig = plt.gcf()
fig.savefig("please.png")
# f