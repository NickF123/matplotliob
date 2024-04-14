#Uses Mathplotlib lib to calculate and display a boxplot

import matplotlib.pyplot as plt


plt.style.use('classic')


#D = [5340, 5300, 5520, 5340, 5320, 4290, 5260, 4330, 1000]
D2 = [5710, 5755, 5850, 5880, 5880, 5890, 5920, 5940, 5950, 6050, 6130, 6325]
#D3 = [D, D2]
# plot
fig, ax = plt.subplots()
BP = ax.boxplot(D2, widths=.25, patch_artist=True,
                vert=False,
                sym='*',
                showcaps=False,
                medianprops = {"color": "black", "linewidth": 1},
                boxprops = {"facecolor": "white", "edgecolor": "black",
                         "linewidth": 1},
                whiskerprops = {"color": "black", "linewidth": 1},
                capprops = {"color": "black", "linewidth": 1})



plt.show()

