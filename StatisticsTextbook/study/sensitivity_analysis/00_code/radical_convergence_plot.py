import matplotlib.pyplot as plt
import numpy as np
from typing import List


inner_circle_size = np.array([0.1, 0.02, 0.2, 0.5, 0.01, 0.01, 0.1, 0.02, 0.02, 0.02,
                              0.1, 0.02, 0.2, 0.5, 0.01, 0.01, 0.1, 0.02, 0.02, 0.02])
outer_circle_size = np.array([0.05, 0.2, 0.25, 0.35, 0.25, 0.15, 0.15, 0.2, 0.3, 0.4,
                              0.05, 0.2, 0.25, 0.35, 0.25, 0.15, 0.15, 0.2, 0.3, 0.4])
colors: List[str] = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                     '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                     '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                     '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
text: List[str] = colors

n = len(inner_circle_size)
angle = np.arange(0, np.pi * 2, np.pi * 2 / n)
radius = 2 * np.ones(angle.shape)

x_circle = radius * np.cos(angle)
y_circle = radius * np.sin(angle)
x_len = len(x_circle)

fig = plt.figure(figsize=(9, 9))

for idx in range(x_len):
    # S_i
    plt.scatter(x_circle[idx], y_circle[idx],
                color="white", alpha=1, edgecolors="none",
                s=(inner_circle_size[idx] * 2500), marker='o', zorder=1)

    plt.scatter(x_circle[idx], y_circle[idx],
                color=colors[idx], alpha=0.5, edgecolors='none',
                s=(inner_circle_size[idx] * 2500), marker='o', zorder=2)

    # S_T
    plt.scatter(x_circle[idx], y_circle[idx],
                facecolors='none', edgecolors='black',
                s=(outer_circle_size[idx] * 2500), marker='o', zorder=2)

    # variable name
    if x_circle[idx] > 0:
        rotation_angle = angle[idx] * 180/np.pi
    else:
        rotation_angle = angle[idx] * 180/np.pi + 180

    mul = 1.5
    x_test = mul * radius[idx] * np.cos(angle[idx])
    y_test = mul * radius[idx] * np.sin(angle[idx])
    plt.text(x_test, y_test, text[idx],
             color=colors[idx], size=15,
             rotation=rotation_angle, rotation_mode='anchor',
             horizontalalignment='center', verticalalignment='center')

# line S_ij
plt.plot([x_circle[1], x_circle[4]], [y_circle[1], y_circle[4]],
         linewidth=1, color='k', alpha=0.3, zorder=0)
plt.plot([x_circle[0], x_circle[10]], [y_circle[0], y_circle[10]],
         linewidth=5, color='k', alpha=0.3, zorder=0)
plt.plot([x_circle[6], x_circle[2]], [y_circle[6], y_circle[2]],
         linewidth=2, color='k', alpha=0.3, zorder=0)
plt.plot([x_circle[5], x_circle[3]], [y_circle[5], y_circle[3]],
         linewidth=1, color='k', alpha=0.3, zorder=0)

plt.plot([x_circle[11], x_circle[7]], [y_circle[11], y_circle[7]],
         linewidth=1, color='k', alpha=0.3, zorder=0)
plt.plot([x_circle[10], x_circle[7]], [y_circle[10], y_circle[7]],
         linewidth=5, color='k', alpha=0.3, zorder=0)
plt.plot([x_circle[18], x_circle[12]], [y_circle[18], y_circle[12]],
         linewidth=2, color='k', alpha=0.3, zorder=0)
plt.plot([x_circle[5], x_circle[13]], [y_circle[5], y_circle[13]],
         linewidth=1, color='k', alpha=0.3, zorder=0)

# figure setting
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.yticks(ticks=[])
plt.xticks(ticks=[])
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()
