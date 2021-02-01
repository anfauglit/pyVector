import matplotlib.pyplot as plt
import numpy as np

notes = ['A', 'B'] 
vectors = np.array([[2,3], [-1,1]])
vector_sum = vectors[0] + vectors[1]
notes.append('A+B')
vector_mult= vectors[0] * 3 
notes.append('3A')
vector_mult2= vectors[1] * -2 
notes.append('-2B')
vectors = np.append(vectors, np.array([vector_sum]), axis=0)
vectors = np.append(vectors, np.array([vector_mult]), axis=0)
vectors = np.append(vectors, np.array([vector_mult2]), axis=0)

origin = np.zeros((2, len(vectors)), dtype=int)

plot_limits = (-10, 10)
fig, ax = plt.subplots()
ax.quiver(*origin, vectors[:,0], vectors[:,1], angles='xy', scale_units='xy',
    scale=1, width = 0.004)

ax.scatter(vectors[:,0], vectors[:,1], s=20, c='k')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# plt.vlines(0, *plot_limits, colors='k', linewidth=0.5) 
# plt.hlines(0, *plot_limits, colors='k', linewidth=0.5) 

for i, point in enumerate(vectors):
    plt.annotate(notes[i], point, xytext=[point[0] + 0.3, point[1] - 0.3])

plt.xlim(*plot_limits)
plt.ylim(*plot_limits)
plt.xticks(np.arange(min(plot_limits), max(plot_limits) + 1, 2))
plt.yticks(np.arange(min(plot_limits), max(plot_limits) + 1, 2))

plt.show()
