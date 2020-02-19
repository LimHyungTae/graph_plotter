COLORSET = [(241/255.0, 50/255.0, 50/255.0), (19/255.0, 163/255.0, 153/255.0),(2/255.0, 23/255.0, 157/255.0),  (191/255.0, 17/255.0, 46/255.0)]
# COLORSET = [(241/255.0, 50/255.0, 50/255.0), (2/255.0, 23/255.0, 157/255.0)]
SOFT_COLORSET = [(241/255.0, 187/255.0, 165/255.0), (174/255.0, 245/255.0, 231/255.0), (115/255.0, 123/255.0, 173/255.0), (232/255.0, 138/255.0, 139/255.0)]
LINE = [':', '-.', '--', '--']
LABEL = ['Liao $et\:al.[@]$', 'Ma $et\:al.$[@]', 'Ours']
# LABEL = ['PF', 'Multimodal+A.'] #Non-multimodal', 'Bi-multimodal']
MARKER = ['o','^','s','*', "v"]

import matplotlib.pyplot as plt

from random import random
import numpy as np


# plt.text(0.55, 0.6, "A", fontdict={"size":20, "weight": "bold"},
#          ha="right", va="top",
#          bbox=dict(boxstyle="square",
#                    ec=(0., 0., 0.),
#                    fc=(0.95, .95, 0.95),
#                    )
#          )
# fig = plt.gcf()
# plt.show()
# fig.savefig("test.png")


# Liao
i = 0
plt.scatter(10, 0.553, color=COLORSET[i], marker=MARKER[i], label=LABEL[i], s=100)
plt.grid(True)

# Ma
i = 1
plt.scatter(20, 0.504, color=COLORSET[i], marker=MARKER[i], label=LABEL[i], s=100)
plt.grid(True)


ours_gpu_time = [9, 15, 32]
RMSE = [0.512, 0.496, 0.485]
idx = 2
ms = 10
plt.plot(ours_gpu_time, RMSE, color=COLORSET[idx], marker=MARKER[idx],
                     linestyle=LINE[idx], label=LABEL[idx],
                    linewidth=2, markersize=ms)
# plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
# plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
plt.xlim(0., 0.6)
plt.ylim(0.45, 0.6)
plt.legend()
# plt.xlim(-0.5,1.5)
# plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
# plt.xticks(np.linspace(-0.5,1.5,10, endpoint =True))
# plt.ylim(-0.5,1.5)
plt.xlabel("Inference time [ms]")
plt.ylabel("RMSM [m]")
fig = plt.gcf()
plt.show()
fig.savefig("test.png")
