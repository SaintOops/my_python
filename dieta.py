import matplotlib.pyplot as plt
%matplotlib inline

m = 75

left_edges = list(range(1,7))
heights = [m-i for i in list(np.arange(1.5,10,1.5))]
bar_width = 0.5
plt.bar(left_edges, heights, bar_width)
plt.show()
