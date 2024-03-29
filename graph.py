import matplotlib.pyplot as plt

x=[38.24,39.57,40.56,36.26,33.48,37.56,38.42,37.52,41.23,41.17,36.08,38.47,38.15,37.51,35.49,39.36,38.09,36.09,40.44,40.33,40.37,37.57]
y=[20.42,26.15,25.32,23.12,10.54,12.19,13.11,20.44,9.1,13.05,-5.21,15.13,15.35,15.17,14.32,19.56,24.36,23,13.57,14.15,14.23,22.56]


fig, ax = plt.subplots()
ax.scatter(x, y,marker='o')

for i in range(len(x)):
    ax.annotate(i, (x[i], y[i]))

plt.show()